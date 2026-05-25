from ode_solver import solve_stability
from frictionengine import calculate_friction


def scenario_fasting(hours=72):
    """
    Simulerer et enkelt faste-scenario.
    """
    sol = solve_stability(
        S0=1.0,
        t_span=(0, hours),
        friction_func=calculate_friction,
        params={"k": 0.015}
    )
    return sol


def scenario_refeed(hours=24):
    """
    Simulerer et refeed-scenario med lav friksjon.
    """
    sol = solve_stability(
        S0=0.6,
        t_span=(0, hours),
        friction_func=calculate_friction,
        params={"k": 0.005}
    )
    return sol


def scenario_stress(hours=48):
    """
    Simulerer et stress-scenario med høy friksjon.
    """
    sol = solve_stability(
        S0=0.8,
        t_span=(0, hours),
        friction_func=calculate_friction,
        params={"k": 0.03}
    )
    return sol
