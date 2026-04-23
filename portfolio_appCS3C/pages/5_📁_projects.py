import streamlit as st
st.set_page_config(page_title="projects", page_icon="📁")
st.markdown(
    """
     <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e3a8a,  #1e1e1e);
        color: #e0f2fe;
    }

    /* Style input fields */
    input, textarea {
        background-color: #0f172a !important;
        color: #e0f2fe !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 8px !important;
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #0ea5e9);
        color: white;
        border-radius: 10px;
        border: none;
    }
    </style>

    """,
    unsafe_allow_html=True
)
st.title("📁My Projects")

projects = { 
 "Boarding House Management System": "Montly payment management.",  "HistoQuiz Web Game": " Promotes history the the locals town.", 
 "TouristSpots Reservation Web app": " Promotes tourist spots in local areas." } 

for name, desc in projects.items(): 
 with st.expander(name): 
    st.write(desc) 