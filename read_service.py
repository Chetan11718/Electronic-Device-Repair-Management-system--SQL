import pandas as pd
import streamlit as st
from database import view_all_data_service
def read_service():
    result = view_all_data_service()
    df = pd.DataFrame(result, columns=['USER ID', 'PRODUCT ID','SERVICE ID', 'QUANTITY','ESTIMATED PRICE'])
    with st.expander("View all Services"):
        st.dataframe(df)