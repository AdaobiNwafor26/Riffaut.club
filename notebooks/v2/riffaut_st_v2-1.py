import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# setting the page config
st.set_page_config(page_title='Customer Analytics Dashboard', layout='wide')

# setting up some custome css for the blue - dark blue theme
st.markdown("""
<style>
    .reportview-container {
        background: linear-gradient(to right, #1e3c72, #2a5298);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(to bottom, #2a5298, #1e3c72);
    }
    .Widget>label {
        color: white;
    }
    .stplot {
        background-color: rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_excel('notebooks/v2/df_customers_full.xlsx')
    monthly_rev = pd.read_excel('notebooks/v2/monthly_revenue_trends.xlsx')
    quarterly_rev = pd.read_excel('notebooks/v2/quarterly_revenue_trends.xlsx')
    customer_reten_monthly = pd.read_excel('notebooks/v2/df_customer_reten_monthly.xlsx')
    customer_reten_quarterly = pd.read_excel('notebooks/v2/df_customer_reten_quarterly.xlsx')
    churn_rate_monthly = pd.read_excel('notebooks/v2/customer_monthly_churn_rate.xlsx')
    churn_rate_quarterly = pd.read_excel('notebooks/v2/customer_quarterly_churn_rate.xlsx')
    cltv = pd.read_excel('notebooks/v2/customer_lifetime_value.xlsx')
    customer_churn_probability = pd.read_excel('notebooks/v2/churn_probability_by_customer.xlsx')
    rfm_table = pd.read_excel('notebooks/v2/rfm_table.xlsx')
    rfm_customer_segment = pd.read_excel('notebooks/v2/rfm_customer_segment.xlsx')
    rfm_segment_final = pd.read_excel('notebooks/v2/rfm_segment_final.xlsx')
    product_affinity = pd.read_excel('notebooks/v2/productivity_affinity.xlsx')

    return (df, monthly_rev, quarterly_rev, customer_churn_probability, 
            customer_churn_probability, customer_reten_monthly, 
            customer_reten_quarterly, churn_rate_monthly, churn_rate_quarterly, 
            cltv, rfm_customer_segment, rfm_segment_final, rfm_table, product_affinity)

# loading the data
(df, monthly_rev, quarterly_rev, customer_churn_probability, 
customer_churn_probability, customer_reten_monthly, 
customer_reten_quarterly, churn_rate_monthly, churn_rate_quarterly, 
cltv, rfm_customer_segment, rfm_segment_final, rfm_table, product_affinity) = load_data()


st.title('Customer Analytics Dashboard')

st.sidebar.header('Filters')