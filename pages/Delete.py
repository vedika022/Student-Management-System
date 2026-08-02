import streamlit as st
from db import get_connection

st.header('Delete Student Data :')
'Will delete student data permanently !'

if st.session_state.get('status') == 'success' :
    st.success("Deleted student record !")
    del st.session_state['status']

elif st.session_state.get('status') == 'failure' :
    st.error("Enrollment number doesnt exist.")
    del st.session_state['status']


dept = st.selectbox("Select Department",["Artificial Intelligence and Machine Learning","Instrumentation Enggineering"])

year = st.selectbox("Select Year",["FY", "SY", "TY"],)

enrl_num = st.text_input("Enter Enrollment Number")

if "show_confirm" not in st.session_state:
    st.session_state.show_confirm = False

@st.dialog("Confirm Delete")
def confirm_delete():
    st.write("Are you sure you want to permanently delete this item?")

    col1, col2 = st.columns(2)

    with col1:
        confirm = st.button("Yes")

    if confirm :

            dept_map = {
                            "Artificial Intelligence and Machine Learning": "AIML_STUDENTS_",
                            "Instrumentation Enggineering": "IS_STUDENTS_"
                        }

            table = (
                            f"{dept_map[dept]}"
                            f"{year}"
                        )
            connection = get_connection()
            with connection.cursor() as cursor :
                try :
                    # cursor.execute(F'DELETE FROM {table} where ENRLNO = {enrl_num}')
                    cursor.execute(f"DELETE FROM {table} WHERE ENRLNO = :1",
                            [enrl_num])
                    connection.commit()

                    if cursor.rowcount == 0:
                        connection.rollback()
                        st.session_state.show_confirm = False
                        st.session_state["status"] = 'failure'
                        st.rerun()
                    else:
                        connection.commit()
                        st.session_state.show_confirm = False
                        st.session_state["status"] = "success"
                        st.rerun()
                    
                except Exception as e:
                    connection.rollback()
                    st.error(f"Error: {e}")


    with col2:
        if st.button("No"):
            st.session_state.show_confirm = False
            st.rerun()

if st.button('Delete Record') :
    confirm_delete()

    
