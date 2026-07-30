import oracledb 
import streamlit as st

oracledb.init_oracle_client( lib_dir=r"C:\oraclexe\instantclient_23_26")


connection = oracledb.connect(user = 'STUDENTS', password = 'me12', dsn = 'localhost:1521/XE')

if "connection_toast_shown" not in st.session_state:
    st.toast("Connected successfully!")
    st.session_state.connection_toast_shown = True

pg = st.navigation(['Home.py','pages/Insert.py','pages/View.py'], position='top')
pg.run()