# Grande Metabolic Stability Model — Core stability equations

from biochem.nadph_balance import nadph_net_change
from biochem.bh4_cycle import bh4_net_change
from biochem.no_onoo_cycle import no_onoo_net_change

from geometry.geometry_adapter import geometry_to_friction
from sirtuins.sirtuin_network import sirtuin_activity_index


def compute_friction(state, geom_params):
    """
    Beregn friksjon (ζ) fra geometri.
    Bruker:
    - SAM (metylstatus)
    - H (homocystein)
    - F (eksisterende friksjon / metabolsk motstand)
    - CL_fraction (cardiolipin)
    """
    SAM = state["SAM"]
    H = state["H"]
    F = state["friction"]
    CL_fraction = state["CL_fraction"]

    return geometry_to_friction(SAM, H, F, CL_fraction, geom_params)


def compute_sirtuin_index(state, sirt_params):
    """
    Beregn samlet sirtuin-aktivitet (S-index).
    """
    NAD = state["NAD"]
    NADH = state["NADH"]
    NADPH = state["NADPH"]
    ROS = state["ROS"]

    return sirtuin_activity_index(NAD, NADH, NADPH, ROS, sirt_params)


def stability_derivatives(state, params):
    """
    Beregner tidsderivater for kjernestørrelser i modellen.
    state: dict med tilstander
    params: dict med alle parametere (inkl. geom_params, sirt_params)
    """

    geom_params = params["geometry"]
    sirt_params = params["sirtuins"]

    # 1. Oppdater friksjon fra geometri
    new_friction = compute_friction(state, geom_params)

    # 2. Sirtuin-indeks
    S_index = compute_sirtuin_index(state, sirt_params)

    # 3. NADPH-dynamikk
    dNADPH = nadph_net_change(
        state["pentose_flux"],
        state["idh_flux"],
        state["malic_flux"],
        state["ROS"],
        state["RNS"],
        state["BH2"],
        state["NOX_activity"],
        params["k_pentose"],
        params["k_idh"],
        params["k_malic"],
        params["k_antiox"],
        params["k_bh4"],
        params["k_nox"],
    )

    # 4. BH4-dynamikk
    dBH4, dBH2 = bh4_net_change(
        state["BH4"],
        state["BH2"],
        state["ROS"],
        state["RNS"],
        params["k_ox"],
        params["k_red"]
    )

    # 5. NO/ONOO--dynamikk
    dNO, dONOO = no_onoo_net_change(
        state["NO"],
        state["ONOO"],
        state["ROS"],
        state["RNS"],
        params["k_no_prod"],
        params["k_no_cons"],
        params["k_onoo_form"],
        params["k_onoo_clear"]
    )

    # 6. En enkel friksjonsdynamikk (relakserer mot geometri-bestemt friksjon)
    dFriction = params["k_fric_relax"] * (new_friction - state["friction"])

    # 7. Returner derivater + nytt S-index (kan brukes videre)
    return {
        "dNADPH": dNADPH,
        "dBH4": dBH4,
        "dBH2": dBH2,
        "dNO": dNO,
        "dONOO": dONOO,
        "dFriction": dFriction,
        "S_index": S_index,
    }

