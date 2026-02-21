from openai import OpenAI
client = OpenAI(api_key="")

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
    print("*" * 110)
    user_input = input("👤 You: ")
    SYS_PROMPT = """You are an AI Assistant with START, PLAN, ACTION, Observation and Output state.\n Wait for the User prompt and first PLAN using available tools.\n After Planing, Take the action with appropriate tools and wait for the Observation based on Action. Once you get the observations, Return the AI response based on START prompt and observations\n Avilable Tools: \n -def getWeatherDetails(city): \n getWeatherDetails is a function that accept city as string and return the weather details.\n Example: \n START\n {"type": "user", "user": "What is the sum of weather of delhi and mumbai?"}\n {"type": "plan", "plan": "I will call the getWeatherDetails for delhi"}\n {"type": "action", "function": "getWeatherDetails", "input": "delhi"}\n {"type": "observation", "observation": "14°"}\n {"type": "plan", "plan": "I will call the getWeatherDetails for mumbai"}\n {"type": "action", "function": "getWeatherDetails", "input": "mumbai"}\n {"type": "observation", "observation": "12°"}\n {"type": "output", "output": "The sum of weather of delhi and mumbai is 26°C"}"""
    if user_input == "exit":
        break;
    conversation.append({"role": "user", "content": user_input})
    res = client.responses.create(
        model="gpt-4.1-mini",
        # input=[{'role': 'system', 'content': SYS_PROMPT},
        #        {'role': 'user', 'content': user_input}]
        input =  
            [
               {'role': 'system', 'content': SYS_PROMPT},
               {'role': 'developer', 'content':'{"type": "plan", "plan": "I will call the getWeatherDetails"}'},
               {'role': 'developer', 'content':'{"type": "action", "function": "getWeatherDetails", "input": "delhi"}'},
               {'role': 'developer', 'content':'{"type": "observation", "observation": "14°C"}'},
               {'role': 'user', 'content': user_input}
            ]
        # messages= [
        #     {"role": "system", "content": SYS_PROMPT},
        #     {"role": "user", "content": user_input}
        # ]
    )
    data = res.output[0].content[0].text
    print("🤖 Bot: ", data)
    conversation.append({"role": "assistant", "content": data})


# model="gpt-4.1-mini",
#     input=user_input