import streamlit as st
from database import add_data_payment

def create_payment():
    col1, col2 = st.columns(2)
    with col1:
        user_no = st.text_input("User ID:")
        prod_id = st.text_input("Product ID:")
        payment_no = st.text_input("Payment Number:")
    with col2:
        payment_type = st.selectbox("Payment Type:",["Cash","UPI","Net Banking"])
        total_price = st.number_input("Total Cost:")

    if st.button("Add payment"):
        if not user_no:
            user_no = None
        if not prod_id:
            prod_id = None
        if not payment_no:
            payment_no = None
        if not total_price:
            total_price = None
        add_data_payment(user_no,prod_id,payment_no,payment_type,total_price)
        st.success("Successfully Added Payment: {}".format(payment_no))