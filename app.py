# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password="dimpu123"
# )
# c = mydb.cursor()
# c.execute("CREATE DATABASE demo7")
import streamlit as st
from create import create
from database import create_tables
from delete import delete
from read import read
from update import update
from custom import custom
from PIL import Image
from operations import operations
#opening the image
# image = Image.open('C:\\Users\\CHETAN\\OneDrive\\Desktop\\PES1UG20CS109\\DBMS\\PROJECT\\proj\\image.jpg')
# #displaying the image on streamlit app
# st.image(image)



def main():
    st.title("ELECTRONIC DEVICE REPAIR MANAGEMENT")
    st.subheader("Chetan Reddy Bandi - PES1UG20CS109")
    menu = ["Create", "Read", "Update", "Delete", "Enter Query","Operations"]
    list_of_tables=['User Details', 'Product', 'Service', 'Employee', 'Payment']
    choice = st.sidebar.selectbox("Menu", menu)
    create_tables()
    if choice == "Create":
        st.subheader("Choose the Table: ")
        selected_table = st.selectbox("Table to Create", list_of_tables)
        create(selected_table)
    elif choice == "Read":
        st.subheader("Choose the Table: ")
        selected_table = st.selectbox("Table to Read", list_of_tables)
        read(selected_table)
    elif choice == "Update":
        st.subheader("Choose the Table: ")
        selected_table = st.selectbox("Table to Update", list_of_tables)
        update(selected_table)
    elif choice == "Delete":
        st.subheader("Choose the Table: ")
        selected_table = st.selectbox("Table to Delete", list_of_tables)
        delete(selected_table)
    elif choice == "Enter Query":
        custom()
    elif choice == "Operations":
        operations()
    else:
        st.subheader("About Electronic")
if __name__ == '__main__':
    main()