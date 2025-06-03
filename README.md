
# ✅ Product Recommendation System (Basic + Advanced)

What it is:

A two-level recommendation system for an online store.

Basic version uses cosine similarity

Advanced version uses collaborative filtering (SVD)

## Skills shown:

Recommendation logic

Item-based filtering

Collaborative filtering

Data preprocessing

## Tools used:

Python

Pandas

Scikit-learn

Surprise

## 🗂 Folder Structure
product-recommender-system/
├── basic_version/
│   └── basic_recommender.py
├── advanced_version/
│   └── advanced_product_recommender.py
├── user_ratings.csv
├── requirements.txt
└── README.md


## 🧠 Version Summary
Version	Method	Main Libs
Basic	Cosine similarity	pandas, sklearn
Advanced	SVD (Collaborative)	pandas, surprise

## ⚙️ How to Run

```bash
pip install -r requirements.txt
If you face issues with surprise, run:
pip install numpy==1.26.4
python basic_version/basic_recommender.py
python advanced_version/advanced_product_recommender.py


