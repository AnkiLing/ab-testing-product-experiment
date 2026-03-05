import pandas as pd
import numpy as np

np.random.seed(42)

n = 5000

groups = np.random.choice(["control", "treatment"], size=n)

conversion_rates = {
    "control": 0.12,
    "treatment": 0.14
}

converted = [
    np.random.binomial(1, conversion_rates[group])
    for group in groups
]

df = pd.DataFrame({
    "user_id": range(1, n + 1),
    "group": groups,
    "converted": converted
})

df.to_csv("ab_test_data.csv", index=False)

print("Dataset created: ab_test_data.csv")

python generate_dataset.py
