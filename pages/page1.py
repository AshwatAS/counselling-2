import streamlit as st
import pandas as pd
import numpy as np

#Page configuration
#st.set_page_config(page_title="Second form")

#Accessing the variables from base form
progress_bar_val = st.session_state.progress_bar_val
user_age=st.session_state.user_age

# Title and Introduction
st.title('Your Registration is successful. Welcome to CounselDirect')

#testing
#st.write(user_age)

# User Inputs
st.subheader("Now you are ready for Assesment, Please click Submit for answering some of the assessment questions.")
# back_button_bool=st.button("Back",on_click=st.switch_page("streamlit_app.py"))

#the submit button
submit_button_bool=st.button("Submit",type="primary")

if submit_button_bool:       
          progress_bar_val+=1
          st.switch_page("pages/page2.py")

#updating progress bar
st.progress(progress_bar_val*20,f"Step {progress_bar_val + 1} of 5")
