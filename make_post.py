import dotenv
import tweepy
import atproto
import os
import time
from datetime import datetime

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
    twitterClient.create_tweet(text = tweet)
    blueskyClient.send_post(text = tweet)
    print("Posted at: " + datetime.now().strftime("%H:%M:%S"))