import os
import subprocess

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