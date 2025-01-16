# Libraries
import pandas as pd
import numpy as np

import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():
    # HEADING
    st.markdown("<h1 style='text-align: center;'>EXPLORATORY DATA ANALYSIS</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: green;'>CREDIT SCORE CLASSIFICATION</h3>", unsafe_allow_html=True)
    # LINE
    st.write('---')

    # BANNER
    st.image('https://img.theepochtimes.com/assets/uploads/2022/09/01/credit-score-shutterstock_1694647429.jpg',
            caption='img.theepochtimes.com')
    st.write('''
Credit scores play a critical role in evaluating a customer's creditworthiness, allowing financial companies to assess risk, and set appropriate loan regulations. Customers with good credit scores are considered low-risk and typically receive better financial terms, while those with poor credit scores are viewed as high-risk, often facing higher interest rates or loan rejections.

Categorizing customers based on their credit scores enables lenders to make faster, data-driven decisions, improving efficiency and ensuring more personalized financial offerings. However, the traditional manual process of categorizing customers into credit score brackets is time-consuming and prone to human error and inconsistency, leading to inefficiencies and higher operational costs.

By automating this process with a machine learning model, the company can significantly enhance the accuracy, speed, and scalability of credit score classification.
             ''')

    # menampilkan dataframe
    st.write('## DATASET')
    st.write('### KAGGLE : Credit Score Classification')
    st.write('###### by ROHAN PARIS')
    st.markdown("<a href='https://www.kaggle.com/datasets/parisrohan/credit-score-classification/data?select=train.csv'> LINK DATASET </a>", unsafe_allow_html=True)

    data = pd.read_csv('credit_score.csv')
    st.dataframe(data.head())
    st.write('''
## Data dimension

This dataset contains :           
column  : 28            
row     : 10000
             ''')

    # klo paragraf panjang pake kutip 3
    st.write('''
        ## Dataset columns information :

        ID: Unique ID of the record
             
        Customer_ID: Unique ID of the customer
             
        Month: Month of the year
             
        Name: The name of the customer
             
        Age: The age of the customer
             
        SSN: Social Security Number of the customer
             
        Occupation: The occupation of the customer
             
        Annual_Income: The Annual Income of the customer
             
        Monthly_Inhand_Salary: Monthly in-hand salary of the customer
             
        Num_Bank_Accounts: The number of bank accounts of the customer
             
        Num_Credit_Card: Number of credit cards the customer is having
             
        Interest_Rate: The interest rate on the credit card of the customer
             
        Num_of_Loan: The number of loans taken by the customer from the bank
             
        Type_of_Loan: The types of loans taken by the customer from the bank
             
        Delay_from_due_date: The average number of days delayed by the customer from the date of payment
             
        Num_of_Delayed_Payment: Number of payments delayed by the customer
             
        Changed_Credit_Card: The percentage change in the credit card limit of the customer
             
        Num_Credit_Inquiries: The number of credit card inquiries by the customer
             
        Credit_Mix: Classification of Credit Mix of the customer
             
        Outstanding_Debt: The outstanding balance of the customer
             
        Credit_Utilization_Ratio: The credit utilization ratio of the credit card of the customer
             
        Credit_History_Age: The age of the credit history of the customer
             
        Payment_of_Min_Amount: Yes if the customer paid the minimum amount to be paid only, otherwise no.
             
        Total_EMI_per_month: The total EMI per month of the customer
             
        Amount_invested_monthly: The monthly amount invested by the customer
             
        Payment_Behaviour: The payment behaviour of the customer
             
        Monthly_Balance: The monthly balance left in the account of the customer
             
        Credit_Score: The person’s credit score (target variable: 'Good,' 'Poor,' 'Standard').
        ''')

    st.write('# Data Visualization')

    st.write('## Categorical Columns Visualization')
    fig1, axis = plt.subplots(nrows=5, ncols=1, figsize=(15,20))
    fig1.subplots_adjust(hspace=1)

    sns.countplot(x=data['Month'], ax=axis[0], palette='icefire')
    axis[0].tick_params(axis='x', rotation=45)

    sns.countplot(x=data['Occupation'], ax=axis[1], palette='icefire')
    axis[1].tick_params(axis='x', rotation=45)

    sns.countplot(x=data['Credit_Mix'], ax=axis[2], palette='icefire')
    axis[2].tick_params(axis='x', rotation=45)

    sns.countplot(x=data['Payment_of_Min_Amount'], ax=axis[3], palette='icefire')
    axis[3].tick_params(axis='x', rotation=45)

    sns.countplot(x=data['Payment_Behaviour'], ax=axis[4], palette='icefire')
    axis[4].tick_params(axis='x', rotation=45)

    st.pyplot(fig1)

    st.write('**Insight :**')
    st.write('- Occupation, Credit_Mix has value "__"')
    st.write('- Payment_of_Min_Amount has wrong entries "NM"')
    st.write('- Payment Behaviour has wrong entries "!@9#%8"')

    st.write('## Numerical Columns Visualization')
    fig2, axis = plt.subplots(nrows=8, ncols=1, figsize=(15,40))
    fig2.subplots_adjust(hspace=1)

    sns.distplot(data['Monthly_Inhand_Salary'], ax=axis[0])
    axis[0].tick_params(axis='x', rotation=45)

    sns.distplot(data['Num_Bank_Accounts'], ax=axis[1])
    axis[1].tick_params(axis='x', rotation=45)

    sns.distplot(data['Num_Credit_Card'], ax=axis[2])
    axis[2].tick_params(axis='x', rotation=45)

    sns.distplot(data['Interest_Rate'], ax=axis[3])
    axis[3].tick_params(axis='x', rotation=45)

    sns.distplot(data['Delay_from_due_date'], ax=axis[4])
    axis[4].tick_params(axis='x', rotation=45)

    sns.distplot(data['Num_Credit_Inquiries'], ax=axis[5])
    axis[5].tick_params(axis='x', rotation=45)

    sns.distplot(data['Credit_Utilization_Ratio'], ax=axis[6])
    axis[6].tick_params(axis='x', rotation=45)

    sns.distplot(data['Total_EMI_per_month'], ax=axis[7])
    axis[7].tick_params(axis='x', rotation=45)

    st.pyplot(fig2)

    st.write('**Insight :**')
    st.write('- Num_Bank_Accounts have very high maximum value, and its minimum value is negative value. This variable cant be negative.')
    st.write('- Num_Credit_Card have very high maximum value.')
    st.write('- Num_of_Loan have a negative value. This variable cant be negative.')

    st.write('## Target Count')
    fig3 = plt.figure(figsize=(10,8))
    sns.countplot(data['Credit_Score'],palette='icefire')
    st.pyplot(fig3)
    st.write('### Target Count is Imbalanced')

if __name__ == '__main__':
    run()