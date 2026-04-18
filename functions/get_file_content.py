import os
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
MAX_CHARS = os.environ.get("MAX_CHARS")

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    valid_target_dir = abs_file_path.startswith(abs_working_dir)
    if not valid_target_dir:
        return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a valid file.'

    with open(abs_file_path, 'r') as file:
        full_file_content = file.read()
        # print(len(full_file_content))
        if len(full_file_content) > 10000:
            content_file = full_file_content[:10000] + f'\n\n\n\n[...File "{file_path}" truncated at {MAX_CHARS} characters] \n'
            return content_file
        return full_file_content


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to retrieves the content from, relative to the working directory",
            ),
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory of the tool. Use the python `os.getcwd()` command to retrieve it",
            ),
        },
    ),
)


def main():
    result = get_file_content("calculator/", "pkg/does_not_exist.py")
    print(result)

if __name__ == "__main__":
    main()

