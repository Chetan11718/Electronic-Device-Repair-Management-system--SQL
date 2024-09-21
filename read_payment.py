import pandas as pd
import streamlit as st
from database import view_all_data_payment
def read_payment():
    result = view_all_data_payment()
    df = pd.DataFrame(result, columns=['USER ID','PRODUCT ID','PAYMENT NO','PAYMENT TYPE','TOTAL COST'])
    with st.expander("View all Payment"):
        st.dataframe(df)