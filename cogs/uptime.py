from discord.ext import commands
from discord import app_commands
import discord


class uptime(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="uptime", description="Botの起動時間を表示します。")
    async def uptime(self, i: discord.Interaction):
        await i.response.send_message(f"<t:{self.bot.uptime}:F>")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(uptime(bot))
