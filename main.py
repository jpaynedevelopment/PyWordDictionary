import requests
import json

word_choice = input("What word: \n")

url = f'https://wordsapiv1.p.rapidapi.com/words/{word_choice}/definitions'

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': "7e748ca65emsh86c8cd4d234a06cp1a4856jsncd55a4cbafb3"
    }

response = requests.request("GET", url, headers=headers)

definitions = response.text

json_data = json.loads(definitions)

print(word_choice)
print(json_data["definitions"])