import streamlit as st
from home import connection
import pandas as pd

@st.dialog("AIML - FY !")
def show_aiml_fy():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM AIML_STUDENTS_FY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)

@st.dialog("AIML - SY !")
def show_aiml_sy():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM AIML_STUDENTS_SY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)

@st.dialog("AIML - TY !")
def show_aiml_ty():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM AIML_STUDENTS_TY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)

@st.dialog("IS - FY !")
def show_is_fy():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM IS_STUDENTS_FY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)

@st.dialog("IS - SY !")
def show_is_sy():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM IS_STUDENTS_sY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)

@st.dialog("IS - TY !")
def show_is_ty():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM IS_STUDENTS_TY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)

fy,sy,ty = st.columns(3)

with fy :

    if st.button(" View AIML-FY  ") :
        show_aiml_fy()

    if st.button(" View IS-FY  ") :
        show_aiml_fy()

with sy :

    if st.button(" View AIML-SY  ") :
        show_aiml_sy()

    if st.button(" View IS-SY  ") :
        show_is_sy()

with ty :

    if st.button(" View AIML-TY  ") :
        show_aiml_ty()

    if st.button(" View IS-TY  ") :
        show_is_ty()
        

# st.snow()