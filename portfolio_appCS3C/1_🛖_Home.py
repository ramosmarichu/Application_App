import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="😊", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e3a8a, #1e1e1e);
        color: #e0f2fe;
    }

    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #0ea5e9);
        color: white;
        border-radius: 10px;
        border: none;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "page" not in st.session_state:
    st.session_state.page = "Home"

st.write("### Navigate")

col1, col2, col3, col4, col5 = st.columns(5)

if col1.button("Home"):
    st.session_state.page = "Home"
if col2.button("Skills"):
    st.session_state.page = "Skills"
if col3.button("About"):
    st.session_state.page = "About"
if col4.button("Projects"):
    st.session_state.page = "Projects"
if col5.button("Contact"):
    st.session_state.page = "Contact"

st.divider()

page = st.session_state.page

if page == "Home":
    st.title("😊 Welcome to My Portfolio")
    st.header("Hi, I'm Marichu Ramos")
    st.write("Aspiring Developer | Designer")

    st.image("Ramos_Marichu.jpeg",caption="Be Passionate", width=300)

    st.info("Welcome to my portfolio! Explore my work and skills.")

elif page == "Skills":
    st.title("🛠️ Skills")

    st.write("Python")
    st.progress(80)

    st.write("JavaScript")
    st.progress(70)

    st.write("PHP")
    st.progress(75)

    st.write("Canva / UI Design")
    st.progress(85)

elif page == "About":
    st.title("👩🏻‍💻 About Me")
    st.write("""
    I am a passionate developer who enjoys creating systems and applications.
    I love solving problems and building user-friendly designs.
    """)

    st.subheader("Education")
    st.write("- BS Computer Science")
    st.write("- Trainings in Web Development & Design")

    st.subheader("Goals")
    st.write("- Become a Full Stack Developer")
    st.write("- Build impactful tech solutions")

elif page == "Projects":
    st.title("📂 Projects")
    st.write("Coming soon... 🚀")

elif page == "Contact":
    st.title("📞 Contact Me")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        if name and email and message:
            st.success("Message sent successfully! ✅")
        else:
            st.error("Please fill all fields.")
