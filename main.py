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

BEARER = os.getenv("BEARER_TOKEN")
APIKEY = os.getenv("API_KEY")
APISECRET = os.getenv("API_SECRET")
BSKYHANDLE = os.getenv("BSKYHANDLE")
BSKYPASSWORD = os.getenv("BSKYPASSWORD")
CALLBACK = "http://localhost:8000"


## Twitter

user_handler = tweepy.OAuth1UserHandler(
    APIKEY, APISECRET,
    callback=CALLBACK
)

print(user_handler.get_authorization_url())

oAuth = input("OAuth Verifier: ")

ACCESS_TOKEN, ACCESS_SECRET = user_handler.get_access_token(
    oAuth
)

auth = tweepy.OAuth1UserHandler(
   APIKEY, APISECRET,
   ACCESS_TOKEN, ACCESS_SECRET
)

api = tweepy.API(auth)

twitterClient = tweepy.Client(
    consumer_key=APIKEY,
    consumer_secret=APISECRET,
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
#    player = randomize(players)
    
    f_type = randomize(types)

    post = random.choice(texts)
    post = str(post).replace('\n', '')

    post = f'f"{post}"'
    post = eval(post)

    print(post + " " + datetime.now().strftime("%H:%M:%S"))  
    try:
        twitterClient.create_tweet(text = post)
        bskyClient.send_post(text= post)
        time.sleep(1799.5) # twitter takes .5 seconds to tweet, this makes it align every actual 30 minutes
    except tweepy.errors.Forbidden:
        print("Twitter error: tweepy.errors.Forbidden")
        time.sleep(10)
    except atproto.exceptions.AtProtocolError:
        print("Bluesky error: atproto.exceptions.AtProtocolError")
        time.sleep(10)