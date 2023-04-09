from discord.ext import commands
from discord import app_commands
import discord


class reverse(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="reverse", description="入力した文字を逆文字にして出力します。")
    @app_commands.describe(input="逆文字にしたい文字を入力してください。")
    async def reverse(self, i: discord.Interaction, input: str):
        reversed = input[::-1]

        conf_embed = discord.Embed(title="逆文字結果", color=discord.Color.green())
        conf_embed.add_field(name="結果", value=reversed)
  
        await i.response.send_message(embed=conf_embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(reverse(bot))
