# 🍽️ Swiggy Restaurant Recommendation System

This project is a simple **Restaurant Recommendation System** built using **Python, Machine Learning (Cosine Similarity), and Streamlit**.  
It recommends restaurants based on **user preferences** such as city, cuisine, budget, and minimum rating.

The project demonstrates the complete workflow of a data science application:
- Data cleaning
- Data preprocessing
- Feature encoding
- Similarity-based recommendation
- Interactive web application

---

## 📌 Project Overview

Users can:
- Select a **city**
- Choose a **cuisine**
- Set a **maximum budget**
- Set a **minimum rating**

Based on these inputs, the system recommends the **top matching restaurants** using **Cosine Similarity**.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** – Data handling and preprocessing
- **Scikit-learn** – One-Hot Encoding & Cosine Similarity
- **Streamlit** – Web application interface
- **Git & GitHub** – Version control

---

## 📂 Project Structure

swiggy-restaurant-recommender/
│
├── app.py # Streamlit application
├── encoder.pkl # Saved One-Hot Encoder
├── scripts/
│ ├── clean_data.py # Data cleaning script
│ ├── encoded_data.py # Data encoding script
│ └── recommend.py # Recommendation logic
│
├── data/
│ ├── swiggy.csv # Raw dataset (ignored in GitHub)
│ ├── cleaned_data.csv # Cleaned dataset (generated)
│ └── encoded_data.csv # Encoded dataset (generated)
│
├── .gitignore
└── README.md


---

## 🧹 Data Cleaning

The raw dataset contains missing values, symbols, and text-based numbers.

Cleaning steps:
- Removed rows with missing or invalid ratings
- Converted ratings to numeric format
- Cleaned cost values (₹ symbol removed)
- Removed rows with missing essential data

Cleaned data is saved as:

data/cleaned_data.csv


---

## 🔢 Data Encoding

Categorical features:
- `city`
- `cuisine`

These are converted into numerical form using **One-Hot Encoding**.

The trained encoder is saved as:

encoder.pkl

The encoded dataset is saved as:

data/encoded_data.csv


---

## 🧠 Recommendation Logic

The system uses **Cosine Similarity** to measure how similar a user’s preferences are to available restaurants.

Steps:
1. User inputs are encoded using the saved encoder
2. Cosine similarity is calculated between user input and restaurant data
3. Restaurants are filtered based on:
   - Budget
   - Rating
   - City
   - Cuisine
4. Top matching restaurants are returned

---

## 🖥️ Running the Application

### 1️⃣ Install required libraries
```bash
pip install pandas scikit-learn streamlit

2️⃣ Run the Streamlit app

streamlit run app.py

The application will open in your browser at:

http://localhost:8501

🚀 Features

Interactive UI using Streamlit

Real-time restaurant recommendations

Simple and explainable ML approach

Beginner-friendly project structure

📊 Future Improvements

Add location-based distance filtering

Include restaurant popularity weighting

Deploy the app online (Streamlit Cloud)

Improve UI styling

👩‍💻 Author

Nihaaraa Dilras