'''
he directory parameter should be treated as a relative path within the working_directory. 
Use os.path.join(working_directory, directory) to create the full path, then validate it stays within the working directory boundaries.
If the full path is not within the working directory, raise a ValueError with the message "Directory is outside the working directory".
If the directory argument is not a directory, again, return an error string: "Directory is not a directory".
Build and return a string representing the contents of the directory. It should use this format:
- README.md: file_size=1032 bytes, is_dir=False
- src: file_size=128 bytes, is_dir=True
- package.json: file_size=1234 bytes, is_dir=False

use standard python libraries to achieve this.
'''
import os

from google.genai import types

def get_files_info(working_directory, directory="."):
    # Create the full path by joining the working directory and the provided directory
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    
    # Ensure the full path is within the working directory boundaries
    if not full_path.startswith(os.path.abspath(working_directory)):
        raise ValueError(f"Error: {directory} is outside the working directory")

    # Check if the full path is a directory
    if not os.path.isdir(full_path):
        raise ValueError(f"Error: {directory} is not a directory")

    # List to hold file information strings
    files_info = []
    
    # Iterate over the items in the directory
    for item in os.listdir(full_path):
        item_path = os.path.join(full_path, item)
        file_size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)
        files_info.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
    
    # Join the list into a single string with new lines
    return "\n".join(files_info)


# print(get_files_info('calculator', '.'))
# print(get_files_info('calculator', 'pkg'))
# print(get_files_info('calculator', '/bin'))
# print(get_files_info('calculator', '../'))

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
    ),
)