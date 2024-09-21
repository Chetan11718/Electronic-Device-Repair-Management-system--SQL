import pandas as pd
import streamlit as st
from database import view_all_data_prod_detail, view_only_prod_id, delete_prod_db
def delete_product():
    list_of_prod = [i[0] for i in view_only_prod_id()]
    selected_prod = st.selectbox("Product to Delete", list_of_prod)
    if selected_prod:
        st.warning("Do you want to Delete ::{}".format(selected_prod))
    if st.button("Delete Product"):
        delete_prod_db(selected_prod)
        st.success("Success!")
    result = view_all_data_prod_detail()
    df = pd.DataFrame(result, columns=['USER ID','PRODUCT ID', ' PRODUCT NAME', 'SLOT BOOKED DATE', 'NEED IT BY','PROBLEM'])
    with st.expander("Updated products"):
        st.dataframe(df)