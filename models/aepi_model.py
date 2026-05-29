import numpy as np

# ---------------------------------------------------------
#  Aepi Model — Grande–Sinclair Epigenetic Stability Index
# ---------------------------------------------------------
#  Denne modulen inneholder:
#   - SIRT_ledig: tilgjengelige sirtuiner etter DSB-belastning
#   - gamma_friksjon: epigenetisk friksjon (støy)
#   - MGI: metabolsk gradientintegritet
#   - Aepi: samlet epigenetisk stabilitetsindeks
#
#  Alle funksjoner er laget for å være:
#   - modulære
#   - publiseringsklare
#   - kompatible med notebooks og simuleringer
# ---------------------------------------------------------


# -----------------------------
# 1. SIRT_ledig
# -----------------------------
def SIRT_ledig(SIRT_total, DSB_load, k_dsb=0.15):
    """
    Beregner tilgjengelige sirtuiner etter DNA-skadebelastning.
    SIRT_ledig = SIRT_total * exp(-k_dsb * DSB_load)
    """
    return SIRT_total * np.exp(-k_dsb * DSB_load)


# -----------------------------
# 2. gamma_friksjon
# -----------------------------
def gamma_friksjon(NAD_ratio, homocysteine, alpha=1.8, beta=0.6):
    """
    Epigenetisk friksjon (støy).
    Høy homocystein → høy friksjon.
    Høy NAD+/NADH → lav friksjon.
    """
    return alpha * homocysteine - beta * NAD_ratio


# -----------------------------
# 3. MGI — Metabolic Gradient Integrity
# -----------------------------
def MGI(NAD_ratio, ATP_ratio, weight_nad=0.65, weight_atp=0.35):
    """
    Metabolsk gradientintegritet.
    Kombinerer NAD+/NADH og ATP/ADP til én stabilitetsverdi.
    """
    return weight_nad * NAD_ratio + weight_atp * ATP_ratio


# -----------------------------
# 4. Aepi — Epigenetic Stability Index
# -----------------------------
def Aepi(SIRT_ledig_value, gamma_value, MGI_value,
         w_sirt=0.45, w_gamma=0.30, w_mgi=0.25):
    """
    Grande–Sinclair epigenetisk stabilitetsindeks.
    Høyere verdi = bedre epigenetisk stabilitet.
    """
    return (w_sirt * SIRT_ledig_value) - (w_gamma * gamma_value) + (w_mgi * MGI_value)


# -----------------------------
# 5. Full pipeline
# -----------------------------
def compute_Aepi(
    SIRT_total,
    DSB_load,
    NAD_ratio,
    homocysteine,
    ATP_ratio,
    params=None
):
    """
    Komplett Aepi-beregning i én funksjon.
    Brukes i simuleringer og Monte Carlo.
    """

    # Standardparametre
    if params is None:
        params = {
            "k_dsb": 0.15,
            "alpha": 1.8,
            "beta": 0.6,
            "weight_nad": 0.65,
            "weight_atp": 0.35,
            "w_sirt": 0.45,
            "w_gamma": 0.30,
            "w_mgi": 0.25
        }

    # Beregninger
    sirt = SIRT_ledig(SIRT_total, DSB_load, params["k_dsb"])
    gamma = gamma_friksjon(NAD_ratio, homocysteine, params["alpha"], params["beta"])
    mgi = MGI(NAD_ratio, ATP_ratio, params["weight_nad"], params["weight_atp"])

    # Aepi
    return Aepi(sirt, gamma, mgi,
                params["w_sirt"],
                params["w_gamma"],
                params["w_mgi"])

