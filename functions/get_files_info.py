import os
from google import genai
from google.genai import types
from py_compile import main

def get_files_info(working_directory, directory="."):
    path_working_directory = os.path.abspath(working_directory)
    # print("Working directory:", path_working_directory)
    if directory == ".":
        target_dir = path_working_directory
        # print("Target Directory is current directory.")
    else:
        # print(os.path.join(path_working_directory, directory))
        target_dir = os.path.normpath(os.path.join(path_working_directory, directory))
        # print("Target Directory:", target_dir)
        # Will be True or False
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a valid directory.'
    valid_target_dir = target_dir.startswith(path_working_directory)
    if valid_target_dir:
        # print("Valid target directory.")
        response_text = ""
        for content in os.listdir(target_dir):
            content_path = os.path.join(target_dir, content)
            size = os.path.getsize(content_path)
            is_dir = os.path.isdir(content_path)
            response_text += f" - {content}: - file_size: {size} bytes , is_dir: {is_dir}\n"
        return response_text
    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory of the tool. Use the python `os.getcwd()` command to retrieve it",
            ),
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def main():
    result = get_files_info("calculator/", "pkg")
    print(result)

if __name__ == "__main__":
    main()