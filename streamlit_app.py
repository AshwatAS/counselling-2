import streamlit as st

st.title('Counselling App')

st.info('Form 1')
user_name=st.text_input("Enter your name: ")
user_age=st.number_input("Enter your age: ",min_value=15,step=1)
