import streamlit as st
import pandas as pd
import numpy as np

#Page configuration
#st.set_page_config(page_title="Second form")

#Accessing the variables from base form
progress_bar_val = st.session_state.progress_bar_val
user_age=st.session_state.user_age

#testing
#st.write(user_age)

# User Inputs
st.subheader("What is your preferred work environment")
preferred_environment = st.radio(
    " ",
    ["Teaching and Training", "Remote/Work from Home", "On-site Industrial Work", 
     "Desk Job", "Fieldwork", "Research Lab", "Creative Studio"],None
)
st.write("You selected:",preferred_environment)

st.progress(progress_bar_val*20,f"Step {progress_bar_val + 1} of 5")
