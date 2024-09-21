import streamlit as st
from database import add_data_user

def create_user():
    col1, col2 = st.columns(2)
    with col1:
        user_no = st.text_input("User ID:") 
        fname = st.text_input("First Name:")
        lname=st.text_input("Last Name:")
        sex=st.selectbox("Sex:",["Male","Female"])
    with col2:
        phone_no = st.text_input("Phone Number:")
        dob = st.date_input("Date Of Birth:")
        age=st.number_input("Age Of The User:",0,100)
        email=st.text_input("Email ID:")
    if st.button("Add USER"):
        if not user_no:
            user_no = None
        if not fname:
            fname = None
        if not lname:
            lname = None
        if not sex:
            sex = None
        if not phone_no:
            phone_no = None
        if not dob:
            dob = None
        if not age:
            age=None
        if not email:
            email=None

        add_data_user(user_no, fname, lname, sex, phone_no, dob,age ,email)
        st.success("Successfully Added User: {}".format(user_no))