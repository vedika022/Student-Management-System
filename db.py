import streamlit as st
import oracledb

oracledb.init_oracle_client(lib_dir=r"C:\oraclexe\instantclient_23_26")

@st.cache_resource
def get_connection():
    return oracledb.connect(
        user="STUDENTS",
        password="me12",
        dsn="localhost:1521/XE"
    )