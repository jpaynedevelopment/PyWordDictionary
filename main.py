import requests
import json

word_choice = input("\nWhat word: \n")


url = f'https://wordsapiv1.p.rapidapi.com/words/{word_choice}/definitions'

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': "Replace your own API key"
    }

response = requests.request("GET", url, headers=headers)


def definiton():
    definitions = response.text
    json_data = json.loads(definitions)
    def_data = json_data['definitions']

    for x in def_data:
        for y in x:
            if y == 'definition':
                print('Definition:')
            else:
                print("Part of Speech:")
            print(x[y])
        print()

def main():
    print()
    definiton()

main()