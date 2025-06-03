import os
import subprocess

# Get the version to run: 'basic' or 'advanced'
version = os.getenv("VERSION", "basic").lower()

if version == "advanced":
    print("🔁 Running Advanced Product Recommender...")
    subprocess.run(["python", "advanced_version/advanced_product_recommender.py"])
elif version == "basic":
    print("▶ Running Basic Product Recommender...")
    subprocess.run(["python", "basic_version/basic_product_recommender.py"])
else:
    print("❌ Invalid VERSION value. Use 'basic' or 'advanced'.")
