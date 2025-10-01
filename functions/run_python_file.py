import os
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_path.startswith(os.path.abspath(working_directory)):
        raise ValueError(f"Error: {file_path} is outside the working directory")
    if not os.path.isfile(full_path):
        raise ValueError(f"Error: {file_path} is not a file")
    
    try:
        import subprocess
        result = subprocess.run(
            ['python3', full_path] + args,
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
            cwd=working_directory
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error executing file: {e.stderr}'
    except Exception as e:
        return f'Exception executing file: {e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file within the working directory, returning the standard output.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="The arguments to pass to the Python file.",
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                default=[]
            ),
        },
        required=["file_path", "args"],
    ),
)