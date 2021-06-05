import snscrape.modules.twitter as sntwitter
import pandas as pd
from pymongo import MongoClient


# Using TwitterSearchScraper to scrape data and append tweets to list
def scrape_tweets(username="elonmusk", iterations=math.Max, since=None):
    # Creating list to append tweet data to
    tweets_list1 = []
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
            tweets_list1.append(
                [tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.URL]
            )

    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(
        tweets_list1, columns=["Datetime", "Tweet Id", "Text", "Username", "URL"]
    )
    tweets_df = tweets_df1.set_index("Tweet Id")
    return tweets_df1
