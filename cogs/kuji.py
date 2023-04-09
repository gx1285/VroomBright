from discord.ext import commands
from discord import app_commands
import random
import discord


class kuji(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="kuji", description="くじ引きをします。")
    async def kuji(self, i: discord.Interaction):
        result = ["大吉", "中吉", "小吉", "凶", "大凶"]
        await i.response.send_message(f"結果: {random.choice(result)}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(kuji(bot))
