import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

# Load data
df = pd.read_csv("ab_test_data.csv")

# Group conversion rates
conversion_rates = df.groupby("group")["converted"].mean()
print(conversion_rates)

# Counts
conversions = df.groupby("group")["converted"].sum()
visitors = df.groupby("group")["converted"].count()

# Z-test
stat, pval = proportions_ztest(conversions, visitors)

print("Z-test statistic:", stat)
print("P-value:", pval)

if pval < 0.05:
    print("Result is statistically significant.")
else:
    print("No significant difference.")
