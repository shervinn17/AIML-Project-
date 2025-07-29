# 🤖 AI Chatbot for Mental Health Support

This project is a simple AI-powered chatbot designed to provide emotional support and empathetic conversations. It utilizes NLP models to engage users in safe, respectful dialogue.

---

## 🧠 Features

- Conversational AI using Hugging Face's DialoGPT model  
- Profanity filter to detect and block offensive inputs  
- Empathetic scripted fallback responses  
- Flask-based REST API for chat and session management  
- Streamlit frontend UI for interactive use  
- Session-wise chat logging  

---

## 🚀 Tools & Technologies

- Python 3.x  
- [Transformers (Hugging Face)](https://huggingface.co/transformers/)  
- Flask  
- Streamlit (optional UI)  
- better_profanity (for filtering)  

---

## 🛠 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/mental-health-chatbot.git
   cd mental-health-chatbot

   mental-health-chatbot/
├── mental_health_chatbot.py     # Flask API + chatbot logic
├── streamlit_app.py             # Frontend UI (optional)
├── requirements.txt             # Dependency list
├── README.md                    # Project overview

