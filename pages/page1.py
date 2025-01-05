import streamlit as st
import pandas as pd
import numpy as np

#Page configuration
#st.set_page_config(page_title="Second form")

#Accessing the variables from base form
progress_bar_val = st.session_state.progress_bar_val
user_age=st.session_state.user_age

# Title and Introduction
st.title('Hello! Welcome to Career Compass')
st.info("We help you decide what you should study in the future with the help of our large datasets and accurate algorithms.")

st.write(user_age)

# User Inputs
st.subheader("Try and answer as accurately as possible! These questions are helping you, not deciding your future.")
preferred_environment = st.selectbox(
    "What is your preferred work environment?",
    ["Teaching and Training", "Remote/Work from Home", "On-site Industrial Work", 
     "Desk Job", "Fieldwork", "Research Lab", "Creative Studio"]
)
# salary_expect = st.slider("How much annual income do you expect from your job in the future? (INR)", 400000, 1250000, step=50000)
# time_filter = st.slider("Maximum Years to Land a Job", 3, 8, step=1)

# Options Lists
hobbies = ["Astronomy", "Bird Watching", "Board Games", "Calligraphy", "Cooking", "Cycling", 
           "Dance", "Drawing", "Fishing", "Gardening", "Hiking", "Knitting", "Music Composition", 
           "Origami", "Painting", "Photography", "Pottery", "Reading", "Sculpting", 
           "Woodworking", "Writing"]

soft_skills = ["Adaptability", "Attention to Detail", "Collaboration", "Communication", 
               "Conflict Resolution", "Creativity", "Critical Thinking", "Decision Making", 
               "Empathy", "Interpersonal Skills", "Leadership", "Negotiation", 
               "Problem-Solving", "Public Speaking", "Resilience", "Self-Motivation", 
               "Stress Management", "Teamwork", "Time Management", "Work Ethic"]

technical_skills = ["AR/VR Development", "Blockchain Development", "C++", "Cloud Computing", 
                    "Content Writing", "Cybersecurity", "Data Analysis", "Database Management", 
                    "Digital Marketing", "Game Design", "Graphic Design", "Java", "Machine Learning", 
                    "Mobile App Development", "Network Administration", "Python", "SEO", 
                    "Social Media Management", "UI/UX Design", "Web Development"]

passion_areas = ["Automobiles", "Business Strategy", "Creative Arts", "Education", 
                 "Entrepreneurship", "Environmental Conservation", "Fashion", "Film & Media", 
                 "Fitness & Wellness", "Food & Culinary Arts", "Gaming", "Healthcare", 
                 "History & Culture", "Politics", "Science & Research", "Social Work", 
                 "Space Exploration", "Sports", "Technology", "Travel"]

subjects = ["Accounting", "Anthropology", "Archaeology", "Architecture", "Art", "Biology", 
            "Business Studies", "Chemistry", "Computer Science", "Data Science", "Economics", 
            "Engineering", "English", "Environmental Science", "Ethics", "Geography", 
            "History", "Law", "Linguistics", "Literature", "Mathematics", "Media Studies", 
            "Medicine", "Music", "Nursing", "Pharmacology", "Philosophy", "Physical Education", 
            "Physics", "Political Science", "Psychology", "Public Health", "Sociology", 
            "Sports Science", "Statistics", "Theology", "Veterinary Science"]

# Multi-Select Inputs
selected_hobbies = st.multiselect("Select one or more hobbies:", hobbies)
selected_soft_skills = st.multiselect("Select one or more skills:", soft_skills)
selected_technical_skills = st.multiselect("Select one or more technical skills:", technical_skills)
selected_passion_areas = st.multiselect("Select one or more passion areas:", passion_areas)
selected_subjects = st.multiselect("Select the subjects you are good at:", subjects)

# Capture grades for selected subjects
grades = {}
for subject in selected_subjects:
    grades[subject] = st.slider(f"What was your percentage in {subject}?", 1, 100, step=1)

st.progress(progress_bar_val*20,f"Step {progress_bar_val + 1} of 5")
