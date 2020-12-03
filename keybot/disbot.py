# discord world of warcraft bot
import CustomClient

import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth


def create_access_token(client_id, client_secret, region = 'us'):
    url = "https://%s.battle.net/oauth/token" % region
    body = {"grant_type": 'client_credentials'}
    auth = HTTPBasicAuth(client_id, client_secret)
    response = requests.post(url, data=body, auth=auth)
    
    return response.json()

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')
    # Wow API Access Token Renewal
    ACCESS_TOKEN = create_access_token(os.getenv('WOW_ID'), os.getenv('WOW_SECRET'))
    bot = CustomClient.CustomBot(GUILD=GUILD, ACCESS_TOKEN=ACCESS_TOKEN['access_token'], command_prefix='!')
    bot.run(TOKEN)



main()
