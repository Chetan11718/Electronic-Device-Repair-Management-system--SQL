import streamlit as st
from database import custom_query
import pandas as pd

def custom():
    cols = st.text_input("Enter the names of the columns seperated by ',': ")
    cols = cols.split(sep=',')
    query = st.text_input("Enter the query:")
    if query:
        result = custom_query(query)
        df = pd.DataFrame(result, columns=cols)
        with st.expander("View Results"):
            st.dataframe(df)