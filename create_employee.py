import streamlit as st
from database import add_data_employee

def create_employee():
    col1, col2 = st.columns(2)
    with col1:
        emp_no = st.text_input("Employee ID:")
        fname = st.text_input("First Name:")
        lname = st.text_input("Last Name:")
    with col2:
        sex = st.selectbox("Sex:",["Male","Female"])
        ser_no = st.text_input("Service ID:")
    if st.button("Add Employee"):
        if not emp_no:
            emp_no = None
        if not fname:
            fname = None
        if not lname:
            lname = None
        if not user_no:
            user_no = None
        if not sex:
            sex= None
        if not ser_no:
            ser_no = None
        add_data_employee(emp_no, fname, lname, sex, ser_no)
        st.success("Successfully added Employee: {}".format(emp_no))