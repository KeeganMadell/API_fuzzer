import requests
import sys

def loop():
    for word in sys.stdin: # used to processinput from file or pipeline(checks for words in 'words.txt')
        response = requests.get(url=f"https://jsonplaceholder.typicode.com/todos{word}") # requests data from url , stores it in 'response' variable
        if response.status_code == 404: #if the response is a 404 error call the loop function again 
            loop()
        else: # otherwise it prints the data below
            data = response.json
            print(data)
            print(response.status_code)
            print(word)
loop()
