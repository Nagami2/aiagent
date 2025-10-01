
import os
import sys
from google.genai import types

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_path.startswith(os.path.abspath(working_directory)):
        raise ValueError(f"Error: {file_path} is outside the working directory")
    if not os.path.isfile(full_path):
        raise ValueError(f"Error: {file_path} is not a file")
    try:
        with open(full_path, 'r') as file:
            return file.read()[:MAX_CHARS]
    except Exception as e:
        return f'Exception reading file: {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file within the working directory, returning up to MAX_CHARS characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
    

    

# print(get_file_content('calculator', 'pkg/calculator.py'))
# print(get_file_content('calculator', 'lorem.txt'))