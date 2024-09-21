import pandas as pd
import streamlit as st
from database import view_all_data_prod_detail, view_only_prod_id, get_prod, edit_prod_data
def update_product():
    list_of_prod = [i[0] for i in view_only_prod_id()]
    selected_prod = st.selectbox("Product to Edit", list_of_prod)
    selected_result = get_prod(selected_prod)
    if selected_result:
        prod_id = selected_result[0][0]
        user_no=selected_result[0][1]
        name = selected_result[0][2]
        slot_booking_date = selected_result[0][3]
        need_it_by = selected_result[0][4]
        problem= selected_result[0][5]
    col1, col2 = st.columns(2)
    with col1:
        new_prod_id = st.text_input("Product ID:")
        new_user_no=st.text_input("User ID:")
        new_name = st.text_input("Name:")
    with col2:
        new_slot_booking_date = st.date_input("Slot Booking Date:")
        new_need_it_by = st.date_input("Need It By:")
        new_problem=st.text_input("Problem:")
    if st.button("Update Product"):
        if not new_prod_id:
            new_prod_id = None
        if not new_user_no:
            new_user_no = None
        if not new_name:
            new_name = None
        edit_prod_data(new_user_no,new_prod_id, new_name, new_slot_booking_date, new_need_it_by,new_problem,user_no,prod_id, name, slot_booking_date, need_it_by,problem)
        st.success("Successfully Updated:: {} to ::{}".format(prod_id, new_prod_id))
    result = view_all_data_prod_detail()
    df = pd.DataFrame(result, columns=['USER ID','PRODUCT ID', ' PRODUCT NAME', 'SLOT BOOKED DATE', 'NEED IT BY','PROBLEM'])
    with st.expander("Updated Products"):
        st.dataframe(df)