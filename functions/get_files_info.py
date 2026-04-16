import os
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



def main():
    result = get_files_info("calculator/", "pkg")
    print(result)

if __name__ == "__main__":
    main()