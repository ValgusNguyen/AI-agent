from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file , run_python_file
from functions.write_file import schema_write_file , write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ])

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})") 
    else:
        print(f" - Calling function: {function_call_part.name}")
    Functions = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "write_file": write_file,
        "run_python_file": run_python_file,
    } 
    kwargs = dict(function_call_part.args or {})
    funcname= function_call_part.name
    func = Functions.get(funcname)
    if not func:
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=funcname,
            response={"error": f"Unknown function: {funcname}"},
        )
    ],
) 
    kwargs["working_directory"] = "./calculator"
    result = func(**kwargs)
    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=funcname,
            response={"result": result},
        )
    ],
)