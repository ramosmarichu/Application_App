import streamlit as st

st.set_page_config(page_title="Contact Me", page_icon="📞")

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

st.title("📞Contact Me")

name = st.text_input("Name") 
email = st.text_input("Email") 
message = st.text_area("Message") 
if st.button("Send"): 
    if name and email and message: 
        st.success("Message sent successfully! ✅") 
else: 
    st.error("Please fill all fields.") 
st.markdown("🌐 Social Links") 
st.write("- GitHub:https://github.com/ramosmarichu") 
st.write("- Facebook:https://www.facebook.com/Jhud.ramos1205 ")
