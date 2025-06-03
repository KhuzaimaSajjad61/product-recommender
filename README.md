# Product Recommendation System
Product Recommendation System is an intelligent AI-based application designed to provide personalized product suggestions based on user behavior, preferences, and past interactions. Powered by machine learning models, this system delivers accurate, real-time recommendations to enhance the user shopping experience.

## 🔍 Features
Personalized Recommendations: Uses user ratings, preferences, and historical interactions to suggest relevant products.

Dual Recommendation Engines:

Content-Based Filtering: Recommends similar products based on features like category, price, and brand.

Collaborative Filtering: Suggests products using matrix factorization (SVD) based on what similar users liked.

## 🗂️ Project Structure
```plaintext
product-recommender-system/
├── basic_version/
│   └── basic_recommender.py
├── advanced_version/
│   └── advanced_product_recommender.py
├── user_ratings.csv
├── Dockerfile
├── .dockerignore
├── run.py
├── requirements.txt
└── README.md
```

## ⚙️ Requirements
Python 3.11 or higher<br>
Pandas, Scikit-learn, Surprise, numpy

## Install all dependencies via:

```bash
pip install -r requirements.txt
```
## 🖥️ Installation & Running
### 🔧 Local Setup

1. Clone the repository:
```bash
https://github.com/KhuzaimaSajjad61/product-recommender.git
cd product-recommendation-system
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Build the Docker image:

```bash
docker build -t product-recommendor .
```
4. Run the Docker container:
if you want to run the basic version:

```bash
docker run -it --rm product-recommendor
```
if you want to run the advanced version:

```bash
docker run -it --rm -e VERSION=advanced product-recommender
```

## 📊 How It Works
The Product Recommendation System leverages two core machine learning approaches:

### 🧠 Content-Based Filtering 
• Analyzes product features like name, category, price, and description.<br>  
• Computes cosine similarity between products.<br>
• Suggests similar items to what the user views or selects.<br>  

### 🤝 Collaborative Filtering (SVD)
• Uses user-item interactions (ratings matrix).<br> 
• Applies matrix factorization to uncover latent user preferences.<br>  
• Recommends products based on the behavior of similar users.<br> 


## 🛠️ Technologies Used
Technology	Purpose<br>
Python:	Core backend and ML processing<br>
Scikit-learn: For content-based filtering and preprocessing<br>
Surprise: Collaborative filtering via SVD<br>
Docker: Containerized deployment<br>



## 📜 License
This project is licensed under the Apache License 2.0.
See the LICENSE file for details.

## 🤝 Contributing
We welcome contributions to improve the recommendation system!<br>
If you have suggestions, bug reports, or want to submit a feature, feel free to:<br>

• Open an issue<br>
• Submit a pull request

