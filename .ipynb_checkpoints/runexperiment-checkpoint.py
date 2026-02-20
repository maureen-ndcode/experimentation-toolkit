from ABSimulator.ab_test import run_ab_test

results = run_ab_test(
    n_control=5000,
    n_treatment=5000,
    p_control=0.10,
    p_treatment=0.12
)

print(results)