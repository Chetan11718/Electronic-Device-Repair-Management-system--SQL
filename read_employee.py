import pandas as pd
import streamlit as st
from database import view_all_data_employee
def read_employee():
    result = view_all_data_employee()
    df = pd.DataFrame(result, columns=['EMPLOYEE ID', 'FIRST NAME', 'LAST NAME', 'SEX', 'SERVICE ID'])
    with st.expander("View all Employee"):
        st.dataframe(df)