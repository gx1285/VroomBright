import discord
from discord.ext import commands
from discord import app_commands
import urllib.parse


class gosenchouen(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
    @app_commands.describe(
        bottom="下部文字列",
        top="上部文字列",
    )
    @app_commands.command(name="5000", description="5000兆円ほしいを生成します。")
    async def gosenchouen(
        self,
        i: discord.Interaction,
        top: str,
        bottom: str,
    ):
        embed = discord.Embed(title="5000兆円ほしい!!", color=0x3498DB).set_image(
            url=f"https://gsapi.cbrx.io/image?top={urllib.parse.quote(top)}&bottom={urllib.parse.quote(bottom)}"
        )
        await i.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(gosenchouen(bot))
