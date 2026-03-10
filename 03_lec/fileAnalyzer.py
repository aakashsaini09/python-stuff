from openai import OpenAI
client = OpenAI(api_key="")
file = open("Test.java", "r")

content = file.read()
print(content)
file.close()
response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Analyze the letter and provide a summary of the key points.",
                },
                {
                    "type": "input_file",
                    "file_url": content,
                },
            ],
        },
    ]
)

print(response.output[0].content[0].text)