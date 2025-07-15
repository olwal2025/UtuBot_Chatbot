# UtuBot Chatbot

A culturally-aware SRHR (Sexual Reproductive Health and Rights) chatbot project for the PLP AI for Software Engineering Finals.

## Overview

UtuBot is an AI-powered assistant designed to support young people with accurate, non-judgmental information about sexual and reproductive health, relationships, consent and body changes. The chatbot provides real-time answers based on trusted health FAQs and AI, ensuring privacy and empathy.

## Features

- 🩺 Answers to common SRHR questions
- ❤️ Guidance on relationships and consent
- 🤖 Real-time chat powered by OpenAI
- 🧠 Private, safe and always available
- 🌍 Culturally-appropriate responses for African youth

## Getting Started

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [OpenAI API Key](https://platform.openai.com/signup)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/olwal2025/UtuBot_Chatbot.git
    cd UtuBot_Chatbot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your OpenAI API key to a `.env` file in the project root:
    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

> **Note:** The `.env` file is listed in `.gitignore` and will not be tracked by Git.

### Running the App Locally

```bash
streamlit run Home.py
```

The app will be available at [http://localhost:8501](http://localhost:8501).

### Live Demo

Try the deployed chatbot here:  
[https://hzsyjuj3m2kuwgd8ljkbtc.streamlit.app/](https://hzsyjuj3m2kuwgd8ljkbtc.streamlit.app/)

## Project Structure

- `Home.py` – Main landing page
- `pages/1_💬_Chat.py` – Chatbot interface
- `faqs.json` – Frequently asked questions and answers
- `requirements.txt` – Python dependencies

## Contact

Built with ❤️ by Ahenda Olwal  
Email: ahendaolwal@gmail.com