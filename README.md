📊 Loan Approval Prediction using Machine Learning

This project builds a Loan Approval Prediction System using Logistic Regression. It preprocesses applicant data, engineers features, and trains a model to predict whether a loan application will be approved or rejected.

🚀 Project Overview

The goal of this project is to:

Clean and preprocess raw loan data
Perform feature engineering
Train a machine learning model
Predict loan approval status
📁 Dataset

The dataset used is:

loan_approval_dataset.csv
Features include:
Education
Self-employed status
Income details
Asset values (residential, commercial, luxury, bank)
Loan status (target variable)
🧹 Data Preprocessing

Steps performed:

Removed unnecessary columns (loan_id)
Trimmed column names and string values
Handled categorical data:
education: Graduate → 1, Not Graduate → 0
self_employed: Yes → 1, No → 0
loan_status: Approved → 0, Rejected → 1
Created a new feature:
Assets = sum of all asset values
Dropped redundant asset columns
Checked for missing values
🧠 Model Building
Split data into training and testing sets (80/20)
Applied feature scaling using StandardScaler
Trained model using Logistic Regression
📈 Model Performance
Evaluated using .score() on test data
Outputs prediction accuracy
💾 Model Saving

The trained model and scaler are saved using pickle:

model.pkl → Trained Logistic Regression model
scaler.pkl → StandardScaler object
🔮 Making Predictions

Example:

import pickle as pk

model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))

# Example input
pred_data = scaler.transform([[...]])

prediction = model.predict(pred_data)
print(prediction)
🛠️ Technologies Used
Python 🐍
Pandas
NumPy
Scikit-learn
Pickle
