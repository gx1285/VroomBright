from discord.ext import commands
from discord import app_commands
import requests
from bs4 import BeautifulSoup
import discord

class search(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="search", description="入力した内容で最も近い候補を表示します。")
    @app_commands.describe(search="検索したい内容を入力してください。")
    async def search(self, i: discord.Interaction, search: str):
        url = f"https://www.google.com/search?q={search}"
        headers = {"User-Agent": "VroomBright/1.0(DiscordBot)"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        titles = [title.get_text() for title in soup.find_all('h3')]

        if len(titles) == 0:
            await i.response.send_message(f"'{search}'に関する検索結果は見つかりませんでした。")
        else:
            response = "\n".join(titles)
            await i.response.send_message(f"'{search}'での検索結果の上位表示は以下の通りです。\n{response}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(search(bot))
