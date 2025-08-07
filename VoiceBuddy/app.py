import streamlit as st
from voice_io import listen_to_user, speak_text, handle_command

def main():
    st.set_page_config(page_title="VoiceBuddy", page_icon="🎙️")
    st.title("🎙️ VoiceBuddy: Your Voice Assistant")

    # Initial welcome greeting (only once per session)
    if "greeted" not in st.session_state:
        st.session_state.greeted = False

    if not st.session_state.greeted:
        speak_text("Hey, I am VoiceBuddy, your personal voice assistant. How can I help you today?")
        st.session_state.greeted = True

    st.markdown("Click the button and speak your command.")
    if st.button("🎤 Start Listening"):
        user_command = listen_to_user()
        if user_command:
            response = handle_command(user_command)
            st.success(response)
            speak_text(response)
        else:
            st.warning("Didn't catch that. Try again!")

if __name__ == "__main__":
    main()
