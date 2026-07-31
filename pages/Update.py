import streamlit as st

st.title("Update Student Record !")

'Update single student record ! '

slt_dept = st.selectbox('Select Department : ', ['Artificial Intelligence and Machine Learning',
                                                 'Instrumentation Enggineering'], key= 'slt_dept')
enrl_num_for_update =st.text_input('Enter Enrollment Number :',width= 300,key='enrl_num_for_update')

to_update = st.multiselect('Select what to update :' ,['Enrollment Number','Name','Email','Phone'],key='to_update')

if st.button("Proceed") :
    