import streamlit as st

st.title("Update Student Record !")

'Update single student record ! '

slt_dept = st.selectbox('Select Department : ', ['Artificial Intelligence and Machine Learning',
                                                 'Instrumentation Enggineering'])
enrl_num_for_update =st.text_input('Enter Enrollment Number :',width= 300)

to_update = st.checkbox('Select what to update :'['Enrollment Number','Name',''])
