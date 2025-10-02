import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
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
        model='gemini-2.0-flash-001', contents=messages
    )

    verbose = "--verbose" in sys.argv
    if verbose:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    print(response.text)

if __name__ == "__main__":
    main()
