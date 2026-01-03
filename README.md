# 🛒 Market Basket Analysis & Recommendation System

An end-to-end **Market Basket Analysis** project that uncovers hidden purchasing patterns from retail transaction data using the **Apriori algorithm**.  
The project is extended into an **interactive Streamlit web application** that allows users to explore association rules and product relationships dynamically.

---

## 📌 Project Overview

Market Basket Analysis is a key data mining technique used in retail and e-commerce to understand customer purchasing behavior.  
This project analyzes customer-level grocery transactions to identify:

- Frequently purchased item combinations  
- Strong association rules between products  
- Cross-selling opportunities based on historical data  

The final solution is deployed as a **Streamlit dashboard**, making the insights easy to explore and interpret.

---

## 🎯 Key Features

- ✔ Data preprocessing and cleaning of retail transaction data  
- ✔ Identification of **frequent itemsets** using the Apriori algorithm  
- ✔ Generation of **association rules** evaluated using:
  - Support  
  - Confidence  
  - Lift  
- ✔ Time-based sales analysis to study purchasing trends  
- ✔ Interactive **Streamlit web application** for visualization  
- ✔ Rule-based **product recommendation system**  

---

## 🧠 Algorithm Used

### Apriori Algorithm
The Apriori algorithm works on the principle that:
> *If an itemset is frequent, all of its subsets must also be frequent.*

It iteratively:
1. Generates candidate itemsets  
2. Filters them using minimum support  
3. Creates association rules using confidence and lift  

This makes it highly effective for market basket and retail analytics.

---

## 📊 Tech Stack

- **Programming Language:** Python  
- **Web Framework:** Streamlit  
- **Libraries:**  
  - Pandas  
  - NumPy  
  - Matplotlib  
  - Seaborn  
  - apyori (Apriori algorithm)  

---

## 🚀 Live Application

🔗 **Streamlit App:**  
👉 https://your-app-name.streamlit.app  

*(Replace with your actual deployed Streamlit link)*

---

## 💻 Project Repository

🔗 **GitHub Repository:**  
👉 https://github.com/aashwathyadav05-svg/Market-Basket-Analysis  

---

## 🗂 Dataset Information

- Public grocery transaction dataset  
- Contains customer-level purchase history  
- Includes item descriptions and transaction dates  
- Suitable for association rule mining and retail analytics  

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/aashwathyadav05-svg/Market-Basket-Analysis.git
cd Market-Basket-Analysis
