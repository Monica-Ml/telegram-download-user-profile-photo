from telethon import TelegramClient, events, sync

# API variables
api_id =  # Your api_id (int)
api_hash = "" # Your api_hash

# Making Client Object
client = TelegramClient("session", api_id, api_hash)
client.start()

# download photo from profile
# usernames = ["username1", "username2", "username3"] # for 3 user
usernames = ["test123"] # target username on telegram (string)

for username in usernames:
    photo = client.download_profile_photo(username)
    print("{} saved !".format(photo))

client.log_out()
client.disconnect()
