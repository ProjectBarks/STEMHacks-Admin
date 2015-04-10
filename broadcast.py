import webapp2
import json
from google.appengine.ext import vendor
vendor.add("libs")
import tweepy
from twilio.rest import TwilioRestClient

#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY,  )

#api = tweepy.API(auth)
#api.update_status('Updating using OAuth authentication via Tweepy!')

data = json.load(open("config/broadcaster.json"))
twillio = TwilioRestClient(data["twillio"]["id"], data["twillio"]["token"])