from discord.ext import commands
from discord import app_commands
import requests
from os import environ
import discord

newsapi = environ['newsapi']

class news(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="news", description="最新のニュースを表示します。")
    async def news(self, i: discord.Interaction):
        url = "https://newsapi.org/v2/top-headlines?country=jp&apiKey={}".format(newsapi)
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            articles = data["articles"]
            embed = discord.Embed(title="最新のニュース", color=0x00ff00)
            for article in articles[:5]: # 最新の5つの記事をEmbedに組み込む
              title = article["title"]
              url = article["url"]
              embed.add_field(name=title, value="[記事全文はこちら]({})\n{}".format(url, '-'*50), inline=False)
            await i.response.send_message(embed=embed)
        else:
            await i.response.send_message("ニュースの取得に失敗しました。")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(news(bot))
