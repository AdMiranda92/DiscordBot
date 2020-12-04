This is a personal project to create a discord bot to interact with World of Warcraft guild serverss in order
to provide on-demand information and recommendations. Interfacing with this bot is done via commands that begin with
the '!' prefix (i.e !help, !keys)

Goals:
The purpose of this project is to learn how to use both the Blizzard API and the Discord API. As this is a personal learning project
there will be many revisions of code and design as I learn more about the way the Discord API works.

--UPDATE 12/3/20--
Discord uses Cogs to simplify adding commands to a bot

Cogs allow commands to be split by file, and loaded as necessary. Will need to look into fragmenting the custom bot
class to avoid putting too much into one class - for now, even though it will incur technical debt, the goal is to learn the API.
No changes will be made for now. 
