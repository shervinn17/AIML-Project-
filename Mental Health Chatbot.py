# === 1. Load and Fine-tune DialoGPT (optional pre-trained use) ===
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(user_input, chat_history_ids=None):
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response, chat_history_ids

# === 2. Basic NLP Filter for Offensive Input ===
from better_profanity import profanity
profanity.load_censor_words()

def is_offensive(text):
    return profanity.contains_profanity(text)

# === 3. Flask API ===
from flask import Flask, request, jsonify, session
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session handling

chat_sessions = {}  # Store per-session logs

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    session_id = session.get("id") or os.urandom(8).hex()
    session["id"] = session_id

    if session_id not in chat_sessions:
        chat_sessions[session_id] = []

    if is_offensive(user_input):
        bot_response = "I'm here to support you respectfully. Please avoid offensive language."
    else:
        history = chat_sessions[session_id][-1]["history"] if chat_sessions[session_id] else None
        bot_response, history = generate_response(user_input, history)

    chat_sessions[session_id].append({
        "user": user_input,
        "bot": bot_response,
        "timestamp": datetime.now().isoformat(),
        "history": history
    })

    return jsonify({"response": bot_response})

@app.route("/logs", methods=["GET"])
def logs():
    session_id = session.get("id")
    return jsonify(chat_sessions.get(session_id, []))

# === 5. Run App ===
if __name__ == "__main__":
    app.run(debug=True)
