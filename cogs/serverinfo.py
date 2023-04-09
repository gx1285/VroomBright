from discord.ext import commands
from discord import app_commands
import discord


class serverinfo(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="serverinfo", description="サーバーの詳細を表示します。")
    async def ping(self, i: discord.Interaction):
        guild = i.guild
        roles = [role for role in guild.roles]
        text_channel = [text_channels for text_channels in guild.text_channels]
        p = discord.Color.purple()
        title = "サーバー詳細"
        embed = discord.Embed(title=title, timestamp=i.created_at, color=p)
        embed.add_field(name="チャンネル数", value=f"{len(text_channel)}")
        embed.add_field(name="ロール数", value=f"{len(roles)}")
        embed.add_field(name="サーバーブースター", value=guild.premium_subscription_count)
        embed.add_field(name="メンバー数", value=guild.member_count)
        embed.set_thumbnail(url=i.guild.icon)
        if i.user.avatar is None:
          embed.set_footer(
            text=f"実行者: {i.user} ",
            icon_url=i.user.default_avatar,
          )
        else:
          embed.set_footer(
           text=f"実行者: {i.user} ",
          icon_url=i.user.avatar,
        )
        await i.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(serverinfo(bot))
