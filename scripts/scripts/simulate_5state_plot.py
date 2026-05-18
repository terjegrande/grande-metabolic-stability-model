import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from src.core.model_5state import ode_system, default_params, reactions


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
        return None, None, None

    # Beregn ROS(t) fra reaksjonsfunksjonen
    ROS_t = np.zeros_like(t_eval)
    for i, ti in enumerate(t_eval):
        _, _, _, _, _, ROS = reactions(sol.y[:, i], default_params)
        ROS_t[i] = ROS

    return t_eval, sol.y, ROS_t


def plot_results(t, y, ROS_t):
    labels = ["NADPH", "GSH", "GSSG", "BH4", "BH2"]
    colors = ["blue", "green", "red", "purple", "orange"]

    plt.figure(figsize=(10, 7))

    # Plot 5 tilstander
    for i in range(5):
        plt.plot(t, y[i], label=labels[i], color=colors[i], linewidth=2)

    # Plot ROS
    plt.plot(t, ROS_t, label="ROS", color="black", linestyle="--", linewidth=2)

    plt.xlabel("Tid")
    plt.ylabel("Konsentrasjon")
    plt.title("5-tilstands redoksmodell + ROS(t)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    t, y, ROS_t = run_simulation()
    if t is not None:
        plot_results(t, y, ROS_t)
