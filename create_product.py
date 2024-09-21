import streamlit as st
from database import add_data_product

def create_product():
    col1, col2 = st.columns(2)
    with col1:
        user_no=st.text_input("User ID:")
        prod_id = st.text_input("Product ID:")
        name=st.text_input("Product Name:")
    with col2:
        slot_booking_date = st.date_input("Slot Booking Date:")
        need_it_by = st.date_input("Need It By:")
        problem = st.text_input("Problem:")
    if st.button("Add product"):
        if not user_no:
            user_no = None
        if not prod_id:
            prod_id= None
        add_data_product(user_no,prod_id,name, slot_booking_date, need_it_by, problem)
        st.success("Successfully Added Product: {}".format(prod_id))