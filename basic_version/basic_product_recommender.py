import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_csv("user_ratings.csv")

# Create user-product matrix
ratings_matrix = df.pivot_table(index="user", columns="product", values="rating").fillna(0)

# Compute cosine similarity between users
similarity = cosine_similarity(ratings_matrix)
similarity_df = pd.DataFrame(similarity, index=ratings_matrix.index, columns=ratings_matrix.index)

# Recommendation function
def get_recommendations(target_user):
    if target_user not in ratings_matrix.index:
        print("User not found.")
        return

    similar_users = similarity_df[target_user].sort_values(ascending=False)[1:]
    most_similar_user = similar_users.idxmax()

    print(f"\nMost similar user to {target_user}: {most_similar_user}")

    target_ratings = ratings_matrix.loc[target_user]
    similar_user_ratings = ratings_matrix.loc[most_similar_user]

    recommendations = similar_user_ratings[(target_ratings == 0) & (similar_user_ratings > 0)].sort_values(ascending=False)

    if recommendations.empty:
        print("No new product recommendations.")
    else:
        print("Recommended products:")
        for product in recommendations.index:
            print(f"→ {product} (Rating: {recommendations[product]})")

# CLI
print("Product Recommender — Type a user name (e.g., Alice, Bob). Type 'exit' to quit.\n")
while True:
    user_input = input("Enter user: ")
    if user_input.lower() == "exit":
        break
    get_recommendations(user_input)
