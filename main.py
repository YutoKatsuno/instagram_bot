import os
from insta_follower import InstaFollower

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

bot = InstaFollower()
bot.login(USERNAME, PASSWORD)
bot.find_followers()
bot.follow()
