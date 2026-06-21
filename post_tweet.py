import os
import tweepy
from gradio_client import Client

# 1. generate a tweet from your Space
space = Client("iloveworldpeace/tweetbot2", token=os.environ["HF_TOKEN"])
tweet_text = space.predict(0.9, 1, api_name="/generate")
tweet_text = tweet_text.strip()[:280]

# 2. set up the X client
client = tweepy.Client(
    consumer_key=os.environ["X_API_KEY"],
    consumer_secret=os.environ["X_API_SECRET"],
    access_token=os.environ["X_ACCESS_TOKEN"],
    access_token_secret=os.environ["X_ACCESS_SECRET"],
)

# 3. diagnostic: check credentials, then try to post
try:
    me = client.get_me()
    print("Credentials OK. Logged in as:", me.data.username)
except Exception as e:
    print("get_me() failed:", repr(e))
    if getattr(e, "response", None) is not None:
        print("X response:", e.response.text)

try:
    client.create_tweet(text=tweet_text)
    print("Posted!")
except Exception as e:
    print("create_tweet failed:", repr(e))
    if getattr(e, "response", None) is not None:
        print("X response:", e.response.text)
