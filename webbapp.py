import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load your model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Load data (if needed)
data = pd.read_csv("Indian_Personal_Finance_spending_habbits.csv")

# Define your prediction function
def predict_savings(age, dependents, occupation, city_tier, rent,
                    loan_repayment, insurance, groceries,
                    transport, eating_out, entertainment,
                    utilities, healthcare, education,
                    miscellaneous):
    # Implement your calculation logic here
    disposable_income = ...  # Replace with actual calculation
    potential_savings = ...   # Replace with actual calculation
    return disposable_income, potential_savings

# Streamlit user input form
st.title("Disposable Income and Savings Predictor")

with st.form(key='user_input'):
    age = st.number_input('Age', min_value=0)
    income = st.number_input('Monthly Income', min_value=0)
    dependents = st.number_input('Number of Dependents', min_value=0)
    occupation = st.selectbox('Occupation', ['Self_Employed', 'Retired', 'Student', 'Professional'])
    city_tier = st.selectbox('City Tier', ['Tier_1', 'Tier_2', 'Tier_3'])
    rent = st.number_input('Monthly Rent')
    loan_repayment = st.number_input('Monthly Loan Repayment')
    insurance = st.number_input('Monthly Insurance Cost')
    groceries = st.number_input('Monthly Groceries Expense')
    transport = st.number_input('Monthly Transport Expense')
    eating_out = st.number_input('Monthly Eating Out Expense')
    entertainment = st.number_input('Monthly Entertainment Expense')
    utilities = st.number_input('Monthly Utilities Expense')
    healthcare = st.number_input('Monthly Healthcare Expense')
    education = st.number_input('Monthly Education Expense')
    miscellaneous = st.number_input('Monthly Miscellaneous Expenses')

    submit_button = st.form_submit_button(label='Predict Savings')

if submit_button:
    disposable_income, potential_savings = predict_savings(age, dependents, occupation,
                                                           city_tier, rent,
                                                           loan_repayment,
                                                           insurance,
                                                           groceries,
                                                           transport,
                                                           eating_out,
                                                           entertainment,
                                                           utilities,
                                                           healthcare,
                                                           education,
                                                           miscellaneous)
    
    # Display results
    st.write(f"Estimated Disposable Income: {disposable_income}")
    st.write(f"Potential Savings: {potential_savings}")
