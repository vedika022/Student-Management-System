import oracledb 
import streamlit as st
import pandas as pd

oracledb.init_oracle_client( lib_dir=r"C:\oraclexe\instantclient_23_26")

connection = oracledb.connect(user = 'STUDENTS', password = 'me12', dsn = 'localhost:1521/XE')
if connection :
    st.toast("Connected succesfully !")


    def create_table() :
        with connection.cursor() as cursor :
            try :
                table_name = 'STUDENTS_AIML_1'
                cursor.execute(f"CREATE TABLE {table_name} ( Rollno number(2) Primary Key , Name varchar2(40))")
                st.toast("Created Table ")
                connection.commit()

            except oracledb.DatabaseError as e:
                error, = e.args

            if error.code == 955:
                pass
            else:
                st.error(f"Error: {error.message}")
        return 

    def view() :
        with connection.cursor() as cursor :
            cursor.execute('SELECT * FROM STUDENTS_AIML_1')    
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=columns)
        return st.dataframe(df)
        
st.button(" View Table ", on_click=view )

st.title('Student Managment System !')

