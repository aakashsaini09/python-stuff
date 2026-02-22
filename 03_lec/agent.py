from openai import OpenAI
import json
client = OpenAI(api_key="")
def getWeatherDetails(city):
    city = city.lower().strip()
    data = {
        "mumbai": "10°C",
        "jind": "22°C",
        "delhi": "14°C",
        "hisar": "19°C",
        "rohtak": "11°C",
        "pune": "13°C"  
    }
    return data.get(city, "City not found")

tools = {
    "getWeatherDetails": getWeatherDetails
}
SYS_PROMPT = """You are an AI Assistant with START, PLAN, ACTION, Observation and Output state.\n Wait for the User prompt and first PLAN using available tools.\n After Planing, Take the action with appropriate tools and wait for the Observation based on Action. Once you get the observations, Return the AI response based on START prompt and observations\n Strictly follow the JSON output format as in examples.\n Avilable Tools: \n -def getWeatherDetails(city): \n getWeatherDetails is a function that accept city as string and return the weather details.\n Example: \n START\n {"type": "user", "user": "What is the sum of weather of delhi and mumbai?"}\n {"type": "plan", "plan": "I will call the getWeatherDetails for delhi"}\n {"type": "action", "function": "getWeatherDetails", "input": "delhi"}\n {"type": "observation", "observation": "14°"}\n {"type": "plan", "plan": "I will call the getWeatherDetails for mumbai"}\n {"type": "action", "function": "getWeatherDetails", "input": "mumbai"}\n {"type": "observation", "observation": "12°"}\n {"type": "output", "output": "The sum of weather of delhi and mumbai is 26°C"}"""
conversation = [{'role': 'system', 'content': SYS_PROMPT}]
while True:
    print("*" * 110)
    user_inp = input("👤 You: ")
    if(user_inp == 'exit'):
        break
    q = {
        "type": "user",
        "user": user_inp
    }
    conversation.append({"role": "user", "content": json.dumps(q)})
    while True:
        chat = client.responses.create(
            model="gpt-4.1-mini",
            input=conversation
        )

        result = chat.output[0].content[0].text
        try:
            call = json.loads(result)
        except: 
            print("Invalid JSON:", result)
            break
        print("DEBUG MODEL OUTPUT:", result)
        if call["type"] == "output":
            print("🤖 Bot:", call["output"])
            conversation.append({"role": "assistant", "content": result})
            break
        elif call['type'] == 'plan':
            conversation.append({
                "role": "assistant",
                "content": result
            })
            continue
        elif call["type"] == "action":
            fn = tools[call["function"]]
            observation = fn(call["input"])

            obs = {
                "type": "observation",
                "observation": observation
            }

            conversation.append({
                "role": "assistant",
                "content": json.dumps(obs)
            })




# while True:
#     print("*" * 110)
#     user_input = input("👤 You: ")
#     if user_input == "exit":
#         break;
#     conversation.append({"role": "user", "content": user_input})
    # res = client.responses.create(
    #     model="gpt-4.1-mini",
    #     # input=[{'role': 'system', 'content': SYS_PROMPT},
    #     #        {'role': 'user', 'content': user_input}]
    #     input =  
    #         [
    #            {'role': 'system', 'content': SYS_PROMPT},
    #            {'role': 'developer', 'content':'{"type": "plan", "plan": "I will call the getWeatherDetails"}'},
    #            {'role': 'developer', 'content':'{"type": "action", "function": "getWeatherDetails", "input": "delhi"}'},
    #            {'role': 'developer', 'content':'{"type": "observation", "observation": "14°C"}'},
    #            {'role': 'user', 'content': user_input}
    #         ]
    # )
    # data = res.output[0].content[0].text
    # print("🤖 Bot: ", data)
    # conversation.append({"role": "assistant", "content": data})