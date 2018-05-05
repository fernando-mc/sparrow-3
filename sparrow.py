#!/usr/bin/env python
import random
import json
from twython import Twython

# Normally, NEVER put your credentials in a file like this
# These are credentials for a throwaway account
CONSUMER_KEY = "TFC1fmZfczFsGMQxzxNVWfl8r"
CONSUMER_SECRET = "qZcUSG1tHz3szLukxAEXhnbEcupVYo6XjrGGD3Z1cy1PNw1s0n"
ACCESS_TOKEN_KEY = "730011964911407105-YRqShkDRTOq83F24kgTuHN7fmibSjCD"
ACCESS_TOKEN_SECRET = "SupI50NhW8EEl1HJ6zO5YODwdefo9qqCTKSVwWW1LmpM7"

# Create the Twython Twitter client using our credentials
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                  ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

# Sample random tweets
potential_tweets = [ ] # Add your own tweets (as a string) in here!

def send_tweet():
    """Sends a random tweet to Twitter from a list of potential tweets"""
    tweet = random.choice(potential_tweets)
    twitter.update_status(status = tweet)

send_tweet()

# Then check for the Tweet here:
# https://twitter.com/salutations_bot
