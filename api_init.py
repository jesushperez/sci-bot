import tweepy
import config

def create_api():
  # imports key and token values from config file
  consumer_key = config.consumer_key
  consumer_secret_key = config.consumer_secret_key
  access_token = config.access_token
  access_token_secret = config.access_token_secret

  # Authenticates twitter credentials
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
  auth.set_access_token(access_token, access_token_secret)

  # Creates and returns API
  api = tweepy.API(auth)
  return api