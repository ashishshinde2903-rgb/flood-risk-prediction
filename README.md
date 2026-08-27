# 🌊 Flood Risk Prediction & Analytics

## 📌 Project Overview

This project focuses on predicting flood-risk levels using machine learning
and analyzing historical flood events in India.

The project includes data preprocessing, exploratory data analysis (EDA),
multiple machine learning classification models, and an interactive
Streamlit application.

---

## 🎯 Objectives

- Analyze historical flood-event data
- Perform exploratory data analysis and visualization
- Prepare environmental and geographical features for machine learning
- Compare multiple classification algorithms
- Build a flood-risk prediction model
- Develop an interactive Streamlit application

---

## 📊 Dataset

The machine learning dataset contains environmental and geographical
features related to flood risk.

Key features include:

- Rainfall
- River Water Level
- Reservoir Level
- Soil Moisture
- Temperature
- Humidity
- Elevation
- Slope
- Land Use
- Flood History
- Drainage Quality

The target variable is:

**Flood Risk:** Low, Medium, High, Extreme

A separate historical flood-event dataset is used for exploratory analysis
and visualization.

---

## 🔍 Exploratory Data Analysis

The historical flood dataset was analyzed to identify:

- Flood events by year
- Flood events by month
- Flood events by state
- People affected by floods
- Flood-related deaths
- Houses damaged
- Crop loss
- Flood types
- Major flood causes
- Relationship between rainfall and flood impact

---

## 🤖 Machine Learning

The following classification algorithms were evaluated:

- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- XGBoost

### Data Preprocessing

- Train-test split
- One-Hot Encoding for categorical features
- StandardScaler for numerical features
- Label Encoding for the target variable

---

## 📈 Model Performance

XGBoost achieved approximately **92.7% test accuracy** and was selected
as the final model.

Model evaluation included:

- Accuracy
- Precision
- Recall
- F1-score
- Cross-validation

---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit application that allows
users to:

- Enter environmental conditions
- Predict flood-risk level
- Explore historical flood data
- Apply filters
- Analyze flood trends and impacts

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Streamlit

---

## 📁 Project Structure

```text
flood-risk-prediction/
│
├── app.py
├── app2.py
├── Flood_Detection.ipynb
├── Historical_flood.ipynb
├── XGBoost.py
├── flood_risk_ml_dataset.csv
├── india_flood_curated_2000_2026.csv
├── model.pkl
├── requirements.txt
└── README.md

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/ashishshinde2903-rgb/flood-risk-prediction.git

cd flood-risk-prediction

pip install -r requirements.txt

streamlit run app.py
