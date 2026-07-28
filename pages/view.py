import streamlit as st
from home import connection
import pandas as pd

def view() :
    with connection.cursor() as cursor :
        cursor.execute('SELECT * FROM STUDENTS_AIML_1')    
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)
    return st.dataframe(df)

# st.snow()

st.button(" View Table ", on_click=view )