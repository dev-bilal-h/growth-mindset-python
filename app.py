import streamlit as st
import sqlite3
from PIL import Image
import time
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import sqlite3

# Set page configuration
st.set_page_config(
    page_title="Growth Mindset",
    page_icon="💡",
    layout="centered",
)


# Custom CSS for animations
st.markdown(
    """
    <style>
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .animated {
            animation: fadeInUp 1s ease-in-out;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize SQLite database
conn = sqlite3.connect("growth_mindset.db")
c = conn.cursor()

# Create tables if they don't exist
c.execute(
    """CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)"""
)
c.execute(
    """CREATE TABLE IF NOT EXISTS progress
             (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, progress INTEGER, date TEXT)"""
)
c.execute(
    """CREATE TABLE IF NOT EXISTS reflections
             (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, reflection TEXT, date TEXT)"""
)
c.execute(
    """CREATE TABLE IF NOT EXISTS habits
             (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, habit TEXT, date TEXT)"""
)
conn.commit()

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Daily Inspiration",
        "Daily Progress",
        "Sign Up",
        "Login",
    ],
)

# Developer Info Section at the Bottom
st.sidebar.markdown("---")  # Separator line
st.sidebar.markdown(
    """
    ### 🖥️ Developer Info  
    - 🛠️ **Created by:** Bilal Hassan
    - 📧 **Get in Touch:** [Send Email](mailto:siddiquibilal882@gmail.com)  
    - 🌐 **Website:** [My Portfolio](https://portfolio-tailwind-css-bh.vercel.app/)  
    """,
    unsafe_allow_html=True,
)


# User Authentication
def login(username, password):
    c.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?", (username, password)
    )
    return c.fetchone()


def sign_up(username, password):
    c.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
    )
    conn.commit()


if page == "Home":
    st.markdown(
        "<h1 class='animated' style='color: red;'>Step into the Growth Mindset Challenge 💡</h1>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])

    # Content Section
    with col1:
        st.markdown(
            """
        <div class='animated'>
            <h3 style='color: #20C997;'>Understanding a Growth Mindset</h3>
            <p>A growth mindset is about believing that skills and intelligence can improve with effort, practice, and learning from experiences. 
            This idea, introduced by psychologist Carol Dweck, encourages us to see challenges as opportunities rather than barriers.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
    <div class='animated'>
        <h3 style='color: #20C997;'>Why Cultivate a Growth Mindset?</h3>
        <ul>
            <li><b>Face Challenges Positively:</b> Every obstacle is a chance to grow.</li>
            <li><b>Turn Mistakes into Lessons:</b> Failure is just another step toward success.</li>
            <li><b>Stay Determined:</b> Hard work and consistency lead to personal development.</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class='animated'>
        <h3 style='color: #20C997;'>Ways to Develop a Growth Mindset</h3>
        <ul>
            <li><b>Set Skill-Based Goals:</b> Aim to improve rather than just achieve.</li>
            <li><b>Reflect & Adapt:</b> Learn from both victories and setbacks.</li>
            <li><b>Seek Constructive Feedback:</b> Use advice to enhance your abilities.</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class='animated'>
        <p>Embracing a growth mindset helps you break limits, push boundaries, and unlock new possibilities. 
        Progress is a journey, and every step forward brings you closer to excellence.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )


    # Image Section
    with col2:
        with st.spinner("Loading image..."):
            time.sleep(1)
            try:
                image = Image.open("home-img.png")
                st.image(
                    image,
                    caption="Step into a mindset of growth!",
                    use_container_width=True,
                )
            except FileNotFoundError:
                st.error("Image not found. Ensure the correct file path.")



