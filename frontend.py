import streamlit as st

# Set Page Configurations
st.set_page_config(page_title="Anushka Tyagi - Portfolio", layout="centered")

# Header Section
st.markdown(
    """
    <style>
        .header-section {
            background: linear-gradient(to right, #0073e6, #00c6ff);
            color: white;
            text-align: center;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
    <div class="header-section">
        <h1>Anushka Tyagi</h1>
        <p>Aspiring Software Development Engineer | AI & ML Enthusiast</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Navigation Bar
sections = ["About", "Skills", "Projects", "Achievements", "Contact"]
section_links = {section: f"#{section.lower()}" for section in sections}
st.markdown(
    """
    <style>
        .nav-bar {
            background-color: #f4f4f9;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .nav-bar a {
            margin: 0 15px;
            font-weight: bold;
            color: #333;
            text-decoration: none;
            font-size: 1.1rem;
        }
        .nav-bar a:hover {
            color: #0073e6;
            text-decoration: underline;
        }
    </style>
    <div class="nav-bar">
        """ + " | ".join([f'<a href="#{section.lower()}">{section}</a>' for section in sections]) + """
    </div>
    """,
    unsafe_allow_html=True
)

# About Me Section
st.header("About Me", anchor="about")
st.write(
    "I am a final-year Computer Science student specializing in Artificial Intelligence and Machine Learning. With a strong foundation in Python, MySQL, and project development, I aim to leverage my technical expertise and problem-solving skills to create impactful and innovative solutions."
)

# Skills Section
st.header("Technical Skills", anchor="skills")
st.markdown(
    """
    - **Programming Languages:** Python, Java, SQL
    - **Databases:** MySQL
    - **Tools & Libraries:** TensorFlow, OpenCV, scikit-learn
    - **Development Skills:** API Integration, Web Development Basics
    - **Other Skills:** Problem Solving, Data Analysis, Team Collaboration
    """
)

# Projects Section
st.header("Projects", anchor="projects")
st.markdown(
    """
    - **Vigilant Vision – Real-Time Conflict Detection System:** Designed a computer vision system to detect physical altercations in video streams using deep learning. Future scope includes weapon detection.
    - **AI-Powered Chatbot for Museum Booking:** Built a chatbot to streamline the museum booking process for users with API integration.
    - **Feature Extraction Model:** Developed a machine learning model for feature extraction and classification tasks in image data.
    """
)

# Achievements Section
st.header("Achievements", anchor="achievements")
st.markdown(
    """
    - **Hackathon Finalist:** Reached the finals in the Smart India Hackathon (SIH) and Amazon ML Hackathon.
    - **Sports:** Silver Medal in Badminton (Zonals, Second Year).
    """
)

# Contact Section
st.header("Contact Me", anchor="contact")
st.markdown(
    """
    - **Email:** [anushka.tyagi53@gmail.com](mailto:anushka.tyagi53@gmail.com)
    - **LinkedIn:** [https://www.linkedin.com/in/tyagianushka/](https://www.linkedin.com/in/tyagianushka/)
    - **GitHub:** [https://github.com/anushka0505](https://github.com/anushka0505)
    """
)

# Footer
st.markdown(
    """
    <style>
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 10px 0;
            background-color: #0073e6;
            color: white;
            border-radius: 10px;
        }
    </style>
    <div class="footer">
        <p>&copy; 2025 Anushka Tyagi. All Rights Reserved. Built with ❤️ in Streamlit.</p>
    </div>
    """,
    unsafe_allow_html=True
)
