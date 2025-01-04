import streamlit as st

st.set_page_config(page_title="Base form",menu_items={
        'Get Help': 'https://www.youtube.com/',
        'Report a bug': "https://www.youtube.com/",
        'About': "# This is a header. This is an *extremely* cool app!"})



st.title('Counselling App')

st.info('Form 1')

progress_bar_val=0

with st.form("user_base_form"):
  user_name=st.text_input("Enter your name: ")
  user_age=st.number_input("Enter your age: ",min_value=15,step=1)
  submit_button_bool=st.form_submit_button("Next",type="primary")
  
if submit_button_bool:
  progress_bar_val+=1
  st.switch_page("pages/page1.py")
  
st.progress(progress_bar_val*20,f"Step {progress_bar_val + 1} of 5")
