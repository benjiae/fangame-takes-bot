import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

apiKey = os.getenv("TWITTER_API_KEY")
apiSecret = os.getenv("TWITTER_API_SECRET")
twtAccessToken = os.getenv("TWITTER_ACCESS_TOKEN")
twtAccessSecret = os.getenv("TWITTER_ACCESS_SECRET")
callback = "http://localhost:8000"

def get_keys():
    if twtAccessToken == ("" or None) or twtAccessSecret == ("" or None):
        user_handler = tweepy.OAuth1UserHandler(
            apiKey, apiSecret,
            callback=callback
        )

        print(user_handler.get_authorization_url())

        oAuth = input("Twitter OAuth Verifier: ")

        accessToken, accessSecret = user_handler.get_access_token(
            oAuth
        )

        print("TWITTER_ACCESS_TOKEN=" + accessToken)
        print("TWITTER_ACCESS_SECRET=" + accessSecret)
        print("Please save them on your .env file")
        exit()