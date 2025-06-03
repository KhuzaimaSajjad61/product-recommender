import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
import numpy as np

# Load data
df = pd.read_csv("user_ratings.csv")

# ------------------------------
# 1. ITEM-BASED RECOMMENDATIONS
# ------------------------------
def item_based_recommender(df, user):
    pivot = df.pivot_table(index='user', columns='product', values='rating').fillna(0)
    
    if user not in pivot.index:
        print("User not found.\n")
        return

    # Compute cosine similarity between products
    similarity = cosine_similarity(pivot.T)
    similarity_df = pd.DataFrame(similarity, index=pivot.columns, columns=pivot.columns)

    user_ratings = pivot.loc[user]
    unseen = user_ratings[user_ratings == 0]

    scores = {}
    for product in unseen.index:
        sim_scores = similarity_df[product]
        total_sim = 0
        weighted_sum = 0
        for seen_product, rating in user_ratings[user_ratings > 0].items():
            sim = sim_scores[seen_product]
            weighted_sum += sim * rating
            total_sim += sim
        if total_sim != 0:
            scores[product] = weighted_sum / total_sim

    if scores:
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        print(f"\nItem-based Recommendations for {user}:\n")
        for prod, score in sorted_scores[:3]:
            print(f"→ {prod} (score: {score:.2f})")
    else:
        print("No recommendations available.")

# ------------------------------
# 2. MATRIX FACTORIZATION (SVD)
# ------------------------------
def model_based_recommender(df, user):
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[["user", "product", "rating"]], reader)
    trainset, testset = train_test_split(data, test_size=0.2)

    model = SVD()
    model.fit(trainset)

    all_products = df['product'].unique()
    user_seen = df[df['user'] == user]['product'].values if user in df['user'].values else []

    print(f"\nModel-based SVD Recommendations for {user}:\n")
    preds = []
    for prod in all_products:
        if prod not in user_seen:
            preds.append((prod, model.predict(user, prod).est))

    if not preds:
        print("No recommendations (user not found or has seen all products).")
        return

    top_preds = sorted(preds, key=lambda x: x[1], reverse=True)[:3]
    for prod, rating in top_preds:
        print(f"→ {prod} (Predicted Rating: {rating:.2f})")

# ------------------------------
# MAIN INTERFACE
# ------------------------------
print("\nWelcome to the Advanced Product Recommender\n")
print("Type a user name to get item-based and SVD recommendations. Type 'exit' to quit.\n")

while True:
    user_input = input("Enter user: ")
    if user_input.lower() == 'exit':
        break
    item_based_recommender(df, user_input)
    model_based_recommender(df, user_input)
    print("\n" + "-" * 40)
