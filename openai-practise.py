import openai
import credentials
openai.api_key = credentials.openai_api_key
# model_list = sorted([openai.Model.list()["data"][i].id for i in range(len(openai.Model.list()["data"]))])
# print(model_list)
# prompt = "ask me a good question"

# print(openai.Completion.create(
#     model = "text-davinci-003",
#     prompt = prompt)["choices"][0].text)

# print("\n" +
#     openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo-0301",
#         messages = [
#             {
#                 "role": "user",
#                 "content": "Do you have access to LinkedIn posts or content?"
#             }
#         ]
#     )["choices"][0].message.content
# + "\n")

import langchain

llm = langchain.llms.OpenAI(openai_api_key = credentials.openai_api_key)

tools = langchain.agents.load_tools(["google-search"], llm = llm)

agent = langchain.agents.initialize_agent(
    tools,
    llm,
    agent = langchain.agents.AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)

prompt = "what does anomaly mean?"

agent.run(f"{prompt}")