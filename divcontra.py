import streamlit as st
import pandas as pd
import plotly.express as px

# Setting the layout to evenly spread my containers
st.set_page_config(layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('/Users/clementngatia/Downloads/Divorce&Contraception/NSFG_2022_2023_FemRespPUFData (Autosaved).xlsx')

div_cont = load_data()

# Setting the title for the page
st.title("Modern Contraception and Divorce")
st.markdown()