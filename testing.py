import json

joke_file = open('jokes.json') # opening JSON file
jokes = json.load(joke_file) # returns JSON object as a dictionary
joke_file.close() # Closing file

print(jokes[0])