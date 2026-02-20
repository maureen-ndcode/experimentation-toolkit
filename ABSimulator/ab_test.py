import numpy as np
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.proportion import proportion_confint

def run_ab_test(n_control, n_treatment, p_control, p_treatment, alpha=0.05):
    control = np.random.binomial(1, p_control, n_control)
    treatment = np.random.binomial(1, p_treatment, n_treatment)
    successes = [control.sum(), treatment.sum()]
    observations = [n_control, n_treatment]
    z_stat, p_value = proportions_ztest(successes, observations)
    control_rate = control.mean()
    treatment_rate = treatment.mean()
    absolute_lift = treatment_rate - control_rate
    relative_lift = (absolute_lift / control_rate) * 100
    ci_control = proportion_confint(successes[0], n_control, alpha=alpha, method='normal')
    ci_treatment = proportion_confint(successes[1], n_treatment, alpha=alpha, method='normal')
    decision = "Significant" if p_value < alpha else "Not Significant"

    return {
        "control_rate": control_rate,
        "treatment_rate": treatment_rate,
        "absolute_lift": absolute_lift,
        "relative_lift_%": relative_lift,
        "p_value": p_value,
        "z_stat": z_stat,
        "decision": decision,
        "control_CI": ci_control,
        "treatment_CI": ci_treatment
    }