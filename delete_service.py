import pandas as pd
import streamlit as st
from database import view_all_data_service, view_only_service_id, delete_service_db
def delete_service():
    list_of_service = [i[0] for i in view_only_service_id()]
    selected_service = st.selectbox("Service to Delete", list_of_service)
    if selected_service:
        st.warning("Do you want to delete ::{}".format(selected_service))
    if st.button("Delete service"):
        delete_service_db(selected_service)
        st.success("Success!")
    result = view_all_data_service()
    df = pd.DataFrame(result,
                      columns=['USER ID', 'PRODUCT ID','SERVICE ID', 'QUANTITY','ESTIMATED PRICE'])
    with st.expander("View Updated services"):
        st.dataframe(df)