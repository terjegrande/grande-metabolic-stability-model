# Grande Metabolic Stability Model — NADPH balance

def nadph_production(pentose_flux, idh_flux, malic_flux,
                     k_pentose, k_idh, k_malic):
    """
    Produksjon av NADPH fra:
    - pentosefosfatveien (G6PD/PGD)
    - isocitratdehydrogenase (IDH)
    - malic enzyme
    """
    prod_pentose = k_pentose * pentose_flux
    prod_idh = k_idh * idh_flux
    prod_malic = k_malic * malic_flux
    return prod_pentose + prod_idh + prod_malic


def nadph_consumption(ROS, RNS, BH2, NOX_activity,
                      k_antiox, k_bh4, k_nox):
    """
    Forenklet NADPH-forbruk:
    - antioksidantforsvar (GSH-system, Trx, etc.) drevet av ROS/RNS
    - BH4-resirkulering fra BH2
    - NOX-aktivitet (NADPH oxidase)
    """
    antiox_use = k_antiox * (ROS + RNS)
    bh4_use = k_bh4 * BH2
    nox_use = k_nox * NOX_activity
    return antiox_use + bh4_use + nox_use


def nadph_net_change(pentose_flux, idh_flux, malic_flux,
                     ROS, RNS, BH2, NOX_activity,
                     k_pentose, k_idh, k_malic,
                     k_antiox, k_bh4, k_nox):
    """
    Netto endring i NADPH-poolen.
    """
    prod = nadph_production(pentose_flux, idh_flux, malic_flux,
                            k_pentose, k_idh, k_malic)
    cons = nadph_consumption(ROS, RNS, BH2, NOX_activity,
                             k_antiox, k_bh4, k_nox)
    return prod - cons
