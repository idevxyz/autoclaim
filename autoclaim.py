import time
from telethon import TelegramClient, sync, events

from telethon.tl.functions.messages import (
    GetHistoryRequest,
    GetBotCallbackAnswerRequest,
)
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json, re, sys, os


try:
   import requests
except:
   os.system("pip install requests")
   import requests 
   
try:
   import bs4
except:
   os.system("pip install bs4")
   import bs4       


try:
    import webbrowser
    import requests
    from bs4 import BeautifulSoup
except:
    print(
        "\033[1;30m# \033[1;31mHmmm Sepertinya Modul Requests Dan Bs4 Belum Terinstall\n\033[1;30m# \033[1;31mTo install Please Type pip install requests and pip install bs4"
    )
    sys.exit



c = requests.session()

for i in range(5000000):
        sys.stdout.write("\r")
        sys.stdout.write("\033[1;30m \n\033[1;33m ⏩ DOGEUP BOT VERSION 1.0")
        sys.stdout.flush() 
        sleep(2)
        os.system("clear")
        break


banner = """\033[0;35m   
\033[0;36m✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘
                                                              
   ░ █▄  █ █▀▀ █  █ ▀▀█▀▀ █▀▀█ █▀▀█ █   　  
   ░ █ █ █ █▀▀ █  █   █   █▄▄▀ █▄▄█ █   　  
   ░ █  ▀█ ▀▀▀ ▀▀▀▀   ▀   ▀ ▀▀ ▀  ▀ ▀▀▀ 　  

          █▀▀█ █▀▀█ █▀▄▀█ █  █ ░
          █▄▄█ █▄▄▀ █ ▀ █ █▄▄█ ░
          █  █ ▀─▀▀ ▀   ▀ ▄▄▄█ ░
 
\033[0;36m✘✘✘✘✘✘✘✘✘✘✘ [BORN TO HACK] ✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘✘

\033[1;32m🔷Script Credit \033[1;31m   :\033[1;0m Neutral Army
\033[1;32m🔷Telegram Channel \033[1;31m:\033[1;0m @Neutralarmy
\033[1;32m🔷Telegram Group\033[1;31m   : \033[1;0m@Neutralarmydiscuss
\033[1;32m🔷Youtube Channel\033[1;31m  :\033[1;0m @Neutral Army
\n\033[1;32m❒❒❒❒❒❒❒❒❒❒❒ [DOGE MOON BOT] ❒❒❒❒❒❒❒❒❒\n\n"""


print(banner)
c = requests.Session()
if not os.path.exists('session'):
     os.makedirs('session')
print(banner)
if len(sys.argv) < 2:
    print("\n\n\n\033[1;32mUsage : python autoclaim.py  Your no. with country code")
    sys.exit(1)

    

def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(
            "\033[1;30m#\033[1;0m{:2d} \033[1;32mseconds remaining".format(remaining)
        )
        sys.stdout.flush()
        sleep(1)


ua = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
}


api_id = 5785894
api_hash = "3bbd832921adc222850990108fc9cb39"
phone_number = sys.argv[1]

client = TelegramClient("session/" + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input("\n\n\n\033[1;0mEnter Your OTP received in Telegram: "))
    except SessionPasswordNeededError:
        passw = input("\033[1;0mEnter Your 2fa Password : ")
        me = client.start(phone_number, passw)
myself = client.get_me()
os.system("clear")
print(banner)
print(
    "\033[1;31m ➢️ Welcome  User\033[1;0m:",
    myself.first_name,
    "\n\033[1;0m ➢ [Doge Up is running Now]",
)



print("\n\n\033[1;37mTask: Auto Claim Bonus ")
try: 
    channel_entity = client.get_entity("@@free_dogcoin_bonus_bot")
    channel_username = "@free_dogcoin_bonus_bot"
    client.send_message(entity=channel_entity, message="/start 1878756731 \n")
    for i in range(5000000):
        sys.stdout.write("\r")
        sys.stdout.write(
            "                                                              "
        )
        sys.stdout.write("\r")
        sys.stdout.write("\033[1;30m# \033[1;33mClaiming Bonus🎁\n\n")
        client.send_message(entity=channel_entity, message="🎰 Bonus\n")    
        print("\033[1;30m# \033[0;36mYou have Sucessfully Claimed Bonus🎁\n\n") 
        sleep(5)
        posts = client(
            GetHistoryRequest(
                peer=channel_entity,
                limit=2,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0,
            )
        )
        message = posts.messages[0].message
        print(message)
        sys.stdout.flush()
        time.sleep(5)
        
        seconds = int(3605)
        for i in range (seconds) :
            print ( "\nWait "+ str (seconds - i)+" Seconds for Next Claim" )
            time.sleep(1)    
        posts = client(
            GetHistoryRequest(
                peer=channel_entity,
                limit=1,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0,
            )
        )
        if (
            posts.messages[0].message.find("Sorry, there are no new ads available")
            != -1
        ):
            print("\n\033[1;30m# \033[1;31mNo site remains to visit❌\n")
         
               
finally:
    client.disconnect()
