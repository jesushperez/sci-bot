import tweepy
import requests
import config
from time import sleep
from api_init import create_api

# Creates API, called bot
bot = create_api()

# Sets up NewsAPI url
news_url = config.news_url + config.news_key

while True:
  # Get fresh news
  news = requests.get(news_url).json()
  articles = news['articles']

  for article in articles:
    # Formats string for each article and tweets it out.
    article_title = article['title']
    article_url = article['url']
    tweet_string = '"' + article_title + '" #Science #Gali #ScienceBot ' + article_url
    bot.update_status(tweet_string)
    sleep(900)