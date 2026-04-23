import streamlit as st 
st.set_page_config(page_title="About Me", page_icon="👩🏻‍💻")

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
st.title("👩🏻‍💻 About Me") 
st.write(""" 
I am a passionate developer who enjoys creating systems and applications. I love solving problems and building user-friendly designs. """) 
st.subheader(" Education") 
st.write("- BS Computer Science") 
st.write("- Trainings in Web Development & Design") 
st.subheader(" Goals") 
st.write("- Become a Full Stack Developer") 
st.write("- Build impactful tech solutions") 