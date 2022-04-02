from instagram_private_api import Client, ClientCompatPatch
import json
import os
import helper
import time
from socket import *
import pickle
from dotenv import load_dotenv


# get login info for bot account
load_dotenv('secrets.env')
user_name = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# user id of account i care about 
user_id = 530285848

# cache da cookies
if not os.path.exists("settingObj"):
    helper.writeSettings(user_name,password,"settingObj")
cache_settings = helper.readSettings("settingObj")

api = Client(user_name, password, settings=cache_settings)

# variabools
following = []
stinkies = []
whitelist = []

# gather followers
followers = helper.get_all_followers(api, user_id)

# gather following
following = helper.get_all_following(api, user_id)

# gather stinkies (not following back & not whitelisted)
for user in following:
    if user in followers and user not in whitelist:
        stinkies.append(user)


print(len(followers))
print(len(following))
print(len(stinkies))