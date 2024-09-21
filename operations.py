import streamlit as st
from functions import query_execute 
from procedure import procedure_execute
import pandas as pd


def operations():
    tab1, tab2 = st.tabs(["Prodecure", "Function"])

    with tab1:
        st.subheader("Procedure Call")
        if st.button("Update Age"):
            try:
                res = procedure_execute("select * from user_details where user_no='1004'")
            except Exception as e:
                st.warning(e)
            finally:
                st.info("Executed")
                df = pd.DataFrame(res)
                df.index += 1
                st.dataframe(df, use_container_width=True)


    with tab2:
        st.subheader("Function Call")
        if st.button("Checking Valid Cost"):
            try:
                res = query_execute(
                    "with t as (Select user_no,payment_no,total_price as count from payment group by user_no) select user_no,payment_no,count_cost(count) as Validate,count as Cost from t;")
            except Exception as e:
                st.warning(e)
            finally:
                st.info("Executed")
                df = pd.DataFrame(res)
                df.index += 1
                st.dataframe(df, use_container_width=True)
