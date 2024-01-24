import random
import os
import time

def readfile(file):
    files = open("" + file, "r", encoding="utf8")
    text = list(map(lambda string: string.rstrip("\n"), files))
    array = []

    for i in text:
        array.append(i)

    files.close()
    return array

def appendfile(file, text):
    files = open("" + file, "a")
    files.write(text + '\n')
    files.close()

def randomize(vari):
    temp = [random.choice(vari), random.choice(vari)]

    return temp

while True: # Text randomizer + tweeting

    fangames = readfile("text/fangames.txt")
    events = readfile("text/events.txt")
    spreadsheets = readfile("text/spreadsheets.txt")
    texts = readfile("text/text.txt")
    types = readfile("text/types.txt")
    tweets = readfile("tweets.txt")
    
    fangame = randomize(fangames)
    event = randomize(events)
    spreadsheet = randomize(spreadsheets)
    f_type = randomize(types)

    tweet = random.choice(texts)

    tweet = f'f"{tweet}"'
    
    tweet = "I wanna Kardia is a great beginner fangame!"
    print(tweets)
    if tweet in tweets:
        time.sleep(5)
        print("repetido")
    else:
        print("lol")
    continue