import numpy as np

# ---------------------------------------------------------
#  Friction Model — Grande Metabolic Friction Framework
# ---------------------------------------------------------
#  Denne modulen inneholder:
#   - U-formet friksjonskurve
#   - Metabolsk friksjon (ζ_metabolsk)
#   - Kjernefriksjon (ζ_kjerne)
#   - Total friksjon (ζ_total)
# ---------------------------------------------------------


# -----------------------------
# 1. U-formet friksjonskurve
# -----------------------------
def u_shaped_friction(x, x_opt=1.0, a=1.2):
    """
    U-formet friksjonsfunksjon.
    Minimum ved x_opt.
    """
    return a * (x - x_opt)**2


# -----------------------------
# 2. Metabolsk friksjon
# -----------------------------
def metabolic_friction(NAD_ratio, homocysteine, weight_nad=0.6, weight_hcy=0.4):
    """
    Metabolsk friksjon:
    - Lav NAD+ → høy friksjon
    - Høy homocystein → høy friksjon
    """
    return weight_hcy * homocysteine + weight_nad * (1 / (NAD_ratio + 1e-9))


# -----------------------------
# 3. Kjernefriksjon
# -----------------------------
def nuclear_friction(DSB_load, chromatin_noise, w_dsb=0.7, w_noise=0.3):
    """
    Kjernefriksjon:
    - Høy DSB-belastning → høy friksjon
    - Høy kromatin-støy → høy friksjon
    """
    return w_dsb * DSB_load + w_noise * chromatin_noise


# -----------------------------
# 4. Total friksjon
# -----------------------------
def total_friction(z_metabolic, z_nuclear):
    """
    Total friksjon = metabolsk + kjerne
    """
    return z_metabolic + z_nuclear

