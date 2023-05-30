import openai
import credentials
# openai.organization = "org-rjk9KVuSZRAXwdBUkubDvur0"
openai.api_key = credentials.openai_api_key
# model_list = sorted([openai.Model.list()["data"][i].id for i in range(len(openai.Model.list()["data"]))])
# print(model_list)
# prompt = "ask me a good question"

# print(openai.Completion.create(
#     model = "text-davinci-003",
#     prompt = prompt)["choices"][0].text)

print(
    openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-0301",
        messages = [
            {
                "role": "user",
                "content": "Who originally wrote the song O Holy Night?"
            }
        ]
    )["choices"][0].message.content
)