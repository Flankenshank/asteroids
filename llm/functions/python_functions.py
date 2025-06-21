import os
import subprocess
from .files import get_file_content, get_files_info
from google import genai
from google.genai import types

def run_python_file(working_directory, file_path):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), file_path))
    if not (abs_file_path == abs_working_dir or abs_file_path.startswith(abs_working_dir + os.sep)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    file_name, file_extension = os.path.splitext(file_path) 
    if file_extension != '.py':
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(
            ["python3", file_path],
            cwd=working_directory,
            timeout=30,
            capture_output=True,
            text=True,
            check=False
        )
        lines = []
        if result.stdout:
            lines.append("STDOUT:\n" + result.stdout.rstrip())
        if result.stderr:
            lines.append("STDERR:\n" + result.stderr.rstrip())
        if result.returncode != 0:
            lines.append(f"Process exited with code {result.returncode}")
        if not lines:
            return "No output produced."
        return "\n".join(lines)
            
    except subprocess.TimeoutExpired:
        return "Error: executing Python file: Timeout expired"
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
def run_tests(filename, working_directory):
    abs_working_dir = os.path.abspath(working_directory)    
    try:
        result = subprocess.run(["python3", filename],
                                cwd=abs_working_dir,
                                capture_output=True,
                                text=True)
    except Exception as e:
        return f"Error running tests: {str(e)}"
    return result.stdout

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    function_map = {
        "write_file": write_file,
        "run_python_file":run_python_file,
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_tests": run_tests
        }
    
    if function_call_part.name in function_map:
        function_to_call = function_map[function_call_part.name]
        args_with_working_dir = {**function_call_part.args, "working_directory": "./calculator"}

        if function_call_part.name == "run_python_file":
            if "directory" in args_with_working_dir:
                args_with_working_dir["filepath"] = args_with_working_dir.pop("directory")
                
        function_result = function_to_call(**args_with_working_dir)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_result},
                )
            ],
        )
    else:
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"error": f"Unknown function: {function_call_part.name}"},
        )
    ],
)

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not (abs_file_path == abs_working_dir or abs_file_path.startswith(abs_working_dir + os.sep)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"