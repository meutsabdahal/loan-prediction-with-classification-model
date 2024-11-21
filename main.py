import streamlit as st
import pickle as pkl
import pandas as pd
from sklearn.preprocessing import StandardScaler

with open('encoders.pkl', 'rb') as encoder_file: 
    encoders = pkl.load(encoder_file)
 
with open('random_forest.pkl', 'rb') as model_file: 
    model = pkl.load(model_file)

st.title('Loan Approval Prediction')

person_age = st.number_input('Age: ', max_value=100, value=None)
person_gender = st.selectbox('Gender: ', encoders['person_gender'].classes_)
person_education = st.selectbox('Education Qualification: ', encoders['person_education'].classes_)
person_income = st.number_input('Income: ', value=100)
person_emp_exp = st.number_input('Employment Experience: ', value=None)
person_home_ownership = st.selectbox('Home Ownership: ', encoders['person_home_ownership'].classes_)
loan_amnt = st.number_input('Loan Amount: ', value=100)
loan_intent = st.selectbox('Loan Intent: ', encoders['loan_intent'].classes_)
loan_int_rate = st.number_input('Loan Interest Rate: ', step=0.1)
cb_person_cred_hist_length = st.number_input('Credit History Length: ', value=None)
credit_score = st.number_input('Credit Score: ', value=None)
previous_loan_defaults_on_file = st.selectbox('Previous Loan Defaults: ', encoders['previous_loan_defaults_on_file'].classes_)

loan_percent_income = loan_amnt / person_income 
loan_to_income = loan_amnt / person_income 
income_to_loan = person_income / loan_amnt 
net_disposable_income = person_income - (loan_amnt * loan_int_rate / 100)


encoded_data = {
    'person_age': person_age,
    'person_gender': encoders['person_gender'].transform([person_gender])[0],
    'person_education': encoders['person_education'].transform([person_education])[0],
    'person_income': person_income,
    'person_emp_exp': person_emp_exp, 
    'person_home_ownership': encoders['person_home_ownership'].transform([person_home_ownership])[0],
    'loan_amnt': loan_amnt,
    'loan_intent': encoders['loan_intent'].transform([loan_intent])[0], 
    'loan_int_rate': loan_int_rate, 
    'loan_percent_income': loan_percent_income, 
    'cb_person_cred_hist_length': cb_person_cred_hist_length,
    'credit_score': credit_score, 
    'previous_loan_defaults_on_file': encoders['previous_loan_defaults_on_file'].transform([previous_loan_defaults_on_file])[0],    
    'loan_to_income': loan_to_income, 
    'income_to_loan': income_to_loan, 
    'net_disposable_income': net_disposable_income 
}

predict_df = pd.DataFrame([encoded_data])
scaler = ['person_age', 'person_income', 'loan_amnt', 'loan_int_rate', 'cb_person_cred_hist_length', 'credit_score', 'loan_to_income', 'income_to_loan', 'net_disposable_income']
# scaler = StandardScaler()
predict_df[scaler] = StandardScaler().fit_transform(predict_df[scaler])


if st.button('Predict!'):
    prediction = model.predict(predict_df)
    if prediction[0] == 1:
        st.success('Congratulation!! Loan Approved')
    else:
        st.error('Loan Not Approved!')
