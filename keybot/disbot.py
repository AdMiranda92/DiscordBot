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
    description = "A Wow Bot to help automate information gathering and handling for guilds"
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    # Wow API Access Token Renewal
    ACCESS_TOKEN = create_access_token(os.getenv('WOW_ID'), os.getenv('WOW_SECRET'))
    bot = CustomClient.CustomBot(ACCESS_TOKEN=ACCESS_TOKEN['access_token'], command_prefix='!', description=description)
    bot.run(TOKEN)


if __name__ == '__main__':
    # more setup will be in this section later on
    # for now, simply call main and let the bot run
    main()