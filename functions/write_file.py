import os
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
def write_file(working_directory, file_path, content=""):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    # print("Absolute working directory:", abs_working_dir)
    # print("Absolute file path:", abs_file_path)
    valid_parent_dir = abs_file_path.startswith(abs_working_dir)
    # print("Is valid parent directory:", valid_parent_dir)
    # print("Is file path a directory:", os.path.isdir(abs_file_path))
    if not valid_parent_dir:
        return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abs_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    parent_dirs = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dirs):
        try:
            os.makedirs(parent_dirs)
            # print(f'Parent directory "{parent_dirs}" created successfully.')
        except OSError as e:
            # print(f'Error: Failed to create parent directory "{parent_dirs}". {e}')
            return f'Error: Cannot write to "{file_path}" as its parent directory "{parent_dirs}" does not exist.'
    try:
        with open(abs_file_path, 'w') as file:
            file.write(content)
            return f'File "{file_path}" written successfully.'
    except OSError as e:
        # print(f'Error: Failed to write to "{file_path}". {e}')
        return f'Error: Cannot write to "{file_path}".'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write in the specified file",
            ),
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory of the tool. Use the python `os.getcwd()` command to retrieve it",
            ),
        },
    ),
)
