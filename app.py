
import streamlit as st
from db import get_connection

connection = get_connection()

if connection :
    st.toast("Connected !")

pg = st.navigation(['Home.py','pages/Insert.py','pages/View.py','pages/Update.py'], position='top')
pg.run()