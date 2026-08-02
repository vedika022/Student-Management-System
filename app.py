import streamlit as st

pg = st.navigation(['Home.py','pages/Insert.py','pages/View.py','pages/Update.py','pages/Delete.py'], position='top')

pg.run()