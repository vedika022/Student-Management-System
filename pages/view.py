import streamlit as st
from home import connection
import pandas as pd



@st.dialog("AIML - FY !", width="large")
def show_aiml_fy():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM AIML_STUDENTS_FY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)

@st.dialog("AIML - SY !", width="large")
def show_aiml_sy():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM AIML_STUDENTS_SY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)

@st.dialog("AIML - TY !", width="large")
def show_aiml_ty():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM AIML_STUDENTS_TY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)

@st.dialog("IS - FY !", width="large")
def show_is_fy():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM IS_STUDENTS_FY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)

@st.dialog("IS - SY !", width="large")
def show_is_sy():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM IS_STUDENTS_sY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)

@st.dialog("IS - TY !", width="large")
def show_is_ty():
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM IS_STUDENTS_TY')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)


st.title("Academic Dashboard")
st.caption("Manage student details and marks")



AIML, IE = st.columns(2)




with AIML:
    with st.container(border=True):

        st.subheader("Artificial Intelligence & Machine Learning")
        st.write("Manage student information and marks.")

        col1, col2 = st.columns(2)


        with col1:

            st.markdown("Student Details")

            tabs = st.tabs(["FY", "SY", "TY"])

            with tabs[0]:
                if st.button(
                    "View FY Students",
                    key="aiml_fy_students",
                    use_container_width=True
                ):
                    show_aiml_fy()

            with tabs[1]:
                if st.button(
                    "View SY Students",
                    key="aiml_sy_students",
                    use_container_width=True
                ):
                    show_aiml_sy()

            with tabs[2]:
                if st.button(
                    "View TY Students",
                    key="aiml_ty_students",
                    use_container_width=True
                ):
                    show_aiml_ty()



        with col2:

            st.markdown("Unit Test Marks")

            tabs = st.tabs(["FY", "SY", "TY"])

            with tabs[0]:
                st.button(
                    "View FY Marks",
                    key="aiml_fy_marks",
                    use_container_width=True
                )
                    # show_aiml_ut_fy()

            with tabs[1]:
                st.button(
                    "View SY Marks",
                    key="aiml_sy_marks",
                    use_container_width=True
                )
                    # show_aiml_ut_sy()

            with tabs[2]:
                st.button(
                   "View TY Marks",
                    key="aiml_ty_marks",
                    use_container_width=True
                )
                    # show_aiml_ut_ty()



with IE:
    with st.container(border=True):

        st.subheader("Instrumentation Engineering")
        st.write("Manage student information and unit test marks.")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("Student Details")

            tabs = st.tabs(["FY", "SY", "TY"])

            with tabs[0]:
                if st.button(
                    "View FY Students",
                    key="is_fy_students",
                    use_container_width=True
                ):
                    show_is_fy()

            with tabs[1]:
                if st.button(
                    "View SY Students",
                    key="is_sy_students",
                    use_container_width=True
                ):
                    show_is_sy()

            with tabs[2]:
                if st.button(
                    "View TY Students",
                    key="is_ty_students",
                    use_container_width=True
                ) :
                    show_is_ty()


        with col2:

            st.markdown("Marks")

            tabs = st.tabs(["FY", "SY", "TY"])

            with tabs[0]:
                st.button(
                    "View FY Marks",
                    key="is_fy_marks",
                    use_container_width=True
                )
                    # show_is_ut_fy()

            with tabs[1]:
                st.button(
                    "View SY Marks",
                    key="is_sy_marks",
                    use_container_width=True
                )
                    # show_is_ut_sy()

            with tabs[2]:
                st.button(
                    "View TY Marks",
                    key="is_ty_marks",
                    use_container_width=True
                )
                    # show_is_ut_ty()

# st.snow()