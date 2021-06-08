import snscrape.modules.twitter as sntwitter
import pandas as pd
from pymongo import MongoClient


def scrape_tweets(username="elonmusk", iterations=math.Max, since=None):
    client = MongoClient()
    db = client["tweets"]
    for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(f"from:{username}").get_items()
    ):
        if iterations is not None:
            if i > iterations:
                break
        if since is not None:
            if tweet.date < since:
                break
        if tweet.inReplyToUser is None:
            tweet_dict = tweet_to_dict(tweet)
            try:
                db["tweets"].insert(tweet_dict)
            except Error as err:
                print(err)
    print("Done scraping tweets")


def tweet_to_dict(tweet):
    tweet_dict = {
        "Datetime": tweet.date,
        "Tweet_Id": tweet.id,
        "Text": tweet.content,
        "Username": tweet.user.username,
        "URL": tweet.url,
    }
    return tweet_dict
