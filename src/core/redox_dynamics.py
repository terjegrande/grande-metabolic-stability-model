# Grande Metabolic Stability Model — Redox Dynamics

def ros_production(mito_activity, leakage_rate):
    return mito_activity * leakage_rate


def rns_production(NO, O2, k_rns):
    return k_rns * NO * O2


def antioxidant_capacity(GSH, catalase, k_antiox):
    return k_antiox * (GSH + catalase)

