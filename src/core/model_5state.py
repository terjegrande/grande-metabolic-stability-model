import numpy as np

def reactions(x, p):
    """
    Beregner reaksjonshastigheter v1–v5 og ROS.
    x = [NADPH, GSH, GSSG, BH4, BH2]
    p = parameterdict
    """

    NADPH, GSH, GSSG, BH4, BH2 = x

    # Parametre
    k_PPP = p["k_PPP"]
    k1 = p["k1"]
    k2 = p["k2"]
    k3 = p["k3"]
    k4 = p["k4"]
    k5 = p["k5"]

    # ROS (algebraisk steady-state)
    ROS = k3 / (k4 * GSH + k5 * BH4 + 1e-12)

    # Reaksjoner
    v1 = k1 * NADPH * GSSG          # GSSG → GSH
    v2 = k2 * NADPH * BH2           # BH2 → BH4
    v3 = k3                         # ROS-produksjon
    v4 = k4 * ROS * GSH             # ROS-detoks via GSH
    v5 = k5 * ROS * BH4             # ROS-detoks via BH4

    return np.array([v1, v2, v3, v4, v5, ROS])


def ode_system(t, x, p):
    """
    5-tilstands ODE-system:
    x = [NADPH, GSH, GSSG, BH4, BH2]
    """

    v1, v2, v3, v4, v5, ROS = reactions(x, p)

    dNADPH = p["k_PPP"] - v1 - v2
    dGSH   = 2 * v1 - v4
    dGSSG  = v4 - v1
    dBH4   = v2 - v5
    dBH2   = v5 - v2

    return np.array([dNADPH, dGSH, dGSSG, dBH4, dBH2])
