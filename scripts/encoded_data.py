import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import pickle

# Load cleaned data
df = pd.read_csv("data/cleaned_data.csv")

# Select columns to encode
cat_cols = ["city", "cuisine"]

encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

encoded = encoder.fit_transform(df[cat_cols])

encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(cat_cols))

# Combine with numerical features
final_df = pd.concat([df[["rating", "cost"]].reset_index(drop=True), encoded_df], axis=1)

# Save encoded data
final_df.to_csv("data/encoded_data.csv", index=False)

# Save encoder
with open("encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("Encoding complete. Files saved.")
