A simple twitter/bluesky bot that posts fangame related stuff every 30 minutes

"Official" Account pages:
- https://twitter.com/badfangametakes
- https://bsky.app/profile/fangametakes.bsky.social


# Installation:

## Beforehand:

0.1: Get the dependencies:
- python-dotenv
- tweepy
- atproto
- (i'm pretty sure)

0.2: [Make a Twitter application](https://developer.twitter.com/) and setup a bluesky bot account
## Setup:

1. make a .env file that follows this example:
```
BSKYHANDLE= Bluesky handle
BSKYPASSWORD= Bluesky password

TWITTER_API_KEY= Twitter Api Key
TWITTER_API_SECRET= Twitter Api Secret
```

2. Run ```main.py```

3. congrats it works


# Modification:

There are a few TXT Files that contain some variables (fangames, events, spreadsheets, types and texts), you can edit them, but "text.txt" contains the randomized tweets.

Edit main.py to fit your needs.


# Contributing:

make a pr and i'll probably accept it

make an issue and i'll probably fix it
