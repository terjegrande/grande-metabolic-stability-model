import numpy as np
from scipy.integrate import solve_ivp

from src.core.model_5state import ode_system, default_params


def run_simulation():
    # Initialtilstander: [NADPH, GSH, GSSG, BH4, BH2]
    x0 = np.array([5.0, 8.0, 1.0, 3.0, 1.0])

    # Tidsrom
    tspan = (0.0, 200.0)
    t_eval = np.linspace(tspan[0], tspan[1], 1000)

    sol = solve_ivp(
        fun=lambda t, x: ode_system(t, x, default_params),
        t_span=tspan,
        y0=x0,
        t_eval=t_eval,
        max_step=0.5,
    )

    if not sol.success:
        print("Simulering feilet:", sol.message)
        return

    print("\n=== Resultat ved slutt-tid t = {:.1f} ===".format(tspan[1]))
    print("NADPH =", sol.y[0, -1])
    print("GSH   =", sol.y[1, -1])
    print("GSSG  =", sol.y[2, -1])
    print("BH4   =", sol.y[3, -1])
    print("BH2   =", sol.y[4, -1])


if __name__ == "__main__":
    run_simulation()
