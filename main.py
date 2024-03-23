from dotenv import load_dotenv
import os
import tweepy
import atproto
import time
import random
from datetime import datetime

def readfile(file):
    files = open(file, "r", encoding="utf8")
    text = list(map(lambda string: string.rstrip("\n"), files))
    array = []

    for i in text:
        array.append(i)

    files.close()
    return array

def randomize(vari):
    temp = [random.choice(vari), random.choice(vari)]

    text = list(map(lambda string: string.rstrip(), temp))

    return text

## Dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

BSKYHANDLE = os.getenv("BSKYHANDLE")
BSKYPASSWORD = os.getenv("BSKYPASSWORD")


## Twitter

if ACCESS_TOKEN == "" or ACCESS_SECRET == "":
    print("No access token OR access secret found, please use get_access_keys.py")
    exit()

if os.getenv("ACCESS_TOKEN") == None or os.getenv("ACCESS_SECRET") == None:
    print("No access token OR access secret found, please use get_access_keys.py")
    exit()

auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET,
    ACCESS_TOKEN, ACCESS_SECRET
)

api = tweepy.API(auth)

twitterClient = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

## Bluesky
bskyClient = atproto.Client()
bskyClient.login(BSKYHANDLE, BSKYPASSWORD)


while True: # Text randomizer + posting

    fangames = readfile("text/fangames.txt")
    events = readfile("text/events.txt")
    spreadsheets = readfile("text/spreadsheets.txt")
    texts = readfile("text/text.txt")
    types = readfile("text/types.txt")
    games = readfile("text/games.txt")
    things = readfile("text/stuff.txt")
#    players = readfile("text/people.txt") // Players won't be used until there's more than 3 guys
    
    fangame = randomize(fangames)
    event = randomize(events)
    spreadsheet = randomize(spreadsheets)
    game = randomize(games)
    thing = randomize(things)
#    player = randomize(players) // Players won't be used until there's more than 3 guys
    
    f_type = randomize(types)

    post = random.choice(texts)
    post = str(post).replace('\n', '')

    post = f'f"{post}"'
    post = eval(post)

    try:
        twitterClient.create_tweet(text = post)
        bskyClient.send_post(text= post)
        print(post + " | posted at: " + datetime.now().strftime("%H:%M:%S"))  
        time.sleep(1800)
    except tweepy.errors.Forbidden:
        print("Twitter error: tweepy.errors.Forbidden")
        time.sleep(10)