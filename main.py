import os
from insta_follower import InstaFollower

SIMILAR_ACCOUNT = ""
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

bot = InstaFollower()
bot.login(USERNAME, PASSWORD)
bot.get_followers(SIMILAR_ACCOUNT)
bot.follow()
