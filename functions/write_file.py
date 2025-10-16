import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        abswkdir = os.path.abspath(working_directory)
        target_file = os.path.abspath(os.path.join(working_directory,file_path))

        if not target_file.startswith(abswkdir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(target_file): 
            try:
                os.makedirs(os.path.dirname(target_file),exist_ok= True)
            except Exception as e:
                return f"Error: creating directory: {e}"
            
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write or overwrite files, relative to the working directory. If the content not provided, the function should still overwrite the file , and the file would become empty"
            )   
        },
        required=["file_path", "content"],
    ),
)