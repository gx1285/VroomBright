from discord.ext import commands
from discord import app_commands
import requests
from os import environ
import discord

CSE = environ['cse']
APIKEY = environ['apikey1']

def get_url(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={APIKEY}&cx={CSE}&q={query}&num=1&fields=items(link)"
    response = requests.get(url).json()
    return response['items'][0]['link']

class search(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="search", description="入力した内容で最も近い候補を表示します。")
    @app_commands.describe(search="検索したい内容を入力してください。")
    async def search(self, i: discord.Interaction, search: str):
        url = get_url(search)
        await i.response.send_message(url)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(search(bot))
