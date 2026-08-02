import streamlit as st
from db import get_connection

st.title("Update Student Record")

if st.session_state.get("status") == "success" :
    st.success('Student Record Updated !')
    del st.session_state['status']
    st.session_state.step = 1
if st.session_state.get('status')== 'failure' :
    st.error("Enrollment number not found.")
    del st.session_state['status']
    st.session_state.step = 1


if "step" not in st.session_state :
    st.session_state.step = 1
if "to_update" not in st.session_state:
    st.session_state.to_update = []

# ---------------- STEP 1 ----------------
if st.session_state.step == 1:

    dept = st.selectbox(
        "Select Department",
        [
            "Artificial Intelligence and Machine Learning",
            "Instrumentation Enggineering"
        ]

    )

    year = st.selectbox(
        "Select Year",
        ["FY", "SY", "TY"],
    )

    enrl_num = st.text_input(
        "Enter Enrollment Number"
    )

    selected = st.multiselect(
        "Select what to update",
        ["Enrollment Number", "Name", "Email", "Phone"]
    )

    if st.button("Proceed"):
        st.session_state.selected = selected
        st.session_state.dept = dept
        st.session_state.enrl_num = enrl_num
        st.session_state.year = year

        st.session_state.step = 2
        st.rerun()


# ---------------- STEP 2 ----------------
if st.session_state.step == 2:

    to_update = st.session_state.selected
    slt_dept = st.session_state.dept
    enrl_num_for_update = st.session_state.enrl_num
    slt_year = st.session_state.year
    # st.write(to_update)

    if "Enrollment Number" in to_update:
        st.text_input(
            "Enter New Enrollment No.",
            key="upd_rolln"
        )

    if "Name" in to_update:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.text_input("First Name", key="fname")

        with col2:
            st.text_input("Middle Name", key="mname")

        with col3:
            st.text_input("Last Name", key="lname")

    if "Email" in to_update:
        st.text_input("Email", key="email")

    if "Phone" in to_update:
        st.number_input("Phone", key="phone")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Back"):
            st.session_state.step = 1
            st.rerun()
    # st.write(to_update)
    with col2:
        btn = st.button("Update Record")
        
    if btn :
        # st.write(to_update)

        updates = {}

        if "Enrollment Number" in to_update:
            updates["ENRLNO"] = st.session_state.upd_rolln

        if "Name" in to_update:
            updates["FIRST_NAME"] = st.session_state.fname
            updates["MIDDLE_NAME"] = st.session_state.mname
            updates["LAST_NAME"] = st.session_state.lname

        if "Email" in to_update:
            updates["EMAIL"] = st.session_state.email

        if "Phone" in to_update:
            updates["PHONE"] = st.session_state.phone

        slt_dept_map = {
                "Artificial Intelligence and Machine Learning": "AIML_STUDENTS_",
                "Instrumentation Enggineering": "IS_STUDENTS_"
            }

        table = (
                f"{slt_dept_map[slt_dept]}"
                f"{slt_year}"
            )

            # Build: EMAIL = :EMAIL, PHONE = :PHONE, ...
        set_clause = ", ".join(
                [f"{col} = :{col}" for col in updates.keys()]
            )

        query = f"""
                UPDATE {table}
                SET {set_clause}
                WHERE ENRLNO = :OLD_ENRLNO
            """

            # Bind values
        bind_vars = updates.copy()
        bind_vars["OLD_ENRLNO"] = enrl_num_for_update

        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, bind_vars)

                if cursor.rowcount == 0:
                    connection.rollback()
                    st.session_state["status"] = 'failure'
                    st.rerun()
                else:
                    connection.commit()
                    st.session_state["status"] = "success"
                    st.rerun()

        except Exception as e:
            connection.rollback()
            st.error(f"Error: {e}")


