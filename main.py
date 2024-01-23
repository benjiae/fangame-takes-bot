from dotenv import load_dotenv
import os
import tweepy
import time
import random

def readfile(file):
    files = open(file, "r")
    array = []

    for i in files:
        array.append(i)

    files.close()
    return array

def randomize(vari):
    temp = [random.choice(vari), random.choice(vari)]

    text = list(map(lambda string: string.rstrip(), temp))

    return text

fangames = readfile("fangames.txt")
makers = readfile("makers.txt")
events = readfile("events.txt")
spreadsheets = readfile("spreadsheets.txt")
players = readfile("players.txt")
texts = readfile("text.txt")

##################################################

endpoint = "api.twitter.com/2/tweets"

load_dotenv()

BEARER = os.getenv("BEARER_TOKEN")
APIKEY = os.getenv("API_KEY")
APISECRET = os.getenv("API_SECRET")
CLIENTSECRET = os.getenv("CLIENT_SECRET")
CLIENTID = os.getenv("CLIENT_ID")
CALLBACK = "http://localhost:8000"

oauth1_user_handler = tweepy.OAuth1UserHandler(
    APIKEY, APISECRET,
    callback=CALLBACK
)

print(oauth1_user_handler.get_authorization_url())

oAuth = input("OAuth Verifier: ")

ACCESS_TOKEN, ACCESS_SECRET = oauth1_user_handler.get_access_token(
    oAuth
)

auth = tweepy.OAuth1UserHandler(
   APIKEY, APISECRET,
   ACCESS_TOKEN, ACCESS_SECRET
)

api = tweepy.API(auth)

client = tweepy.Client(
    consumer_key=APIKEY,
    consumer_secret=APISECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

####################################
while True:
    fangame = randomize(fangames)
    maker = randomize(makers)
    event = randomize(events)
    spreadsheet = randomize(spreadsheets)
    player = randomize(players)

    tweet = random.choice(texts)
    tweet = str(tweet).replace('\n', '')

    tweet = f'f"{tweet}"'
    client.create_tweet(text = eval(tweet))
    time.sleep(1800)