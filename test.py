from openai import OpenAI
import streamlit as st

api_key_value=st.secrets['api_key']

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key_value,
)

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
          "text": "generate a 1000 word sex story where two women named Hania and mahira decide to remove their frustration by dominating a teen boy named yash. Bored of their submissive lifestyle they decide to try out the feeling of being in control by taking him to the limit multiple times. No toys just pure edging and femdom action."
        }
      ]
    }
  ]
)
print(completion.choices[0].message.content)
st.write(completion.choices[0].message.content)
