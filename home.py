import oracledb 
import streamlit as st

oracledb.init_oracle_client( lib_dir=r"C:\oraclexe\instantclient_23_26")

connection = oracledb.connect(user = 'STUDENTS', password = 'me12', dsn = 'localhost:1521/XE')
if connection :
    st.toast("Connected succesfully !")

st.title('Student Managment System !')

# if st.button("NExt page ") :
#     st.switch_page("pages/view.py")

st.balloons()



