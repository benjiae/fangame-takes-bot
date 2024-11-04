import dotenv
import time
from datetime import datetime
import random

def readfile(file):
    files = open("./text/" + file + ".txt", "r", encoding="utf8")
    text = list(map(lambda string: string.rstrip("\n"), files))
    array = []

    for i in text:
        array.append(i)

    files.close()
    return array

def get_random_element(vari):
    temp = [random.choice(vari), random.choice(vari)]

    text = list(map(lambda string: string.rstrip(), temp))

    return text

def randomize(file):
    text_file = readfile(file)
    return get_random_element(text_file)

def get_post():
    fangame = randomize("fangames")
    event = randomize("events")
    game = randomize("games")
    spreadsheet = randomize("spreadsheets")
    thing = randomize("stuff")
    f_type = randomize("types")

    text = randomize("text")

    post = str(text[1]).replace('\n', '')

    post = f'f"{post}"'
    post = eval(post)

    return post


dotenv.load_dotenv()

with open("post.txt", "w", encoding="utf-8") as f:
    f.write(get_post())