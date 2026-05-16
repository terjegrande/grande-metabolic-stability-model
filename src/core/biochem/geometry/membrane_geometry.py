# Grande Metabolic Stability Model — Membrane and compartment geometry

import math


def sphere_surface_area(radius):
    """
    Overflateareal av en sfære.
    A = 4πr^2
    """
    return 4.0 * math.pi * radius**2


def sphere_volume(radius):
    """
    Volum av en sfære.
    V = 4/3 πr^3
    """
    return (4.0 / 3.0) * math.pi * radius**3


def surface_to_volume_ratio(radius):
    """
    Overflate/volum-forhold for en sfære.
    S/V = 3/r
    """
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    return 3.0 / radius


def effective_diffusion_length(radius, shell_thickness):
    """
    Effektiv diffusjonslengde i et sfærisk skall.
    Brukes som enkel proxy for transportmotstand.
    """
    if shell_thickness <= 0:
        raise ValueError("Shell thickness must be positive.")
    if shell_thickness > radius:
        raise ValueError("Shell thickness cannot exceed radius.")
    inner_r = radius - shell_thickness
    return radius - inner_r


def compartment_exchange_factor(radius, shell_thickness, k_base):
    """
    Skalerer en basis-utvekslingskonstant (k_base) med geometri:
    høyere S/V gir høyere effektiv utveksling.
    """
    sv = surface_to_volume_ratio(radius)
    dl = effective_diffusion_length(radius, shell_thickness)
    return k_base * sv / dl
