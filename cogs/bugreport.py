from discord.ext import commands
from discord import app_commands
import discord


class report(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="bugreport", description="バグ報告をします。")
    @app_commands.describe(report_description="バグ報告する内容を入力してください。")
    async def bugreport(self, i: discord.Interaction, report_description: str):
        channel = self.get_channel(1095604986051842138)
        await channel.send(f"{str(report_description)} - {i.user}|{i.user.id}")
        await i.response.send_message("報告しました。ご協力ありがとうございます。", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(report(bot))
