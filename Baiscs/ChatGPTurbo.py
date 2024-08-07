# ---------------------------------
# 1. Get API Key
# API_KEY = 'YOUR_API_KEY'

# 2. Install openai
# pip install openai
# ---------------------------------

# ---------------------------------
from openai import OpenAI

client = OpenAI(api_key="API-KEY")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "What do you think 2 + 2 is?"},
    ],
)

message = response.choices[0].message.content
print(message)
# ---------------------------------

# the plans of the API key has been changed and I have finished my quota before even using it wow and hence I cannot run this program anymore