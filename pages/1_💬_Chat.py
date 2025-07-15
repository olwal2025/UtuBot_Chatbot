import streamlit as st
import openai
from dotenv import load_dotenv
import os
import json
from difflib import get_close_matches

# Load environment variables
load_dotenv()
openai.api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

# Load FAQs from faqs.json
def load_faqs():
    with open("faqs.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["faqs"]  # <-- Fix: get the list under "faqs"

faqs = load_faqs()

# Match user's question with FAQs
def match_faq(user_question):
    questions = [faq["question"] for faq in faqs]
    matches = get_close_matches(user_question.lower(), [q.lower() for q in questions], n=1, cutoff=0.7)
    if matches:
        for faq in faqs:
            if faq["question"].lower() == matches[0]:
                return faq["answer"]
    return None

# Streamlit UI setup
st.set_page_config(page_title="UtuBot - SRHR Chat", page_icon="🤖", layout="centered")
st.title(" UtuBot - Your Friendly SRHR Assistant ")
st.caption("A culturally-appropriate AI assistant promoting safe, informed decisions.")

# Custom CSS for bold fonts and creative colors
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Roboto:wght@400;900&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Montserrat', 'Roboto', sans-serif;
        background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
    }
    h1, .stTitle {
        font-family: 'Montserrat', sans-serif;
        font-weight: 900;
        color: #3b82f6;
        text-shadow: 2px 2px 0 #fbbf24;
        letter-spacing: 2px;
    }
    .stCaption {
        font-family: 'Roboto', sans-serif;
        font-size: 1.1em;
        color: #6366f1;
        font-weight: bold;
        background: #fef9c3;
        padding: 8px 16px;
        border-radius: 8px;
        margin-bottom: 16px;
        display: inline-block;
    }
    .stChatMessage {
        font-family: 'Roboto', sans-serif;
        font-size: 1.08em;
        color: #1e293b;
        background: #e0e7ff;
        border-radius: 12px;
        padding: 12px 18px;
        margin: 8px 0;
        box-shadow: 0 2px 8px #c7d2fe;
    }
    .stChatMessage.user {
        background: #fbbf24;
        color: #1e293b;
        font-weight: bold;
    }
    .stChatMessage.assistant {
        background: #3b82f6;
        color: #fff;
        font-weight: bold;
    }
    .stChatInput {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.1em;
        border: 2px solid #6366f1;
        border-radius: 8px;
        padding: 10px;
        margin-top: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are UtuBot, a friendly SRHR assistant for teens in Africa. Respond with empathy and clarity."}
    ]

# Display previous messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about your body, relationships or sexual health..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Try FAQ match first
    faq_response = match_faq(prompt)

    if faq_response:
        reply = faq_response
    else:
        # Fallback to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages,
            temperature=0.6
        )
        reply = response.choices[0].message.content

    # Display and save assistant reply
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
