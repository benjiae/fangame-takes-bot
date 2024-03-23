import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

BEARER = os.getenv("BEARER_TOKEN")

client = tweepy.Client(BEARER, )

client.create_tweet(text = "test")