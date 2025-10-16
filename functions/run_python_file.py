import os
import sys
import subprocess   
from google.genai import types


def run_python_file(working_directory, file_path, arg=[]):
    wkdir = os.path.abspath(working_directory)
    absfile_path = os.path.abspath(os.path.join(working_directory,file_path))
    try:
        if not absfile_path.startswith(wkdir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(absfile_path):
            return f'Error: File "{file_path}" not found.'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        cmd = ['python', absfile_path]
        if arg:
            cmd += arg
        result = subprocess.run(cmd,capture_output=True,text=True, timeout=30, cwd=wkdir )
        if not result.stdout.strip() and not result.stderr.strip():
            return  "No output produced."
        elif result.returncode != 0:
            return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}\nProcess exited with code {result.returncode}"
        else:
            return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"

    except Exception as e:
        return f"error: {str(e)}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="TPath to the Python file to execute, relative to the working directory.",
            ),
            "arg": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file."
                ),
                description="Optional arguments to pass to the Python file."
            )
        },
        required=['file_path'],
    ),
)