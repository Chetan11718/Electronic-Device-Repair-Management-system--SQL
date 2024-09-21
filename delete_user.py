import pandas as pd
import streamlit as st
from database import view_all_data_user, view_only_user_no, delete_user_db
def delete_user():
    list_of_user = [i[0] for i in view_only_user_no()]
    selected_user = st.selectbox("User to Delete", list_of_user)
    if selected_user:
        st.warning("Do you want to delete ::{}".format(selected_user))
    if st.button("Delete user"):
        delete_user_db(selected_user)
        st.success("Success!")
    result = view_all_data_user()
    df = pd.DataFrame(result, columns=['User ID' , 'First Name' ,'Last Name' , 'Sex' , 'Phone Number' , 'Date Of Birth', 'Age','Email ID'])
    with st.expander("Updated users"):
        st.dataframe(df)