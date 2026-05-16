
# Grande Metabolic Stability Model — Core Stability Equations

def d_zeta_dt(ONOO, ROS, NADPH, k_onoo, k_ros, k_repair):
    """
    Time derivative of the friction coefficient ζ.
    """
    return -k_onoo * ONOO - k_ros * ROS + k_repair * NADPH


def load_total(L_mito, L_rib, L_mem, L_redox):
    """
    Total metabolic load L.
    """
    return L_mito + L_rib + L_mem + L_redox


def d_nadph_dt(P_pentose, C_BH4, C_GSH, C_lipid):
    """
    NADPH balance equation.
    """
    return P_pentose - C_BH4 - C_GSH - C_lipid


def bh4_ss(k_regen, NADPH, k_ox, k_uncouple):
    """
    Steady-state BH4 level.
    """
    return (k_regen * NADPH) / (k_ox + k_uncouple)


def onoo_rate(k_uncouple, NO, O2):
    """
    ONOO- production rate.
    """
    return k_uncouple * NO * O2


def zeta_total(zeta_CL, zeta_redox, zeta_geom):
    """
    Total ζ from cardiolipin, redox, and geometry contributions.
    """
    return zeta_CL * zeta_redox * zeta_geom


def stability(L, zeta, alpha):
    """
    Stability equation S = L / ζ^α.
    """
    return L / (zeta ** alpha)
