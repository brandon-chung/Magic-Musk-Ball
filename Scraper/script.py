import scraper
import json
import datetime
import pytz

with open("config.json", "r") as f:
    config = json.load(f)

new_date = pytz.utc.localize(datetime.datetime.now())
new_date = new_date.strftime(f"%m/%d/%Y, %H:%M:%S {new_date.tzinfo}")
last_update = config.get("last_update", None)
last_update = datetime.datetime.strptime(
    last_update, f"%m/%d/%Y, %H:%M:%S {utc_now.tzinfo}"
)
last_update = pytz.utc.localize(last_update)

scraper.scrape_tweets(since=last_update)
config["last_update"] = new_date

with open("config.json", "w") as f:
    json.dump(config, f)
