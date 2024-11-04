import tweepy
import dotenv
import os

post = open("post.txt", "r", encoding="utf-8")

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

twitterClient.create_tweet(text = post.readlines()[0])