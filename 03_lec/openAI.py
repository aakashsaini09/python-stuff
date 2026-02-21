from openai import OpenAI
client = OpenAI('')

conversation = []
print("ChatBot Started. Enter 'exit' to quit\n")
while True:
    user_input = input("You: ")
    if user_input == "exit":
        break;
    conversation.append({"role": "user", "content": user_input})
    res = client.responses.create(
        model="gpt-4.1-mini",
        input=user_input
    )

    res = (res.output[0].content[0].text)
    print("Bot: ", res)
    conversation.append({"role": "assistant", "content": res})

# from openai import OpenAI

# client = OpenAI(api_key="YOUR_NEW_KEY")

# response = client.responses.create(
#     model="gpt-4.1-mini",
#     input="Say this is a test"
# )

# print(response.output[0].content[0].text)