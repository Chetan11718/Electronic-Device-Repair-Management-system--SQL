import pandas as pd
import streamlit as st
from database import view_all_data_user
def read_user():
    result = view_all_data_user()
    df = pd.DataFrame(result, columns=['User ID' , 'First Name' ,'Last Name' , 'Sex' , 'Phone Number' , 'Date Of Birth', 'Age', 'Email ID'])
    with st.expander("View all Users"):
        st.dataframe(df)