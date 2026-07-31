import streamlit as st
from db import get_connection
import pandas as pd

@st.dialog("Student Details :")
def show_details(table):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table}")
            columns = [c[0] for c in cursor.description]
            rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df)
    except Exception as e:
        st.error(e)




# st.set_page_config(layout = 'wide')
AIML, IS = st.columns(2)

with AIML :
    with st.expander('Artificial Intelligence and Machine Learning') :

        st.write("STUDENT DETAILS :")
        if st.button("FY", key='AIML_FY') :
            show_details('AIML_STUDENTS_FY')
        if st.button("SY",key='AIML_SY') :
            show_details('AIML_STUDENTS_SY')
        if st.button("TY",key='AIML_TY') :
            show_details('AIML_STUDENTS_TY')

                

with IS :
    with st.expander('Instrumentation Enggineering') :

        if st.button("FY",key='IS_FY') :
            show_details('IS_STUDENTS_FY')
        if st.button("SY",key='IS_SY') :
            show_details('IS_STUDENTS_SY')
        if st.button("TY",key='IS_TY') :
            show_details('IS_STUDENTS_TY')
        

# st.snow()