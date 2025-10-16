import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]
    if not args: 
        print("Error: No arguments provided!")
        sys.exit(1)
    user_prompt = " ".join(args)


    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    content(client, messages, user_prompt)

def content(client, messages, user_prompt):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt),
    )

    verbose = "--verbose" in sys.argv
    if verbose:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
 
    if not response.function_calls:
        return response.text 
    function_call_part = response.function_calls[0]
    print("part",function_call_part)
    function_call_result = call_function(function_call_part, verbose=verbose)
    print(function_call_result,"result here")
    try:
        func_response = function_call_result.parts[0].function_response.response
        print("res", function_call_result.parts[0])
    except (AttributeError, IndexError):
        raise RuntimeError("Fatal: function_call_result missing function_response")
    # for func in response.function_calls:
    if verbose:
        print(f"Calling function: {func.name}({func.args})")
        print(f"-> {func_response}")

    return function_call_result


if __name__ == "__main__":
    main()
