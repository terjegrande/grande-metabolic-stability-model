# Grande Metabolic Stability Model — Curvature and membrane geometry effects

import math


def curvature_from_SAM(SAM, K_SAM, C_max):
    """
    SAM-avhengig membrankurvatur.
    C øker når SAM er høy, og flater ut når SAM er lav.
    """
    return C_max * SAM / (K_SAM + SAM)


def curvature_penalty_homocysteine(H, H0, k_hcy):
    """
    Homocystein reduserer kurvatur ved å hemme metylsyklusen.
    """
    if H <= H0:
        return 0.0
    return -k_hcy * (H - H0)


def curvature_penalty_friction(F, k_fric):
    """
    Friksjon (metabolsk motstand) reduserer effektiv kurvatur.
    """
    return -k_fric * F


def curvature_penalty_CL(CL_fraction, CL_min, k_cl):
    """
    Cardiolipin-tap reduserer krumning og destabiliserer cristae.
    """
    if CL_fraction >= CL_min:
        return 0.0
    return -k_cl * (CL_min - CL_fraction)


def total_curvature(SAM, K_SAM, C_max,
                    H, H0, k_hcy,
                    F, k_fric,
                    CL_fraction, CL_min, k_cl):
    """
    Total kurvatur = SAM-drevet kurvatur + alle straffefaktorer.
    """
    base = curvature_from_SAM(SAM, K_SAM, C_max)
    penalty_h = curvature_penalty_homocysteine(H, H0, k_hcy)
    penalty_f = curvature_penalty_friction(F, k_fric)
    penalty_cl = curvature_penalty_CL(CL_fraction, CL_min, k_cl)

    return base + penalty_h + penalty_f + penalty_cl
