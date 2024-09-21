import pandas as pd
import streamlit as st
from database import view_all_data_payment, view_only_payment_no, delete_payment_db
def delete_payment():
    list_of_payment = [i[0] for i in view_only_payment_no()]
    selected_payment = st.selectbox("Payment to Delete", list_of_payment)
    if selected_payment:
        st.warning("Do you want to delete ::{}".format(selected_payment))
    if st.button("Delete payment"):
        delete_payment_db(selected_payment)
        st.success("Success!")
    result = view_all_data_payment()
    df = pd.DataFrame(result,
                      columns=['USER ID','PRODUCT ID','PAYMENT NO','PAYMENT TYPE','TOTAL COST'])
    with st.expander("View all Payments"):
        st.dataframe(df)