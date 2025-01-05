import streamlit as st
import datetime

st.set_page_config(page_title="Base form",initial_sidebar_state="collapsed",menu_items={
        'Get Help': 'https://www.youtube.com/',
        'Report a bug': "https://www.youtube.com/",
        'About': "# This is a header. This is an *extremely* cool app!"})


st.title('Counselling App')

st.info('Form 1')

progress_bar_val=0
today_date=datetime.date.today()
st.write(today_date)
if progress_bar_val not in st.session_state:
    st.session_state.progress_bar_val = 1

with st.form("user_base_form"):
  user_name=st.text_input("Enter your name: ",placeholder="Ex: Patrick Junes")
  #user_age=st.number_input("Enter your age: ",min_value=15,step=1)
  user_DOB = st.date_input("When's your birthday",format="DD.MM.YYYY",max_value=datetime.date(1,1,today_date.year-14))
  submit_button_bool=st.form_submit_button("Next",type="primary")
  
if submit_button_bool:
  progress_bar_val+=1
  st.switch_page("pages/page1.py")
  
st.progress(progress_bar_val*20,f"Step {progress_bar_val + 1} of 5")
