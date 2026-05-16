
# Grande Metabolic Stability Model — Load Components

def mitochondrial_load(ATP_demand, proton_leak, k_mito):
    return k_mito * (ATP_demand + proton_leak)


def ribosomal_load(protein_synthesis_rate, k_ribo):
    return k_ribo * protein_synthesis_rate


def membrane_load(curvature_stress, lipid_damage, k_mem):
    return k_mem * (curvature_stress + lipid_damage)


def redox_load(ROS, RNS, k_redox):
    return k_redox * (ROS + RNS)
