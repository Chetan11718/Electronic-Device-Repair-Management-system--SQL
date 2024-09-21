import pandas as pd
import streamlit as st
from database import view_all_data_employee, view_only_emp_no, delete_employee_db
def delete_employee():
    list_of_employee = [i[0] for i in view_only_emp_no()]
    selected_employee = st.selectbox("Employee to Delete", list_of_employee)
    if selected_employee:
        st.warning("Do you want to delete ::{}".format(selected_employee))
    if st.button("Delete Employee"):
        delete_employee_db(selected_employee)
        st.success("Success!")
    result = view_all_data_employee()
    df = pd.DataFrame(result, columns=['EMPLOYEE ID', 'FIRST NAME', 'LAST NAME', 'SEX', 'SERVICE ID'])
    with st.expander("View all Employee"):
        st.dataframe(df)