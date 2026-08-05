import streamlit as st
from db import get_connection
import pandas as pd

@st.dialog("Student Details :",width='large')
def show_details(branch, year):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM STUDENTS
                WHERE year = :1
                AND branch = :2
            """, [year, branch])
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
            show_details('AIML',1)
        if st.button("SY",key='AIML_SY') :
            show_details('AIML',2)
        if st.button("TY",key='AIML_TY') :
            show_details('AIML',3)

                

with IS :
    with st.expander('Instrumentation Enggineering') :

        if st.button("FY",key='IS_FY') :
            show_details('IS',1)
        if st.button("SY",key='IS_SY') :
            show_details('IS',2)
        if st.button("TY",key='IS_TY') :
            show_details('IS',3)
        

# st.snow()