import streamlit as st
from db import get_connection
import oracledb
import pandas as pd

st.title("Marks Entry : ")

def display_table(year,branch,subject,exam):

    connection = get_connection()
    with connection.cursor() as cursor :

        try :

            cursor.execute(
    f"""
    SELECT
        s.ENRLNO,
        s.FIRST_NAME,
        s.LAST_NAME,
        m.{exam}
    FROM STUDENTS s
    JOIN MARKS m
        ON s.ENRLNO = m.ENRLNO
    WHERE s.YEAR = :year
    AND s.BRANCH = :branch
    AND m.SUBJECT = :subject
    ORDER BY s.ENRLNO
    """,
            year=year,
            branch=branch,
            subject = subject
        )
            rows = cursor.fetchall()
            df = pd.DataFrame(rows,columns=[desc[0] for desc in cursor.description])
            return df

        except oracledb.Error as e :
            connection.rollback()
            st.write("Error :",e)


subjects = {
    ('AIML', 'FY'): [
        'Python',
        'Data Structures And Algorithms',
        'Computer Fundamentals'
    ],
    ('AIML', 'SY'): [
        'Database Management Systems',
        'Machine Learning',
        'Artificial Intelligence'
    ],
    ('AIML', 'TY'): [
        'Cloud Computing',
        'Deep Learning',
        'Natural Language Processing'
    ],
    ('IS', 'FY'): [
        'science',
        'maths',
        'instrumentation'
    ],
    ('IS', 'SY'): [
        'instrumentation_something',
        'soundwaves',
        'instrument technology'
    ],
    ('IS', 'TY'): [
        'deep instrumentation',
        'Cryptography',
        'final instrumentation'
    ]
}



col1,col2 = st.columns(2)
with col1 :
    st.selectbox('Enter Year :',['FY', 'SY', 'TY'],key='year')
with col2 :
    st.selectbox('Enter Branch :',['AIML','IS'],key='branch')

with col1 :
    st.selectbox(
        "Subject :",
        subjects[(st.session_state['branch'], st.session_state['year'])],key='subject')
with col2 :
    st.selectbox('Enter Exam :',['UT1', 'UT2', 'SEM'],key='exam')

if st.button('Load Students') :
    sel_year = st.session_state['year']
    sel_branch = st.session_state['branch']
    sel_sub = st.session_state['subject']
    sel_exam = st.session_state['exam']
    df = display_table(sel_year,sel_branch,sel_sub,sel_exam)

    edited_df = st.data_editor(df)

