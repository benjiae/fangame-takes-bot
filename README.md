A simple twitter bot that tweets fangame related stuff every 30 minutes\
"Official" Account page: https://twitter.com/badfangametakes

# Installation:
## Beforehand:
0.1: Get the dependencies:
  - python-dotenv
  - tweepy\
0.2: [Make a Twitter application](https://developer.twitter.com/)

## Setup:
1. make a .env file that contains these variables (and fill them with your ones):
   - BEARER_TOKEN, API_KEY, API_SECRET, CLIENT_SECRET, CLIENT_ID

2. Run the executable, it will send you a twitter URL and will ask you for the OAuth verifier, enter the URL, authorize and on the page that it returns to (which will fail), get the "oauth_verifier" argument
###### TODO: Automate it

3. congrats it works

# Modification:
There are a few TXT Files that contain some variables (fangames, events, spreadsheets and texts), you can edit them, but "text.txt" contains the randomized tweets.\
Edit main.py to fit your needs.

# Contributing:
make a pr and i'll probably accept it\
make an issue and i'll probably fix it
