import os
from config import MAX_FILE_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.abspath(os.path.join(working_directory, file_path))

        if not target_file.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, "r") as f:
            content = f.read()
            print(content)

        if len(content) > MAX_FILE_CHARS:
            content = content[:MAX_FILE_CHARS] + f'\n[...File "{file_path}" truncated at {MAX_FILE_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {str(e)}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="read the contents in the files constrained to the working directory, the maximum characters in the file is 10000",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory":types.Schema(
                type=types.Type.STRING,
                description="The file path to take the content from, relative to the working directory. If not pr not provided, return an error"
            )
        }
    )
)