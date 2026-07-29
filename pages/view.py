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

# st.set_page_config(layout = 'wide')
AIML, IS = st.columns(2)

with AIML :
    with st.expander('Artificial Intelligence and Machine Learning') :
        col1, col2 = st.columns(2)

        with col1:
            st.write("STUDENT DETAILS :")
            if st.button(" FY ") :
                show_aiml_fy()
            if st.button(" SY ") :
                    show_aiml_sy()
            if st.button(" TY ") :
                show_aiml_ty()

        with col2 :
            st.write("UNIT TEST MARKS")
            st.button("FY") 
                # show_aiml_ut_fy()
            st.button("SY")
                # show_aiml_ut_sy()
            st.button("TY")
                # show_aiml_ut_ty()

                

with IS :
    with st.expander('Instrumentation Enggineering') :

        if st.button(" View IS-FY  ") :
                show_aiml_fy()
        if st.button(" View IS-SY  ") :
            show_is_sy()

        if st.button(" View IS-TY  ") :
            show_is_ty()
        

# st.snow()