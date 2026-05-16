# Grande Metabolic Stability Model — Geometry adapter

from .curvature_effects import total_curvature
from .cristae_topology import topology_state, topology_efficiency


def geometry_to_friction(SAM, H, F, CL_fraction, params):
    """
    Oversetter geometri → friksjon (ζ).
    Kombinerer:
    - kurvatur (SAM, Hcy, CL, friksjon)
    - cristae-topologi (tubular vs lamellar)
    """
    # 1. Beregn total kurvatur
    C = total_curvature(
        SAM, params["K_SAM"], params["C_max"],
        H, params["H0"], params["k_hcy"],
        F, params["k_fric"],
        CL_fraction, params["CL_min"], params["k_cl"]
    )

    # 2. Bestem topologi
    topo = topology_state(CL_fraction, params["CL_threshold"])

    # 3. Effektivitetsfaktor
    eff = topology_efficiency(
        topo,
        params["eff_tubular"],
        params["eff_lamellar"]
    )

    # 4. Friksjon øker når kurvatur faller og topologi blir lamellar
    return params["base_friction"] * (1.0 + eff * (1.0 - C))
