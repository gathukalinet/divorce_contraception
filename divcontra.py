import streamlit as st
import pandas as pd
import plotly.express as px

# Setting the layout to evenly spread my containers
st.set_page_config(layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('/Users/clementngatia/Downloads/Divorce&Contraception/NSFG_2022_2023_FemRespPUFData.csv', encoding = "latin-1")

div_cont = load_data()

# Setting the title for the page
st.title("Modern Contraception and Divorce :broken_heart:")
st.text(
    'Divorce is defined as the legal dissolution of a marriage between two people while Contraception is the deliberate use of artificial methods or other techniques to prevent pregnancy and/or plan the number and spacing of children')
st.markdown("This analysis was inspired by a [YouTube episode](https://youtu.be/9OEZPGU7A5w?t=3766) suggesting that families using contraception are more likely to divorce than those practicing natural family planning. Supporting literature for the claims made on the YouTube post are [The influence of contraception, abortion, and natural family planning on divorce rates](https://pmc.ncbi.nlm.nih.gov/articles/PMC4536625/); a study based on combined surveys from 2006 to 2010 and indicated much smaller ranges in contraception users vs natural family planning users divorce rates")

