import streamlit as st
from app import connection
import oracledb

st.header("Insert *new* student details ")

with st.container(horizontal_alignment='center') :
    option = st.selectbox("Select Department :",['Artificial Intelligence and Machine Learning',
                                                'Instrumentation Enggineering'])


    year = st.selectbox("Select Year :",['First Year','Second Year', 'Third Year'])

    rolln = st.text_input("Enter Enrollment No. :", placeholder="eg. FX23..02",
                                key = 'rolln',width = 'stretch' )
    col1, col2, col3 = st.columns(3)

    with col1 :
        fname = st.text_input('Enter First Name :', placeholder='first name here ..', key = 'fname')
    with col2 :
        mname = st.text_input('Enter Middle Name :', placeholder='middle name here ..', key = 'mname')
    with col3 :
        lname = st.text_input('Enter Last Name :', placeholder='last name here ..', key = 'lname')

    email = st.text_input('Enter Email :', placeholder = 'example@gmail.com',key = 'email')
    phone = st.number_input('Enter Mobile Number :', placeholder = 'eg. 9989......', key = 'phone')
    
def Insert_func() :

    rolln = st.session_state.rolln
    fname = st.session_state.fname

    if not rolln or not fname or not lname :
        st.warning("Please enter both Roll No. and Name.")
        return

    if option == 'Artificial Intelligence and Machine Learning' :
        dept = 'AIML_STUDENTS_' 
    else :
        dept = 'IS_STUDENTS_'

    year_map = {
        "First Year": "FY",
        "Second Year": "SY",
        "Third Year": "TY"
    }

    sel_year = year_map[year]

    with connection.cursor() as cursor :
        try :
            # cursor.execute(f"INSERT INTO STUDENTS_AIML_1 " \
            # "VALUES({rolln},{name})")

            cursor.execute(f"INSERT INTO {dept}{sel_year} VALUES (:1, :2, :3, :4, :5, :6)",
            (rolln, fname, mname, lname, email, phone)
            )

            connection.commit()
            st.success("Student inserted successfully!")
            # Clear input fields
            st.session_state.rolln = ''
            st.session_state.fname = ""
            st.session_state.mname = ""
            st.session_state.lname = ""
            st.session_state.email = ""
            st.session_state.phone = ""
            
            

        except oracledb.Error as e :
            connection.rollback()
            st.error(f"Error inserting student: {e}")


submit_btn = st.button("SUBMIT", on_click=Insert_func)