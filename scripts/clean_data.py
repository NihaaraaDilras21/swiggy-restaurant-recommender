import pandas as pd

# Load the Dataset
df = pd.read_csv("data/swiggy.csv")

#Stage 1: Data Cleaning
# Remove rows where rating is missing or '--'
df = df[df["rating"] != "--"]
df = df.dropna(subset=["rating", "cost", "cuisine", "name"])

# Convert rating to float
df["rating"] = df["rating"].astype(float)

# Clean cost (₹200 → 200)
df["cost"] = df["cost"].str.replace("₹", "")
df["cost"] = df["cost"].str.strip()
df["cost"] = df["cost"].astype(int)

print(df[["name", "rating", "cost", "cuisine"]].head())
print(df.info())

# Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)

print("Cleaned data saved as data/cleaned_data.csv")

