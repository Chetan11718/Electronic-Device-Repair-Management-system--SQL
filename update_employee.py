import pandas as pd
import streamlit as st
from database import view_all_data_employee, view_only_emp_no, get_employee, edit_employee
def update_employee():
    list_of_employee = [i[0] for i in view_only_emp_no()]
    selected_employee = st.selectbox("Employee to Edit", list_of_employee)
    selected_result = get_employee(selected_employee)
    if selected_result:
        emp_no = selected_result[0][0]
        fname = selected_result[0][1]
        lname = selected_result[0][2]
        sex = selected_result[0][3]
        ser_no = selected_result[0][4]
    col1, col2 = st.columns(2)
    with col1:
        new_emp_no = st.text_input("Employee ID:")
        new_fname = st.text_input("First Name:")
        new_lname = st.text_input("Last Name:")
    with col2:
        new_sex = st.selectbox("Sex:",["Male","Female"])
        new_ser_no = st.text_input("Service ID :")
    if st.button("Update Employee"):
        if not new_emp_no:
            new_emp_no = None
        if not new_fname:
            new_fname = None
        if not new_lname:
            new_lname = None
        if not new_user_no:
            new_user_no = None
        if not new_sex:
            new_sex= None
        if not new_ser_no:
            new_ser_no = None

        edit_employee(new_emp_no, new_fname, new_lname, new_sex, new_ser_no, emp_no, fname, lname, sex, ser_no)
        st.success("Successfully updated Employee:: {} to ::{}".format(emp_no, new_emp_no))
    result = view_all_data_employee()
    df = pd.DataFrame(result, columns=['EMPLOYEE ID', 'FIRST NAME', 'LAST NAME', 'SEX', 'SERVICE ID'])
    with st.expander("View Employee"):
        st.dataframe(df)