import os
import sys
from dotenv import load_dotenv, find_dotenv
from google import genai
from google.genai import types
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
model_name = "gemini-1.5-flash"
client = genai.Client(api_key=api_key)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
        required=["directory"]
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file contents",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Read file contents.",
            ),
        },
        required=["directory"]
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Execute Python files with optional arguments.",
            ),
        },
        required=["directory"]
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Write or overwrite files.",
            ),
        },
        required=["directory"]
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

config = types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)

if len(sys.argv) < 2:
    print("No prompt given")
    sys.exit(1)

user_prompt = " ".join(sys.argv[1:])

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=config,
)

if response.function_calls:
    for func in response.function_calls:
        print (f"Calling function: {func.name}({func.args})")
else:
    print(response.text)
