from discord.ext import commands
from discord import app_commands
import discord


class purge(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="purge", description="メッセージを一括削除できます。")
    @app_commands.describe(number="削除したいメッセージの数を入力してください。")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def purge(self, i: discord.Interaction, number: int):
        deleted = await i.channel.purge(limit=number)
        conf_embed = discord.Embed(title="成功", color=discord.Color.green())
        conf_embed.add_field(name="削除しました", value=f"{len(deleted)}メッセージ削除しました。")

        await i.response.send_message(embed=conf_embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(purge(bot))
