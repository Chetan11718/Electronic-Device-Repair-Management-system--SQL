import pandas as pd
import streamlit as st
from database import view_all_data_service, view_only_service_id, get_service, edit_service_data
def update_service():
    list_of_service = [i[0] for i in view_only_service_id()]
    selected_service = st.selectbox("Service to Edit", list_of_service)
    selected_result = get_service(selected_service)
    if selected_result:
        user_no = selected_result[0][0]
        prod_id = selected_result[0][1]
        ser_no = selected_result[0][2]
        qty = selected_result[0][3]
        estimated_price = selected_result[0][4]
    col1, col2 = st.columns(2)
    with col1:
        new_user_no = st.text_input("User ID:")
        new_prod_id = st.text_input("Product ID:")
        new_ser_no = st.text_input("Service ID:")
    with col2:
        new_qty = st.number_input("Quantity:",0,10)
        new_estimated_price = st.number_input("Estimated Price:",-100,100000)
    if st.button("Update service"):
        if not new_user_no:
            new_user_no = None
        if not new_prod_id:
            new_prod_id = None
        if not new_ser_no:
            new_ser_no = None
        if not new_estimated_price:
            new_estimated_price = None
        edit_service_data(new_user_no, new_prod_id, new_ser_no, new_qty, new_estimated_price, user_no, prod_id, ser_no, qty, estimated_price)
        st.success("Successfully updated:: {} to ::{}".format(ser_no, new_ser_no))
    result = view_all_data_service()
    df = pd.DataFrame(result,
                      columns=['USER ID', 'PRODUCT ID','SERVICE ID', 'QUANTITY','ESTIMATED PRICE'])
    with st.expander("View Updated services"):
        st.dataframe(df)