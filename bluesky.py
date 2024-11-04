import atproto
import dotenv
import os

dotenv.load_dotenv()

post = open("post.txt", "r", encoding="utf-8")

bskyHandle = os.getenv("BSKYHANDLE")
bskyPassword = os.getenv("BSKYPASSWORD")

blueskyClient = atproto.Client()
blueskyProfile = blueskyClient.login(bskyHandle, bskyPassword)


blueskyClient.send_post(text = post.readlines()[0])