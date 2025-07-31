from openai import OpenAI
import streamlit as st

api_key_value=st.secrets['api_key']

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key_value,
)


answer=st.text_input("Enter your plot")

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"{answer}"
        }
      ]
    }
  ]
)
print(completion.choices[0].message.content)
st.write(completion.choices[0].message.content)
