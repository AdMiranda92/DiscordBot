
from descriptions import Descriptions as des

import requests
import random
import discord
from discord.ext import commands


class CustomBot(commands.Bot):
    
    def __init__(self, ACCESS_TOKEN, **options):
        super().__init__(**options)
        self.remove_command('help')
        self.add_custom_commands()
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.default_realm = None
    
    async def on_ready(self):
        print('[CONNECTING]...')
        print(f'[CONNECTED]... {self.user} has connected to Discord')


    
    def add_custom_commands(self):
        r'''function to add all commands to the bot'''
        
        @self.command(name='keys')
        async def test(ctx, *args, season=1):
            await ctx.send(f'Looking up {args}')
            # lookup every toon in args and setup the url properly
            for toon in args:
                toon_data = toon.split('-')
                # name and realm given
                if len(toon_data) == 2:
                    api_endpoint = f'https://us.api.blizzard.com/profile/wow/character/{toon_data[1]}/{toon_data[0]}/'\
                                    f'mythic-keystone-profile/season/{season}?namespace=profile-us&locale=en_US&access_token={self.ACCESS_TOKEN}'
                # name only - use default realm
                elif len(toon_data) == 1:
                    if self.default_realm is None:
                        await ctx.send(f'I don\'t have a default realm assigned to look up {toon}! Set a default with \"!setrealm <realm>\"'\
                                        'or pass the name with a realm like so: \"name-realm\"!')
                        continue
                    api_endpoint = f'https://us.api.blizzard.com/profile/wow/character/{self.default_realm}/{toon_data[0]}/'\
                                    f'mythic-keystone-profile/season/{season}?namespace=profile-us&locale=en_US&access_token={self.ACCESS_TOKEN}'
                else:
                    break
                
                # TODO ------------------------------------------------------------
                # ONCE MYTHIC SEASON BEGINS, THIS DATA WILL NO LONGER RETURN 404
                # USE THE JSON RETURNED TO FINISH THIS COMMANDS PURPOSE
                
                await ctx.send(f'Mythic Keystone Data for {toon}:')
                try:
                    data = requests.get(api_endpoint)
                    if data.status_code == 404:
                        await ctx.send(f'{toon} has not completed any mythic keys this season *sad panda noises*')
                except:
                    pass


        @self.command(name='snitch')
        async def snitch(ctx, guild='hollowed'):
            pass
        


        @self.command(name='setrealm')
        @commands.has_any_role('Anger Beard', 'Officer')
        async def setrealm(ctx, *args):
            if len(args) == 0:
                await ctx.send('Please speficy a realm to set as default! For example: \"!setrealm zuljin\"')
                return
            try:
                self.default_realm = args[0]
                await ctx.send(f'Default realm has been set to {args[0]}!')
            except:
                pass
        
        @self.command(name='help')
        async def help(ctx):
            embed = discord.Embed(
                colour = discord.Colour.teal()
                )
            
            embed.set_author(name='What I Can Do')
            embed.add_field(name='!keys', value=des.keys_command, inline=False)
            embed.add_field(name='!snitch', value=des.snitch_command, inline=False)
            embed.add_field(name='!setrealm', value=des.setrealm_command, inline=False)

            await ctx.send(embed=embed)