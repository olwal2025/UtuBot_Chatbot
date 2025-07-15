import os
import streamlit as st
import openai

# Load API key: first from Streamlit secrets, then from environment variable
openai.api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="UtuBot - SRHR Chatbot", page_icon="🤖", layout="centered")

# Optional: Add a header image or icon
st.image(
    "https://media.istockphoto.com/id/2079743285/vector/studio-pc-2151-c-world-sexual-health-day.webp?s=1024x1024&w=is&k=20&c=Yldw_thLEYvBggomroKxN9ZC-zAqMORileIjfnBiJBY=",
    width=120,
)

st.title(" Welcome to UtuBot")
st.markdown("""
UtuBot is your friendly, culturally-aware AI assistant built to support young people with accurate, non-judgmental information about:

- 🩺 Sexual and reproductive health  
- ❤️ Relationships and consent  
- 🤔 Body changes and emotions  

### Why UtuBot?
- ✅ Answers based on trusted health FAQs  
- 🤖 Powered by AI for real-time chat  
- 🧠 Private, safe and always available

---

### 🚀 Ready to talk?

Click the button below to start chatting with UtuBot.
""")

if st.button("💬 Start Chatting"):
    st.switch_page("pages/1_💬_Chat.py")

# Optional: Contact info or footer
st.markdown("---")
st.caption("Built with ❤️ for better youth health. Contact: ahendaolwal@gmail.com")
