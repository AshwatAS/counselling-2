import streamlit as st
import datetime

st.set_page_config(page_title="Base form",initial_sidebar_state="collapsed",menu_items={
        'Get Help': 'https://www.youtube.com/',
        'Report a bug': "https://www.youtube.com/",
        'About': "# This is a header. This is an *extremely* cool app!"})


st.title('Counselling App')

st.info('Form 1')

#initialisation of variables
progress_bar_val=0
today_date=datetime.date.today()
user_age=0

#making the variable accessible in all pages
if progress_bar_val not in st.session_state:
    st.session_state.progress_bar_val = 1

#The form with all the inputs
with st.form("user_base_form"):
        user_name=st.text_input("Enter your name: ",placeholder="Ex: Patrick Junes")
#user_age=st.number_input("Enter your age: ",min_value=15,step=1)
        user_DOB = st.date_input("When's your birthday",format="DD.MM.YYYY",min_value=datetime.date(today_date.year-23,1,1),max_value=datetime.date(today_date.year-14,12,31))
        submit_button_bool=st.form_submit_button("Next",type="primary")

#Logic to calculate age of the user
if today_date.month<user_DOB.month:
        user_age=today_date.year-user_DOB.year-1
elif today_date.month>user_DOB.month:
        user_age=today_date.year-user_DOB.year
else:
        if user_DOB.day<=today_date.day:
                user_age=today_date.year-user_DOB.year
        else:
                user_age=today_date.year-user_DOB.year-1

#making the variable accessible in all pages
if user_age not in st.session_state:
        st.session_state.user_age=user_age


if submit_button_bool:
  progress_bar_val+=1
  st.switch_page("pages/page1.py")

#updating progress bar
st.progress(progress_bar_val*20,f"Step {progress_bar_val + 1} of 5")
