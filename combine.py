import wolframalpha
import wikipedia
import json

config={}
with open('config.json') as config_file:
    config = json.load(config_file)

api_key = config.get("api_key")

while True:
    my_input = input("Q : ")

    try:
        print("trying from wolfram for {}".format(my_input))
        client = wolframalpha.Client(api_key)
        res = client.query(my_input)
        ans = next(res.results).text
        print(ans)
    except:
        print("trying from wikipedia for {}".format(my_input))
        print (wikipedia.summary(my_input))

