import pandas as pd
import streamlit as st
from database import view_all_data_user, view_only_user_no, get_user, edit_user_data
def update_user():
    list_of_user = [i[0] for i in view_only_user_no()]
    selected_user = st.selectbox("User to Edit", list_of_user)
    selected_result = get_user(selected_user)
    if selected_result:
        user_no   = selected_result[0][0]
        fname = selected_result[0][1]
        lname = selected_result[0][2]
        sex = selected_result[0][3]
        phone_no = selected_result[0][4]
        dob = selected_result[0][5]
        age = selected_result[0][6]
        email = selected_result[0][7]

    col1, col2 = st.columns(2)
    with col1:
        new_user_no = st.text_input("User ID:")
        new_fname = st.text_input("First Name:")
        new_lname = st.text_input("Last Name:")
        new_sex = st.selectbox("Sex:",['Male','Female'])
    with col2:
        new_phone_no = st.text_input("Phone Number:")
        new_dob = st.date_input("DOB:")
        new_age=st.number_input("Age Of The User:",0,100)
        new_email=st.text_input("Email ID:")
    if st.button("Update user"):
        if not new_user_no:
            new_user_no=None
        if not new_fname:
            new_fname = None
        if not new_lname:
            new_lname = None
        if not new_sex:
            new_sex = None
        if not new_phone_no:
            new_phone_no = None
        if not new_dob:
            new_dob = None
        edit_user_data(new_user_no, new_fname, new_lname, new_sex, new_phone_no,new_dob,new_age,new_email,user_no, fname, lname, sex, phone_no, dob,age,email)
        st.success("Successfully Updated:: {} to ::{}".format(user_no, new_user_no))
    result = view_all_data_user()
    df = pd.DataFrame(result, columns=['User ID' , 'First Name' ,'Last Name' , 'Sex' , 'Phone Number' , 'Date Of Birth','Age','Email ID'])
    with st.expander("Updated Users"):
        st.dataframe(df)