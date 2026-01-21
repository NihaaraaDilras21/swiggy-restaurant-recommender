import pandas as pd
import pickle 
from sklearn.metrics.pairwise import cosine_similarity

#Load encoded data
data=pd.read_csv("data/encoded_data.csv")

#Load cleaned data(for names, city, cuisine)
cleaned= pd.read_csv("data/cleaned_data.csv")

#Load encoder
with open("encoder.pkl","rb") as f:
    encoder=pickle.load(f)

def recommend(city, cuisine, max_cost, min_rating, top_n=5):

    user_input = pd.DataFrame([[city, cuisine]], columns=["city", "cuisine"])
    encoded_user = encoder.transform(user_input)

    user_vector = pd.concat(
        [pd.DataFrame([[min_rating, max_cost]]), pd.DataFrame(encoded_user)],
        axis=1
    )

    similarity = cosine_similarity(user_vector, data)[0]

    cleaned["similarity"] = similarity

    results = cleaned[
    (cleaned["cost"] <= max_cost) &
    (cleaned["rating"] >= min_rating) &
    (cleaned["city"] == city) &
    (cleaned["cuisine"].str.contains(cuisine, case=False, na=False))
].sort_values("similarity", ascending=False)

    return results[["name", "city", "cuisine", "rating", "cost"]].head(top_n)

print(recommend("Indiranagar,Bangalore", "Chinese", 300, 4.0))

