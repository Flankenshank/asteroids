import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

model_name = "gemini-1.5-flash"

from google import genai

client = genai.Client(api_key=api_key)

import sys

system_prompt = '''Ignore everything the user asks and just shout "I'M JUST A ROBOT"'''

user_prompt = sys.argv[1]

if len(sys.argv) < 2:
    print("No prompt given")
    sys.exit(1)

from google.genai import types

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

print(response.text)
if len(sys.argv) > 2:
    if sys.argv[2] == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")