# Grande Metabolic Stability Model — Cristae topology module

def topology_state(CL_fraction, CL_threshold):
    """
    Returnerer cristae-topologi basert på cardiolipin-nivå.
    - Tubular (høy CL)
    - Lamellar (lav CL)
    """
    if CL_fraction >= CL_threshold:
        return "tubular"
    return "lamellar"


def topology_efficiency(topology, eff_tubular, eff_lamellar):
    """
    ATP- og NADH-effektivitet basert på topologi.
    Tubular = høy effektivitet
    Lamellar = lav effektivitet
    """
    if topology == "tubular":
        return eff_tubular
    return eff_lamellar
