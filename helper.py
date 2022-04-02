import pickle
import time

def writeSettings(user_name,password,settings_file):
    api = Client(user_name,password)
    pickle.dump(api.settings,open(settings_file,"wb"))

def readSettings(settings_file):
    return pickle.load(open(settings_file,"rb"))

def get_all_followers(client, user_id):
    rank_token = client.uuid
    followers = []
    max_id = None
    while True:
        try:
            if max_id is not None:
                results = client.user_followers(user_id, rank_token, max_id=max_id)
            else:
                results = client.user_followers(user_id, rank_token)
        except socket.timeout:
            time.sleep(1)
            continue
        max_id = results.get("next_max_id")
        followers.extend(results['users'])
        if max_id is None:
            break
        time.sleep(0.5)
    return followers

def get_all_following(client, user_id):
    rank_token = client.uuid
    following = []
    max_id = None
    while True:
        try:
            if max_id is not None:
                results = client.user_following(user_id, rank_token, max_id=max_id)
            else:
                results = client.user_following(user_id, rank_token)
        except socket.timeout:
            time.sleep(1)
            continue
        max_id = results.get("next_max_id")
        following.extend(results['users'])
        if max_id is None:
            break
        time.sleep(0.5)
    return following
