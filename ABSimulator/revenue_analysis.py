def revenue_impact(n_control,n_treatment,control_rate,treatment_rate,avg_order_value,profit_margin):
    control_conversions=n_control*control_rate
    treatment_conversions=n_treatment*treatment_rate
    control_revenue=control_conversions*avg_order_value
    treatment_revenue=treatment_conversions* avg_order_value
    control_profit=control_revenue*profit_margin
    treatment_profit=treatment_revenue*profit_margin
    revenue_lift=treatment_revenue-control_revenue
    profit_lift=treatment_profit-control_profit
    return {
    "control_revenue":control_revenue,
        "treatment_revenue":treatment_revenue,
        "revenue_lift":revenue_lift,
        "control_profit":control_profit,
        "treatment_profit":treatment_profit,
        "profit_lift":profit_lift}
    
    