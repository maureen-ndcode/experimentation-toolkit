from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
def calculate_sample_size(p_control,p_treatment,power=0.8,alpha=0.05):
    effect_size=proportion_effectsize(p_control,p_treatment)
    analysis=NormalIndPower()
    sample_size=analysis.solve_power(effect_size=effect_size,power=power,alpha=alpha,ratio=1)
    return int(sample_size)