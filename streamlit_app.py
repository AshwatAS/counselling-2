import streamlit as st
import datetime

st.set_page_config(page_title="Base form",initial_sidebar_state="collapsed",menu_items={
        'Get Help': 'https://www.youtube.com/',
        'Report a bug': "https://www.youtube.com/",
        'About': "# This is a header. This is an *extremely* cool app!"})


st.title('Counselling App')

st.info('Form 1')

#initialisation of important variables
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
        user_gender = st.selectbox("What is your gender?", ["Male","Female","Others"],None)
        user_DOB = st.date_input("When's your birthday",format="DD.MM.YYYY",min_value=datetime.date(today_date.year-23,1,1),max_value=datetime.date(today_date.year-14,12,31))
        
        #EB=education board, SOE=Status of Education,EY=education year
        user_soe=st.selectbox("What is your current year of education?",["Secondary","Higher Secondary","Undergraduate"])
        if user_soe=="Secondary":
                user_ey=st.selectbox("Which grade?",["9th","10th"])
        
        user_eb=st.selectbox("What is your board of education?",["ICSE","CBSE","International","SSC","Others"],None)
        submit_button_bool=st.form_submit_button("Next",type="primary")

#Logic to calculate age of the user
if today_date.month<user_DOB.month:
        user_age=today_date.year-user_DOB.year-1
elif today_date.month>user_DOB.month:
        user_age=today_date.year-user_DOB.year
else:
        if user_DOB.day<=today_date.day:
                user_age=today_date.year-user_DOB.year
        elif user_DOB.day>today_date.day:
                user_age=today_date.year-user_DOB.year-1

#making the variable accessible in all pages
if user_age not in st.session_state:
        st.session_state.user_age=user_age


if submit_button_bool:
        #Checking if all required fields are filled
        if not user_name or not user_gender:
                st.error("Please fill in all required fields.")
        else:       
          progress_bar_val+=1
          st.switch_page("pages/page1.py")

#updating progress bar
st.progress(progress_bar_val*20,f"Step {progress_bar_val + 1} of 5")
