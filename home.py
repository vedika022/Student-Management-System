import streamlit as st
from db import get_connection

connection = get_connection()

if connection :
    st.toast("Connected !")
st.title('Student Managment System !',text_alignment='center')
""
# st.header("A platform for maintaining student records and viewing academic results.",text_alignment = 'center')




