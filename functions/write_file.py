from google.genai import types

import os


def write_file(working_directory, file_path, content):

    # Create the full path by joining the working directory and the provided file path
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    try:
        # Ensure the full path is within the working directory boundaries
        if not full_path.startswith(os.path.abspath(working_directory)):
            raise ValueError(f"Error: {file_path} is outside the working directory")
    except Exception as e:
        return f"Exception validating file path: {e}"

    try:
        # Create any necessary directories in the file path
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
    except Exception as e:
        return f"Exception creating directories: {e}"

    try:
        # Write the content to the file
        with open(full_path, 'w') as file:
            file.write(content)
    except Exception as e:
        return f"Exception writing file: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)