from generate_post import get_post
from get_access_keys import get_keys
from make_post import post
from time import sleep

get_keys()

while True:
    try:
        post(get_post())
        sleep(1790) # make time for the 10 seconds of confirmation
    except tweepy.errors.Forbidden:
        print("tweepy.errors.Forbidden | probably repeated")
        sleep(10)
