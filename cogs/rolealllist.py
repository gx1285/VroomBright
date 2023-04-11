from discord.ext import commands
from discord import app_commands
import discord


class roleall_list(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="role_all_list", description="既存のロールを表示します。")
    async def rolealllist(self, i: discord.Interaction):
        guild = i.guild
        if len(guild.roles) > 1:
            role = "\n".join([r.mention for r in guild.roles][1:])
            embed = discord.Embed(title="ロール一覧", description=f"{role}", color=discord.Color.red())
            await i.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="エラー", description="ロールが見つかりませんでした。", color=discord.Color.red())
            await i.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(roleall_list(bot))