# Daily Inspiration Page
if page == "Daily Inspiration":
    # custom CSS to ensure the heading stays visible
    st.markdown(
        """
        <style>
        .stHeadingContainer {
            position: sticky;
            top: 0;
            background-color: white;
            z-index: 1000;
            padding: 10px 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    # Add content to the first column
    with col1:
        st.markdown(
            "<h1 style='color: red;'>💡 Daily Inspiration</h1>",
            unsafe_allow_html=True,
        )

    # Motivational Quotes
    quotes = [
        "🌱 Every challenge is an opportunity to grow!",
        "💪 Strength comes from consistency!",
        "🔥 Push forward, success is near!",
        "🚀 Elevate yourself daily with learning!",
        "🌟 Small steps lead to big achievements!",
    ]

    # Add content to the second column
    with col2:
        st.subheader(" Today's Thought 🔥")
        st.info(random.choice(quotes))

    # Learning Goal
    goal = st.text_area("What's your current learning goal?")

    # Achieved Goal Date
    achieved_date = st.date_input("Target Completion Date:")
    if achieved_date:
        st.success(
            f"🎯 Keep it up! You're aiming to complete this by **{achieved_date}**. "
        )

    # Growth Mindset Tips
    tips = st.radio(
        "Pick a tip to boost your mindset:",
        [
            "🚀 Keep pushing forward, consistency is key!",
            "🔄 Mistakes help you grow – embrace them!",
            "💬 Feedback is a tool for improvement, use it wisely.",
            "🏋️ Challenge yourself beyond limits every day!",
            "🧠 Effort makes your brain stronger and sharper!",
        ],
    )
    st.success(f"**Tip Selected:** {tips}")

    # Feedback on Progress
    feedback = st.selectbox(
        "How do you feel about your progress?",
        ["On top of the world!", "Making steady progress", "Need a little push"],
    )
    st.write(f"💬 **Your Reflection:** {feedback}")

    # Celebration Button
    celebrate = st.button("Celebrate Small Wins!")
    if celebrate:
        st.balloons()
    st.success("Remember, every step forward is a step toward success! 🚀")

    # Function to generate PDF
    def generate_pdf(goal, achieved_date, tips, feedback):
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)
        pdf.setTitle("Mindset Growth Tracker")

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(200, 750, "🚀 Personal Growth Progress 🌟")

        pdf.setFont("Helvetica", 12)
        pdf.drawString(100, 700, f"Goal: {goal}")
        pdf.drawString(100, 670, f"Target Date: {achieved_date}")  # Fixed
        pdf.drawString(100, 640, f"Mindset Tip: {tips}")  # Fixed
        pdf.drawString(100, 610, f"Self-Reflection: {feedback}")


        pdf.drawString(100, 570, "💡 Keep pushing forward and embracing growth!")

        pdf.save()
        buffer.seek(0)
        return buffer

    # Download PDF Button
    if st.button("📩 Save Your Progress as PDF"):
        if goal and achieved_date:
            pdf_file = generate_pdf(goal, achieved_date, tips, feedback)
            st.download_button(
                label="📥 Download Growth Report",
                data=pdf_file,
                file_name="mindset_growth_report.pdf",
                mime="application/pdf",
            )
        else:
            st.warning("⚠️ Please provide all details before downloading.")


# Daily Tracker
elif page == "Daily Progress":
    # Custom CSS for Slider
 st.markdown(
        "<h1 style='color: red;'>Daily Monitor 📊</h1>",
        unsafe_allow_html=True,
    )   
 st.markdown(
    """
    <style>
    /* Move slider labels (0 and 100) downward */
    .stSlider > div > div > div > div[data-testid="stTickBarMin"], 
    .stSlider > div > div > div > div[data-testid="stTickBarMax"] {
        position: relative;
        top: 10px;  /* Adjust this value to move numbers further down */
    }
    </style>
    """,
    unsafe_allow_html=True
 )


 # Slider for Progress
 progress_value = st.slider("📌 How much did you improve today?", 0, 100, 40)

 # Alternative Visual Progress Bar
 st.progress(progress_value / 100)

 # Button to Save Progress
 if st.button("✅ Log Progress"):
    if "user_id" in st.session_state:
        c.execute(
            'INSERT INTO progress (user_id, progress, date) VALUES (?, ?, DATE("now"))',
            (st.session_state["user_id"], progress_value),
        )
        conn.commit()

        st.success(f"🎯 Your progress has been saved: {progress_value}%")

        # Different Motivational Messages
        if progress_value < 25:
            st.warning("Small steps lead to big changes. Keep going! 💡")
        elif progress_value < 60:
            st.info("You're on the right track! Stay consistent. 🚀")
        else:
            st.success("Fantastic work! You're making remarkable progress! 🎊")
    else:
        st.error("⚠️ Please log in to record your progress.")

 # Close Database Connection
 conn.close()




# Sign Up Page
elif page == "Sign Up":
    st.markdown(
        "<h1 style='color: red;'>Sign Up</h1>",
        unsafe_allow_html=True,
    )
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        sign_up(username, password)
        st.success("You have successfully signed up! Please log in.")


# Login Page
elif page == "Login":
    st.markdown(
        "<h1 style='color: red;'>Log in</h1>",
        unsafe_allow_html=True,
    )
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = login(username, password)
        if user:
            st.session_state["user_id"] = user[0]
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password.")
