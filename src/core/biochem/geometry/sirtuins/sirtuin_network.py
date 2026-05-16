# Grande Metabolic Stability Model — Sirtuin network module

def sirtuin_activity_index(NAD, NADH, NADPH, ROS, params):
    """
    Samlet sirtuin-indeks (S-index).
    - Øker med NAD
    - Hemmes av NADH (redox trap)
    - Hemmes av ROS
    - Støttes av NADPH
    """
    nad_ratio = NAD / (NAD + NADH + 1e-9)

    base = params["k_nad"] * nad_ratio
    redox_penalty = params["k_nadh"] * (NADH / (NAD + 1e-9))
    ros_penalty = params["k_ros"] * ROS
    nadph_support = params["k_nadph"] * NADPH

    S = base + nadph_support - redox_penalty - ros_penalty

    # Normaliser til [0, 1]
    return max(0.0, min(1.0, S))
