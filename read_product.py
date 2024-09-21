import pandas as pd
import streamlit as st
from database import view_all_data_prod_detail
def read_product():
    result = view_all_data_prod_detail()
    df = pd.DataFrame(result, columns=['USER ID','PRODUCT ID', ' PRODUCT NAME', 'SLOT BOOKED DATE', 'NEED IT BY','PROBLEM'])
    with st.expander("View all Products"):
        st.dataframe(df)