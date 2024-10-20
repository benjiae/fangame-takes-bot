import dotenv
import tweepy
import atproto
import os
import time
from datetime import datetime
import random

def readfile(file):
    files = open("/home/user/bots/fangame-takes-bot/text/" + file + ".txt", "r", encoding="utf8")
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

# Variables
twtApiKey = os.getenv("TWITTER_API_KEY")
twtApiSecret = os.getenv("TWITTER_API_SECRET")
twtAccessToken = os.getenv("TWITTER_ACCESS_TOKEN")
twtAccessSecret = os.getenv("TWITTER_ACCESS_SECRET")

bskyHandle = os.getenv("BSKYHANDLE")
bskyPassword= os.getenv("BSKYPASSWORD")

twitterClient = tweepy.Client(
    consumer_key=twtApiKey,
    consumer_secret=twtApiSecret,
    access_token=twtAccessToken,
    access_token_secret=twtAccessSecret
)

blueskyClient = atproto.Client()
blueskyProfile = blueskyClient.login(bskyHandle, bskyPassword)

def post(tweet):
    print("Posting this in 10 seconds:")
    print(tweet)
    time.sleep(10)
    try:
        twitterClient.create_tweet(text = tweet)
        blueskyClient.send_post(text = tweet)
        print("Posted at: " + datetime.now().strftime("%H:%M:%S"))
    except tweepy.errors.Forbidden as tweepy:
        print("tweepy.errors.Forbidden | probably repeated")
        with open("errors.txt", "w", encoding="utf8") as f:
            f.write(datetime.now().strftime("%H:%M:%S"))
            f.write(f"Tweepy error: {tweepy=}")
            f.write("==============================================================")
            f.close()
post(get_post())
