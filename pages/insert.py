import streamlit as st
from home import connection
import oracledb

option = st.selectbox("Select Department :",['AIML','....','...'])

col1, col2 = st.columns(2)

with col1 :
    rolln = st.number_input("Enter Roll No. :", placeholder="eg. 1 ...", min_value=1,max_value=35,
                            key = 'rolln' )

with col2 :
    name = st.text_input('Enter Name :', placeholder='Your name here', key = 'name')

def Insert_func() :

    rolln = st.session_state.rolln
    name = st.session_state.name

    if not rolln or not name:
        st.warning("Please enter both Roll No. and Name.")
        return

    with connection.cursor() as cursor :
        try :
            # cursor.execute(f"INSERT INTO STUDENTS_AIML_1 " \
            # "VALUES({rolln},{name})")

            cursor.execute(
            """
            INSERT INTO STUDENTS_AIML_1
            VALUES (:1, :2)
            """,
            (rolln, name)
            )

            connection.commit()
            st.success("Student inserted successfully!")
            # Clear input fields
            st.session_state.rolln = 0
            st.session_state.name = ""

        except oracledb.Error as e :
            connection.rollback()
            st.error(f"Error inserting student: {e}")


submit_btn = st.button("SUBMIT", on_click=Insert_func)