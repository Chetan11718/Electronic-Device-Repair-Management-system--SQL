import streamlit as st
from database import add_data_service
def create_service():
    col1, col2 = st.columns(2)
    with col1:
        user_no = st.text_input("User Number:")
        prod_id = st.text_input("Product ID:")
        ser_no = st.text_input("Serivice ID:")
    with col2:
        qty = st.number_input("Quantity:",1,100)
        estimated_price = st.number_input(" Estimated Price :",-10000,100000)
    if st.button("Add Services"):
        if not user_no:
            user_no = None
        if not prod_id:
            prod_id= None
        if not ser_no:
            ser_no = None
        if not qty:
            qty = None
        if not estimated_price:
            estimated_price = None
        add_data_service(user_no, prod_id, ser_no, qty,estimated_price)
        st.success("Successfully added Services: {}".format(ser_no))