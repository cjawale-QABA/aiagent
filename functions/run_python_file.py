import os
from dotenv import load_dotenv
import subprocess
import sys

load_dotenv()

def run_python_file(working_directory: str, file_path: str, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: Cannot run "{file_path}" as it is not a file'
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" as it is not a Python file'
    command = ["python", abs_file_path]
    if args:
        command.extend(args)
    result = subprocess.run(command, cwd=abs_working_dir, text=True, capture_output=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=30)
    if result.returncode != 0:
        return f'Process exited with code {result.returncode}\nError: "{file_path}" failed to run with error:\n{result.stdout}'
    return result