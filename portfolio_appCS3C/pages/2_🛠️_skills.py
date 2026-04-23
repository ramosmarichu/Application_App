import streamlit as st
st.set_page_config(page_title="Skills", page_icon="🛠️")
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

st.subheader(" Programming") 
st.progress(80) 
st.write("Python") 
st.progress(70) 
st.write("JavaScript") 
st.progress(75) 
st.write("PHP") 
st.subheader(" Design") 
st.progress(85) 
st.write("Canva / UI Design") 
st.subheader(" Tools") 
st.write("- GitHub") 
st.write("- VS Code") 
st.write("- Streamlit")
