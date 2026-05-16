# Grande Metabolic Stability Model — NO / ONOO⁻ cycle

def no_synthesis(arg, NOS_activity, k_no):
    """
    NO-produksjon fra arginin via NOS.
    """
    return k_no * NOS_activity * arg


def no_decay(NO, k_decay):
    """
    Basal nedbrytning av NO.
    """
    return k_decay * NO


def onoo_formation(NO, O2_superoxide, k_onoo):
    """
    Peroksynitritt-dannelse fra NO + superoksid.
    """
    return k_onoo * NO * O2_superoxide


def onoo_detox(ONOO, GSH, k_detox):
    """
    Detox av ONOO⁻ via GSH-avhengige mekanismer.
    """
    return k_detox * ONOO * GSH


def no_onoo_balance(arg, NOS_activity, NO, O2_superoxide, ONOO, GSH,
                    k_no, k_decay, k_onoo, k_detox):
    """
    Netto
