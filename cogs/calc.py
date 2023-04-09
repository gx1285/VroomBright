from discord.ext import commands
from discord import app_commands
import requests
from os import environ
import discord

app_id = environ['appid']

class calc(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="calc", description="計算します。")
    @app_commands.describe(equation="計算したい数字を入力してください。(例: 10x10）")
    async def calc(self, i: discord.Interaction, equation: str):
        response = requests.get(f"http://api.wolframalpha.com/v2/query?appid={app_id}&input={equation}&output=json")
        result = response.json()['queryresult']['pods'][1]['subpods'][0]['plaintext']
        conf_embed = discord.Embed(title="計算結果", color=discord.Color.green())
        conf_embed.add_field(name="結果", value=result)
  
        await i.response.send_message(embed=conf_embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(calc(bot))
