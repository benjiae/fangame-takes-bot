import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

APIKEY = os.getenv("API_KEY")
APISECRET = os.getenv("API_SECRET")
CALLBACK = "http://localhost:8000"

user_handler = tweepy.OAuth1UserHandler(
    APIKEY, APISECRET,
    callback=CALLBACK
)

print(user_handler.get_authorization_url())

oAuth = input("OAuth Verifier: ")

ACCESS_TOKEN, ACCESS_SECRET = user_handler.get_access_token(
    oAuth
)

print("Access Token: " + ACCESS_TOKEN + ", Access Secret: " + ACCESS_SECRET)