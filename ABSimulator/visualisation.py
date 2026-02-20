import matplotlib.pyplot as plt
def plot_conversion(control_rate,treatment_rate,control_CI,treatment_CI):
    labels=['Control','Treatment']
    rates=[control_rate,treatment_rate]
    control_error=[control_rate-control_CI[0],control_CI[1]-control_rate]
    treatment_error=[treatment_rate-treatment_CI[0],treatment_CI[1]-treatment_rate]
    errors=[[control_error[0],treatment_error[0]],[control_error[1],treatment_error[1]]]
    plt.figure()
    plt.bar(labels,rates)
    plt.errorbar(labels,rates,yerr=errors,fmt='o')
    plt.ylabel("Conversion Rate")
    plt.title("A/B Test Conversion Comparision")
    plt.show()