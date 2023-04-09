from discord.ext import commands
from discord import app_commands
import requests
import discord


class urlshort(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="url_short", description="URLを短縮できます。")
    @app_commands.describe(url="短縮したいURLを入力してください。")
    async def url_short(self, i: discord.Interaction, url: str):
        apiurl = "https://is.gd/create.php?format=json&url="
        response = requests.get(apiurl+url)
        json_response = response.json()
        if 'shorturl' in json_response:
            conf_embed = discord.Embed(title="短縮結果", color=discord.Color.green())
            conf_embed.add_field(name="こちらが短縮されたURLです！", value=json_response['shorturl'])
  
            await i.response.send_message(embed=conf_embed)
        else:
            conf_embed = discord.Embed(title="短縮結果", color=discord.Color.red())
            conf_embed.add_field(name="エラー", value="URLを確認して、もう一度お試しください。")
  
            await i.response.send_message(embed=conf_embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(urlshort(bot))
