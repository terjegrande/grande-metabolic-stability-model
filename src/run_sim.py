from core.load_components import build_model
from core.ode_solver import rk4_step
from core.plot_results import plot_time_series


def run_sim():
    model = build_model()
    params = model["params"]
    step_fn = model["step_fn"]

    # Initial state
    state = {
        "NAD": 300.0,
        "NADH": 100.0,
        "NADPH": 80.0,
        "ROS": 10.0,
        "RNS": 5.0,
        "BH4": 50.0,
        "BH2": 10.0,
        "NO": 5.0,
        "ONOO": 2.0,
        "friction": 1.0,
        "SAM": 1.0,
        "H": 12.0,
        "CL_fraction": 0.4,
        "pentose_flux": 1.0,
        "idh_flux": 1.0,
        "malic_flux": 1.0,
        "NOX_activity": 1.0,
    }

    # Simulation parameters
    T = 100.0
    dt = 0.1
    steps = int(T / dt)

    t = []
    S_series = []
    zeta_series = []
    nadph_series = []
    bh4_series = []

    for i in range(steps):
        derivs = step_fn(state, params)
        S_index = derivs.get("S_index", 0.0)

        t.append(i * dt)
        S_series.append(S_index)
        zeta_series.append(state["friction"])
        nadph_series.append(state["NADPH"])
        bh4_series.append(state["BH4"])

        state = rk4_step(state, params, step_fn, dt)

    plot_time_series(
        t,
        {
            "S-index": S_series,
            "ζ (friction)": zeta_series,
            "NADPH": nadph_series,
            "BH4": bh4_series,
        },
    )


if __name__ == "__main__":
    run_sim()
