from openai import OpenAI
client = OpenAI('')

conversation = []
# Tools
def getWeatherDetails(city):
    if(city == 'mumbai'): 
        return '10°C'
    if(city == 'jind'):
        return '12°C'
    if(city == 'delhi'):
        return '14°C'

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break;
    conversation.append({"role": "user", "content": user_input})
    res = client.responses.create(
        model="gpt-4.1-mini",
        input=user_input
    )
    data = res.choices[0].message.content
    conversation.append({"role": "assistant", "content": data})


# model="gpt-4.1-mini",
#     input=user_input