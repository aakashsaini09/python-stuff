import openai
openai.api_key = ""
prompt = "Say this is a test"
response = openai.completions.create(model="davinci-002", prompt=prompt, max_tokens=6)
print(response)
