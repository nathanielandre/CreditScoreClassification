# Libraries
import pandas as pd
import numpy as np

import streamlit as st

import pickle

# load model

with open ('model_xgbc_grid.pkl', 'rb') as file:
    model = pickle.load(file)

def run():
    # set title
    st.title('Credit Score Classification Predictor')
    st.write('---')

    # set banner
    st.image('https://img.theepochtimes.com/assets/uploads/2022/09/01/credit-score-shutterstock_1694647429.jpg',
            caption='img.theepochtimes.com')

    # deskripsi
    st.write('Predict Your Credit Score Classification Now')

    # buat form
    with st.form(key='form_parameters'):
    # Text inputs for basic information
        id = st.text_input('ID:')
        customer_id = st.text_input('Customer ID:')
        month = st.selectbox('Month:', ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))
        name = st.text_input('Name:')
        age = st.number_input('Age:', min_value=0, max_value=100, value=30)
        ssn = st.text_input('SSN (Social Security Number):')
        occupation = st.text_input('Occupation:')
        
        # Financial information
        annual_income = st.number_input('Annual Income:', min_value=0.0, value=25000.0)
        monthly_salary = st.number_input('Monthly Inhand Salary:', min_value=0.0, value=2000.0)
        num_bank_accounts = st.number_input('Number of Bank Accounts:', min_value=0, max_value=20, value=3)
        num_credit_cards = st.number_input('Number of Credit Cards:', min_value=0, max_value=20, value=2)
        
        # Loan and credit information
        num_of_loans = st.number_input('Number of Loans:', min_value=0, max_value=20, value=1)
        type_of_loans = st.text_input('Type of Loans (e.g., Personal Loan, Payday Loan):')
        delay_from_due_date = st.number_input('Delay from Due Date (in days):', min_value=0, value=0)
        num_delayed_payments = st.number_input('Number of Delayed Payments:', min_value=0, value=0)
        
        # Credit and payment details
        interest_rate = st.slider('Interest Rate (%):', min_value=0, max_value=40, value=12)
        change_credit_limit = st.number_input('Change Credit Limit:', min_value=0.0, max_value=100.0, value=30.0)
        num_credit_inquiries = st.number_input('Num Credit Inquiries:', min_value=0.0, max_value=100.0, value=30.0)
        credit_mix = st.selectbox('Credit Mix', ('Standard', 'Good', 'Bad'))
        outstanding_debt = st.number_input('Outstanding Debt:', min_value=0.0, max_value=10000.0, value=30.0)
        credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%):', min_value=0.0, max_value=100.0, value=30.0)
        credit_history_age = st.number_input('Credit History Age (in months):', min_value=0, max_value=500, value=100)
        total_emi_per_month = st.number_input('Total EMI per Month:', min_value=0.0, value=500.0)
        amount_invested_monthly = st.number_input('Amount Invested Monthly:', min_value=0.0, value=500.0)
        monthly_balance = st.number_input('Monthly Balance:', min_value=0.0, value=1500.0)
        
        # Payment behavior
        payment_of_min_amount = st.selectbox('Payment of Minimum Amount?', ('Yes', 'No'))
        payment_behavior = st.selectbox('Payment Behavior',('Low_spent_Small_value_payments', 'Low_spent_Medium_value_payments', 'Low_spent_Large_value_payments','High_spent_Small_value_payments', 'High_spent_Medium_value_payments', 'High_spent_Large_value_payments'))
        
        # Submit button
        submit_button = st.form_submit_button('Submit')

# After submission
    if submit_button:
        data_raw = {
            'ID': id,
            'Customer_ID': customer_id,
            'Month': month,
            'Name': name,
            'Age': age,
            'SSN': ssn,
            'Occupation': occupation,
            'Annual_Income': annual_income,
            'Monthly_Inhand_Salary': monthly_salary,
            'Num_Bank_Accounts': num_bank_accounts,
            'Num_Credit_Card': num_credit_cards,
            'Num_of_Loan': num_of_loans,
            'Type_of_Loan': type_of_loans,
            'Delay_from_due_date': delay_from_due_date,
            'Num_of_Delayed_Payment': num_delayed_payments,
            'Changed_Credit_Limit': change_credit_limit,
            'Num_Credit_Inquiries': num_credit_inquiries,
            'Credit_Mix': credit_mix,
            'Outstanding_Debt': outstanding_debt,
            'Interest_Rate': interest_rate,
            'Credit_Utilization_Ratio': credit_utilization_ratio,
            'Credit_History_Age': credit_history_age,
            'Total_EMI_per_month': total_emi_per_month,
            'Amount_invested_monthly': amount_invested_monthly,
            'Monthly_Balance': monthly_balance,
            'Payment_of_Min_Amount': payment_of_min_amount,
            'Payment_Behaviour': payment_behavior
        }
        data= pd.DataFrame([data_raw])
        st.dataframe(data)
        result = model.predict(data)
        if result[0] == 0:
            st.write(f'### Credit Score Classification {name} : Good')
        elif result[0] == 1:
            st.write(f'### Credit Score Classification {name} : Poor')
        else :
            st.write(f'### Credit Score Classification {name} : Standard')

if __name__ == '__main__':
    run()