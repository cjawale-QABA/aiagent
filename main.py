import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
verbose_flag = False
response = None
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
if len(sys.argv) < 2 or len(sys.argv) > 3:
    sys.exit("Please provide a prompt as a command-line argument.")

prompt = sys.argv[1]
if len(sys.argv) == 3:
    verbose_flag = True
elif len(sys.argv) == 2:
    verbose_flag = False

messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
agent_output = None 
agent_error = None

for i in range(20):
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=messages, 
            config=types.GenerateContentConfig(
                system_instruction=system_prompt, 
                temperature=0, 
                tools=[available_functions]
            ),
        )
    except Exception as e:
        agent_error = str(e)
        break
    # print('gemini:', i, response)
    print()
    # for content in response.candidates:
    if not response.function_calls or len(response.function_calls) == 0:
        agent_output = str(response.text)
        break
    for function_call in response.function_calls:
        try:
            function_result = call_function(function_call, verbose=verbose_flag)
            messages.append(function_result)
        except Exception as e:
            agent_error = str(e)
            break
        if function_result.parts and len(function_result.parts) == 0:
            agent_error = "Function response is empty"
            break
        if type(function_result.parts[0].function_response) != types.FunctionResponse:
            agent_error = "Invalid function response format"
            break
        if function_result.parts[0].function_response.response is None:
            agent_error = "Function response is None"
            break

        if verbose_flag:
            print(f"-> {function_result.parts[0].function_response.response['result']}")

if agent_output:
    print(f'Output: {agent_output}')
elif agent_error:
    print(f'Error: {agent_error}')
        

def main():
    pass

if __name__ == "__main__":
    main()

