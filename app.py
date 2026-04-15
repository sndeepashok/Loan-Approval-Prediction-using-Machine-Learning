import pandas as pd
import streamlit as st
import pickle as pk

model=pk.load(open(r"C:\Users\deepa\OneDrive\Desktop\Loan\model.pkl"))
scaler=pk.load(open(r"C:\Users\deepa\OneDrive\Desktop\Loan\scaler.pkl"))

st.header('Loan Prediction App')

no_of_dept = st.slider("Choose no of dependents", 0, 5)
education = st.selectbox("Choose Education", ['Graduated', 'Not Graduated'])
self_emp = st.selectbox("Choose Self employed", ["Yes", "No"])
Annual_income = st.slider("Choose Annual Income", 0, 10000000)
Loan_amount = st.slider("Choose Loan Amount", 0, 10000000)
Loan_Duration = st.slider("Choose Loan Duration", 0, 20)
Cibil_Score = st.slider("Choose Cibil score", 0, 1000)
Assets = st.slider("Choose Assets", 0, 100000000)

if education == 'Graduated':
    grad_s = 1
else:
    grad_s = 0

if self_emp == "Yes":
    emp_s = 1
else:
    emp_s = 0

if st.button("Predict"):
    pred_data= pd.DataFrame([[no_of_dept,grad_s,emp_s,Annual_income,Loan_amount,Loan_Duration,Cibil_Score,Assets]],
                        columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','Assets'])
    
    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.markdown('Loan Is Aprroved')
    else:
        st.markdown('Loan Is Rejected')    

    