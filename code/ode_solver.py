from scipy.integrate import solve_ivp

def dS_dt(t, S, friction_func, params):
    """
    ODE for metabolsk stabilitet S(t).
    S : float
        Metabolsk stabilitet (0–1)
    friction_func : function
        Funksjon som beregner friksjon ζ(t)
    params : dict
        Parametre som sendes videre til friksjonsfunksjonen
    """
    zeta = friction_func(S, **params)
    return -zeta


def solve_stability(S0=1.0, t_span=(0, 72), friction_func=None, params=None):
    """
    Løser S(t) gitt en friksjonsfunksjon.
    S0 : float
        Startverdi for S
    t_span : tuple
        (t_start, t_slutt)
    friction_func : function
        Funksjon som beregner friksjon
    params : dict
        Parametre til friksjonsfunksjonen
    """
    if friction_func is None:
        raise ValueError("Du må sende inn en friksjonsfunksjon.")

    if params is None:
        params = {}

    sol = solve_ivp(
        fun=lambda t, S: dS_dt(t, S, friction_func, params),
        t_span=t_span,
        y0=[S0],
        dense_output=True
    )

    return sol

