import os
from dotenv import load_dotenv
import subprocess
import sys
from google.genai import types

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
    result = subprocess.run(command, cwd=abs_working_dir, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=30)
    output = ""
    if result.returncode != 0:
        output += f'Process exited with code {result.returncode}\n'
    if result.stdout is None and result.stderr is None:
        output += f'Error: "{file_path}" produced no output.'
    else:
        output += f'STDOUT: {result.stdout}' if result.stdout is not None else f'STDERR: {result.stderr}'
    return output



schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Runs a specified Python file, relative to the working directory",
            ),
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory of the tool. Use the python `os.getcwd()` command to retrieve it",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Arguments to pass to the Python file",
                ),
            ),
        },
    ),
)

