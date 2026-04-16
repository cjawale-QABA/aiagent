# import os
# import sys
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types



# load_dotenv()
# api_key = os.environ.get("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)
# verbose_flag = False
# if len(sys.argv) < 2 or len(sys.argv) > 3:
#     sys.exit("Please provide a prompt as a command-line argument.")
# else:
#     prompt = sys.argv[1]
#     messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
#     response = client.models.generate_content(
#         model='gemini-2.5-flash', contents=messages,
#     )
#     if len(sys.argv) == 3:
#         verbose_flag = True
#     elif len(sys.argv) == 2:
#         verbose_flag = False




# def main():
#     print("API: ", api_key)
#     try:
#         if verbose_flag:
#             if response.usage_metadata:
#                 # print("Response metadata: ", response.usage_metadata)
#                 print("prompt token: ", response.usage_metadata.prompt_token_count)
#                 print("response token: ", response.usage_metadata.candidates_token_count)
#                 print("Response: ", response.text)
#         else:
#             print("Response: ", response.text)
#     except RuntimeError as e:
#         print("Error: ", e)



# if __name__ == "__main__":
#     main()


from functions import get_files_info

