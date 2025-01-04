import streamlit as st

st.title('Counselling App')

st.info('Form 1')

progress_bar_val=-1

with st.form("user_base_form"):
  user_name=st.text_input("Enter your name: ")
  user_age=st.number_input("Enter your age: ",min_value=15,step=1)
  submit_button_bool=st.form_submit_button("Next")
  
if submit_button_bool:
  progress_bar_val+=1
  
st.progress(progress_bar_val,"Step ")
