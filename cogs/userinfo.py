from discord.ext import commands
from discord import app_commands
import discord


class userinfo(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.describe(user="ユーザーを指定してください。")
    @app_commands.command(name="userinfo", description="指定したユーザーの情報を表示します。")
    async def ping(self, i: discord.Interaction, user: discord.User):
        embed = discord.Embed(title=f"{user.name}のユーザー情報", url=f"https://discord.com/users/{user.id}")
        base = "https://media.discordapp.net/avatars"
        if hasattr(user.avatar, "key"):
            embed.set_author(
                name=f"{user.name}#{user.discriminator}の情報",
                icon_url=f"{base}/{user.id}/{user.avatar.key}.png",
            )
            embed.set_thumbnail(url=f"{base}/{user.id}/{user.avatar.key}.png")
        else:
            embed.set_author(
                name=f"{user.name}#{user.discriminator}",
                icon_url=user.default_avatar.url,
            )
            embed.set_thumbnail(url=user.default_avatar.url)
        if user.bot is True:
            b = "はい"
        else:
            b = "いいえ"
        if user.system is True:
            c = "はい"
        else:
            c = "いいえ"
        embed.add_field(
            name="アカウント作成日時", value=discord.utils.format_dt(user.created_at, "f")
        )
        embed.add_field(name="ユーザー名", value=user.name)
        embed.add_field(name="UserID", value=f"`{user.id}`")
        embed.add_field(name="タグ", value=f"`{user.discriminator}`")
        embed.add_field(name="Botアカウント", value=b)
        embed.add_field(name="システムユーザー", value=c)
        await i.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(userinfo(bot))
