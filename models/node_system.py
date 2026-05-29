import numpy as np

# ---------------------------------------------------------
#  Node System — Grande Metabolic Stability Node Graph
# ---------------------------------------------------------
#  Node-strukturen:
#   Node 3 → Node 4 → Node 7
#
#  Hver node representerer:
#   - 3: Metabolsk input (NAD+, ATP, homocystein)
#   - 4: Epigenetisk respons (SIRT, gamma-friksjon)
#   - 7: Systemisk stabilitet (Aepi + friksjon)
# ---------------------------------------------------------


# -----------------------------
# Node 3 — Metabolsk input
# -----------------------------
def node3(NAD_ratio, ATP_ratio, homocysteine):
    """
    Returnerer metabolsk tilstand som tuple.
    """
    return {
        "NAD_ratio": NAD_ratio,
        "ATP_ratio": ATP_ratio,
        "homocysteine": homocysteine
    }


# -----------------------------
# Node 4 — Epigenetisk respons
# -----------------------------
def node4(SIRT_ledig_value, gamma_value):
    """
    Returnerer epigenetisk respons.
    """
    return {
        "SIRT_ledig": SIRT_ledig_value,
        "gamma": gamma_value
    }


# -----------------------------
# Node 7 — Systemisk stabilitet
# -----------------------------
def node7(Aepi_value, friction_value):
    """
    Returnerer samlet stabilitet.
    """
    return {
        "Aepi": Aepi_value,
        "friction": friction_value,
        "stability_score": Aepi_value - friction_value
    }

