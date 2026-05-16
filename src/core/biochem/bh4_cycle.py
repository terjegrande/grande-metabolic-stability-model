# Grande Metabolic Stability Model — BH4 cycle

def bh4_synthesis(GTP, rate_GTPCH, k_syn):
    """
    Forenklet BH4-syntese fra GTP via GTPCH.
    """
    return k_syn * rate_GTPCH * GTP


def bh4_oxidation(BH4, ROS, RNS, k_ox):
    """
    Oksidasjon av BH4 til BH2 drevet av ROS/RNS.
    """
    return k_ox * BH4 * (ROS + RNS)


def bh4_recycling(BH2, NADPH, k_rec):
    """
    Resirkulering av BH2 tilbake til BH4, NADPH-avhengig.
    """
    return k_rec * BH2 * NADPH


def bh4_net_change(GTP, rate_GTPCH, BH4, BH2, ROS, RNS, NADPH,
                   k_syn, k_ox, k_rec):
    """
    Netto endring i BH4-poolen.
    """
    syn = bh4_synthesis(GTP, rate_GTPCH, k_syn)
    ox = bh4_oxidation(BH4, ROS, RNS, k_ox)
    rec = bh4_recycling(BH2, NADPH, k_rec)
    return syn - ox + rec

