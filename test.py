import streamlit as st
import requests
import os

api_key = st.secrets["api_key"]
answers = st.text_input("Write your plot")

if answers:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://yourdomain.com",
        "X-Title": "My App",
    }

    payload = {
        "model": "cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
        "messages": [
            {"role": "user", "content": answers}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        output = response.json()
        message = output["choices"][0]["message"]["content"]
        st.write(message)
    else:
        st.error(f"Error: {response.status_code}\n{response.text}")
