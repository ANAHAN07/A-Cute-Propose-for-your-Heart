import streamlit as st
import random
import time

# Function to play audio from a URL
def play_audio(file_url):
    audio_html = f"""
        <audio autoplay loop>
        <source src="{file_url}" type="audio/mp3">
        </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# Set the page configuration
st.set_page_config(page_title="I 💖 You", page_icon="💍")

# Page Title and Description
st.title("💖 Will You Be My Love? 💖")
st.write("No matter where life takes us, as long as I'm with you, I'll be home.✨✨")
st.image("https://images.unsplash.com/photo-1610936534941-022318669958?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=400)

# Message asking for proposal
st.write("Hey love! You mean the world to me. Will you be my wife? 💍✨")

# Columns for Yes/No buttons
col1, col2 = st.columns(2)

# Function to move the "No" button if clicked
def move_button():
    new_x = random.randint(10, 80)
    new_y = random.randint(10, 80)
    st.markdown(
        f"""
        <style>
        .stButton>button {{
            position: absolute;
            left: {new_x}%;
            top: {new_y}%;
        }}
        </style>
        """, unsafe_allow_html=True
    )

# Check for user response
if col1.button("💖 Yes, of course! 💖"):
    st.balloons()
    st.success("Yay! I love you so much! 💕")
    st.image("https://media.giphy.com/media/3o7TKU8RvQuomFfUUU/giphy.gif", width=300)
    st.write("You just made me the happiest person ever! 💍🥰")

if col2.button("😜 No"):
    move_button()
    time.sleep(0.2)
    st.warning("Hey! You can't say no! Try again! 😆")

# Additional romantic message
st.write("I never knew what true happiness was until I met you.✨")

# Hidden love letter message
with st.expander("💌 Click here for a special message 💌"):
    st.write("I fall in love with you all over again, each and every day.💖")
    st.write("You are the reason my heart smiles every single day.✨")
    st.write("I promise you, in every situation I will be next to you. 🥰")
    st.image("https://images.unsplash.com/photo-1582809620589-e9748fd04437?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=300)

# Play the audio from the GitHub URL
audio_url = "https://raw.githubusercontent.com/ANAHAN07/A-Cute-Propose-for-your-Heart/main/Run%20this%20file/Ed%20Sheeran%20-%20Perfect.mp3"
play_audio(audio_url)