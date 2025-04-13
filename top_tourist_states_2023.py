import pandas as pd
import matplotlib.pyplot as plt

data = {
    "State": [
        "Uttar Pradesh", "Tamil Nadu", "Karnataka", "Andhra Pradesh",
        "Rajasthan", "Gujarat", "Maharashtra", "West Bengal",
        "Madhya Pradesh", "Bihar"
    ],
    "Domestic Tourists (Millions)": [478.53, 286.01, 284.12, 254.71, 179.05, 178.07, 161.36, 145.67, 111.95, 81.59],
    "Foreign Tourists (Millions)": [4.68, 6.32, 3.45, 2.76, 2.95, 1.87, 5.14, 1.65, 1.32, 0.98]
}

df = pd.DataFrame(data)
df["Total Tourists (Millions)"] = df["Domestic Tourists (Millions)"] + df["Foreign Tourists (Millions)"]
df = df.sort_values(by="Total Tourists (Millions)", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(df["State"], df["Total Tourists (Millions)"], color="skyblue", edgecolor="black")
plt.title("Top Tourist States in India (2023)")
plt.xlabel("State")
plt.ylabel("Total Tourists (Millions)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()