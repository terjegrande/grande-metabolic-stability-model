def calculate_friction(S, k=0.015):
    """
    Enkel friksjonsfunksjon.
    S : float
        Metabolsk stabilitet (0–1)
    k : float
        Friksjonskoeffisient
    """
    return k * (1 - S)
