from discord.ext import commands
from discord import app_commands
import requests
from os import environ
import discord

app_id = environ['appid']

class calc(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.choices(
        mode=[
            app_commands.Choice(name="足し算", value="+"),
            app_commands.Choice(name="引き算", value="-"),
            app_commands.Choice(name="掛け算", value="x"),
            app_commands.Choice(name="割り算", value="/")
        ]
    )
    @app_commands.command(name="calc", description="計算します。")
    @app_commands.describe(num1="値を入力してください。", num2="値を入力してください。", mode="計算したいモードを選んでください。")
    async def calc(self, i: discord.Interaction, num1: str, num2: str, mode: str):
        response = requests.get(f"http://api.wolframalpha.com/v2/query?appid={app_id}&input={num1}{mode}{num2}&output=json")
        result = response.json()['queryresult']['pods'][1]['subpods'][0]['plaintext']
        conf_embed = discord.Embed(title="計算結果", color=discord.Color.green())
        conf_embed.add_field(name="結果", value=result)
  
        await i.response.send_message(embed=conf_embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(calc(bot))
