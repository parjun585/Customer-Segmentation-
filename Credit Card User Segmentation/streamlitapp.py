from sklearn import preprocessing 
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load the model and the dataset
filename = 'final_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
df = pd.read_csv("Clustered_Customer_Data.csv")

# Streamlit UI
st.markdown('<style>body{background-color: Blue;}</style>', unsafe_allow_html=True)
st.title("Customer Segmentation Prediction")

# Input form
with st.form("my_form"):
    balance = st.number_input(label='Balance', step=0.001, format="%.6f")
    balance_frequency = st.number_input(label='Balance Frequency', step=0.001, format="%.6f")
    purchases = st.number_input(label='Purchases', step=0.01, format="%.2f")
    oneoff_purchases = st.number_input(label='OneOff_Purchases', step=0.01, format="%.2f")
    installments_purchases = st.number_input(label='Installments Purchases', step=0.01, format="%.2f")
    cash_advance = st.number_input(label='Cash Advance', step=0.01, format="%.6f")
    purchases_frequency = st.number_input(label='Purchases Frequency', step=0.01, format="%.6f")
    oneoff_purchases_frequency = st.number_input(label='OneOff Purchases Frequency', step=0.1, format="%.6f")
    purchases_installment_frequency = st.number_input(label='Purchases Installments Frequency', step=0.1, format="%.6f")
    cash_advance_frequency = st.number_input(label='Cash Advance Frequency', step=0.1, format="%.6f")
    cash_advance_trx = st.number_input(label='Cash Advance Trx', step=1)
    purchases_trx = st.number_input(label='Purchases TRX', step=1)
    credit_limit = st.number_input(label='Credit Limit', step=0.1, format="%.1f")
    payments = st.number_input(label='Payments', step=0.01, format="%.6f")
    minimum_payments = st.number_input(label='Minimum Payments', step=0.01, format="%.6f")
    prc_full_payment = st.number_input(label='PRC Full Payment', step=0.01, format="%.6f")
    tenure = st.number_input(label='Tenure', step=1)

    # Collect data in a list
    data = [[balance, balance_frequency, purchases, oneoff_purchases, installments_purchases, cash_advance, 
             purchases_frequency, oneoff_purchases_frequency, purchases_installment_frequency, 
             cash_advance_frequency, cash_advance_trx, purchases_trx, credit_limit, payments, 
             minimum_payments, prc_full_payment, tenure]]

    # Submit button
    submitted = st.form_submit_button("Submit")

# Prediction and result display
if submitted:
    clust = loaded_model.predict(data)[0]
    st.write(f'Data Belongs to Cluster: {clust}')

    # Filter the dataframe for the predicted cluster
    cluster_df1 = df[df['Cluster'] == clust]

    # Plot histograms for the cluster
    st.write(f"Displaying histograms for Cluster {clust}")
    for c in cluster_df1.drop(['Cluster'], axis=1):
        fig, ax = plt.subplots(figsize=(5, 5))
        sns.histplot(cluster_df1[c], ax=ax)
        ax.set_title(f'Distribution of {c}')
        st.pyplot(fig)  # Pass the figure directly to st.pyplot
