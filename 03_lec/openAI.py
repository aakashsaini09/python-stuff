from openai import OpenAI
client = OpenAI(api_key="")

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Tell me a programming joke"
)

print(response.output[0].content[0])

# from openai import OpenAI
    
# client = OpenAI(api_key="YOUR_NEW_KEY")

# response = client.responses.create(
#     model="gpt-4.1-mini",
#     input="Say this is a test"
# )

# print(response.output[0].content[0].text)