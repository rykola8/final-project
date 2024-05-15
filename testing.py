import json

joke_file = open('jokes.json', encoding='utf-8') # opening JSON file
jokes = json.load(joke_file) # returns JSON object as a dictionary
joke_file.close() # Closing file

for joke in jokes:
    print(joke["joke"])
