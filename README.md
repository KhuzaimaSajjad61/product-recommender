# Basic Product Recommendation System

This is a basic AI-based recommender system that suggests products to users based on similarity with other users, using collaborative filtering.

## 🧰 Tools Used
- Python
- Pandas
- Scikit-learn
- Cosine Similarity

## 🧠 What It Does
- Builds a user-product matrix from rating data
- Calculates user similarity using cosine similarity
- Recommends products that similar users have liked but the current user hasn't rated yet

## 📁 Dataset
Dummy dataset of 5 users and their ratings on products like:
- Laptop
- Monitor
- Mouse
- Keyboard

## 🚀 How to Run

```bash
pip install -r requirements.txt
python product_recommender.py
