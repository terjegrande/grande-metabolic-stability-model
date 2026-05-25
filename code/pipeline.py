from simulation_scenarios import (
    scenario_fasting,
    scenario_refeed,
    scenario_stress
)


def run():
    print("Kjører faste-scenario (72 timer)...")
    sol = scenario_fasting(hours=72)

    # Hent noen punkter fra løsningen
    t_eval = [0, 12, 24, 48, 72]
    values = [sol.sol(t)[0] for t in t_eval]

    print("\nResultater:")
    for t, v in zip(t_eval, values):
        print(f"t = {t:>3} timer → S = {v:.4f}")


if __name__ == "__main__":
    run()
