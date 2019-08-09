import tweepy
import requests
from api_init import create_api

bot = create_api()

bot.update_status("Hello, World! I'm Gali, the science bot!")