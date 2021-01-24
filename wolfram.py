import wolframalpha
import json

config={}
with open('config.json') as config_file:
    config = json.load(config_file)

api_key = config.get("api_key")

my_input = input("Question : ")
client = wolframalpha.Client(api_key)

res = client.query(my_input)
ans = next(res.results).text

print(ans)
