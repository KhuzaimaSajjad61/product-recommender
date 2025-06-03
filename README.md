# 🛒 Product Recommendation System (Basic + Advanced Versions)

This repository contains two progressively developed versions of a product recommendation system — from a simple cosine similarity-based model to a more advanced model using matrix factorization (SVD). These tools simulate how modern e-commerce platforms personalize product suggestions to boost user engagement and sales.

---

## 📁 Project Structure

```plaintext
product-recommender-system/
├── basic_version/
│   └── basic_recommender.py         # Simple item-based recommender
├── advanced_version/
│   └── advanced_product_recommender.py  # Item-based + SVD recommender
├── user_ratings.csv                 # Sample user-product rating data
├── requirements.txt                 # Python dependencies
└── README.md                       

Install Dependencies And Run:

```bash
pip install -r requirements.txt
python basic_version/basic_recommender.py
python advanced_version/advanced_product_recommender.py