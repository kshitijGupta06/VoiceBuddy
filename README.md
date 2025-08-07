
# VoiceBuddy

### 🚀 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Replace `"your-api-key"` in `gpt_helper.py` with your actual OpenAI API key.

3. Start the app:
```bash
streamlit run main.py
```

### 🔐 Add Authentication (Optional)

Use `streamlit_authenticator` to add login:
```bash
pip install streamlit-authenticator
```
Example code: [https://github.com/mkhorasani/Streamlit-Authenticator](https://github.com/mkhorasani/Streamlit-Authenticator)

### 🌐 Deployment

To deploy on platforms like Streamlit Cloud:

1. Push your code to GitHub.
2. Connect GitHub repo to https://share.streamlit.io
3. Set the `OPENAI_API_KEY` in secrets or directly in the code.
    
