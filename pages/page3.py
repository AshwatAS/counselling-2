import streamlit as st
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

subjects = ["Accounting","Anthropology", "Archaeology", "Architecture", "Art", "Biology", 
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
# back_button_bool=st.button("Back",on_click=st.switch_page("streamlit_app.py"))
