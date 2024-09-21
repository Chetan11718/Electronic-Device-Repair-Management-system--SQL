import pandas as pd
import streamlit as st
from database import view_all_data_payment, view_only_payment_no, get_payment, edit_payment
def update_payment():
    list_of_payment = [i[0] for i in view_only_payment_no()]
    selected_payment = st.selectbox("Payment to Edit", list_of_payment)
    selected_result = get_payment(selected_payment)
    if selected_result:
        user_no = selected_result[0][0]
        prod_id = selected_result[0][1]
        payment_no = selected_result[0][2]
        payment_type = selected_result[0][3]
        total_price = selected_result[0][4]
    col1, col2 = st.columns(2)
    with col1:
        new_user_no = st.text_input("User ID:")
        new_prod_id = st.text_input("Product ID:")
        new_payment_no = st.text_input("Payment Number:")
    with col2:
        new_payment_type = st.selectbox("Payment Type:",["Cash","UPI","Net Banking"])
        new_total_price = st.number_input("Total Cost:")

    if st.button("Update payment"):
        if not new_user_no:
            new_user_no = None
        if not new_prod_id:
            new_prod_id = None
        if not new_payment_no:
            new_payment_no = None
        if not new_total_price:
            new_total_price = None
        edit_payment(new_user_no, new_prod_id,new_payment_no,new_payment_type,new_total_price,user_no, prod_id, payment_no, payment_type, total_price)
        st.success("Successfully updated:: {} to ::{}".format(payment_no, new_payment_no))
    result = view_all_data_payment()
    df = pd.DataFrame(result,
                      columns=['USER ID','PRODUCT ID','PAYMENT NO','PAYMENT TYPE','TOTAL COST'])
    with st.expander("View All Payments"):
        st.dataframe(df)