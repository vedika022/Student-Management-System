import streamlit as st
from db import get_connection

st.header('Delete Student Data :')
'Will delete student data permanently !'

dept = st.selectbox("Select Department",["Artificial Intelligence and Machine Learning","Instrumentation Enggineering"])

year = st.selectbox("Select Year",["FY", "SY", "TY"],)

enrl_num = st.text_input("Enter Enrollment Number")

if "show_confirm" not in st.session_state:
    st.session_state.show_confirm = False

@st.dialog("Confirm Delete")
def confirm_delete():
    st.write("Are you sure you want to permanently delete this item?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes"):
            # Delete logic here
            st.success("Item deleted.")
            st.session_state.show_confirm = False
            st.rerun()

    with col2:
        if st.button("No"):
            st.session_state.show_confirm = False
            st.rerun()

if st.button('Delete Record') :
    confirm_delete()

    
