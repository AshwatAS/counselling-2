import streamlit as st
import datetime
import requests
st.set_page_config(page_title="Base form",initial_sidebar_state="collapsed",menu_items={
        'Get Help': 'https://www.youtube.com/',
        'Report a bug': "https://www.youtube.com/",
        'About': "# This is a header. This is an *extremely* cool app!"})

#Code for API of Indian Cities
#Github URL for accessing all cities in India
url = "https://gist.githubusercontent.com/anubhavshrimal/4aeb195a743d0cdd1c3806c9c222ed45/raw/181a34db4fcb8b37533b7c8b9c489b6c01573158/Indian_Cities_In_States_JSON"

try:
    # Fetch the data
        response = requests.get(url)    
    # Parse the JSON data
        data = response.json()
        #list for all indian cities
        all_cities = [city for cities in data.values() for city in cities]
except:
        st.info(f"An error occurred")


st.title('Counselling App')

st.info('Form 1')

#initialisation of important variables
progress_bar_val=0
today_date=datetime.date.today()
user_age=0

#making the variable accessible in all pages
if progress_bar_val not in st.session_state:
    st.session_state.progress_bar_val = 1

#All the inputs taken from the user
user_name=st.text_input("Enter your name: ",placeholder="Ex: Patrick Junes")
user_city=st.selectbox("Which city are you studying in?",all_cities,None)
user_gender = st.selectbox("What is your gender?", ["Male","Female"],None)
user_DOB = st.date_input("When's your birthday",format="DD.MM.YYYY",min_value=datetime.date(today_date.year-23,1,1),max_value=datetime.date(today_date.year-14,12,31))
user_category=st.selectbox("Which category are you from?",["SC","OBC","ST","General"],None)
user_father_qualification=st.selectbox("What is your father's qualification?",["CA","IIT","MBA","MBBS","IPS","IAS"],None)
user_mother_qualification=st.selectbox("What is your mother's qualification?",["CA","IIT","MBA","MBBS","IPS","IAS"],None)

#EB=education board, SOE=Status of Education,EY=education year
user_soe=st.selectbox("What is your current year of education?",["Secondary","Higher Secondary","Undergraduate"],None)
if user_soe=="Secondary":
        user_ey=st.selectbox("Which grade?",["9th","10th"])
        user_eb=st.selectbox("What is your board of education?",["ICSE","CBSE","International","SSC","Others"],None)
elif user_soe=="Higher Secondary":
        user_ey=st.selectbox("Which grade?",["11th","12th"])
        user_eb=st.selectbox("Which exam are you currently preparing/appearing for?",["IB Diploma","A-Levels","JEE Mains","BITSAT","Others"],None)
elif user_soe=="Undergraduate":
        user_ey=st.selectbox("Which year?",["1st year","2nd year","3rd year","4th year"])
#A fake value initialised because undergraduates do not have an education board
        user_eb="None"
        
#the submit button
submit_button_bool=st.button("Next",type="primary")

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
        if not user_name or not user_gender or not user_soe or not user_eb:
                st.error("Please fill in all required fields.")
        else:       
          progress_bar_val+=1
          st.switch_page("pages/page1.py")

#updating progress bar
st.progress(progress_bar_val*20,f"Step {progress_bar_val + 1} of 5")
