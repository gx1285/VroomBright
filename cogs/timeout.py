from discord.ext import commands
from discord import app_commands
import datetime
import discord


class timeout(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
    
    @app_commands.choices(
        option=[
            app_commands.Choice(name="分数", value="m"),
            app_commands.Choice(name="秒数", value="s")
        ]
    )
    @app_commands.command(name="timeout", description="メンバーをミュートできます。")
    @app_commands.describe(member="ミュートしたい相手を選んでください。",time="ミュートしたい時間を入力してください。",option="分数か秒数を選んでください。")
    @app_commands.checks.has_permissions(mute_members=True)
    async def timeout(self, i: discord.Interaction, member: discord.Member, time: int, option: str):
        timelimit = f"{time}{option}"
        if "s" in timelimit:
          gettime = timelimit.strip("s")
          if int(gettime) > 2678400:
            await i.response.send_message("ミュート時間は31日より大きくできません。")
          else:
              newtime = datetime.timedelta(seconds=int(gettime))
              await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
              conf_embed = discord.Embed(title="成功", color=discord.Color.green())
              conf_embed.add_field(name="ミュートしました", value=f"{member}をミュートしました。")

              await i.response.send_message(embed=conf_embed)
        elif "m" in timelimit:
          gettime = timelimit.strip("m")
          if int(gettime) > 44640:
            await i.response.send_message("ミュート時間は31日より大きくできません。")
          else:
              newtime = datetime.timedelta(minutes=int(gettime))
              await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
              conf_embed = discord.Embed(title="成功", color=discord.Color.green())
              conf_embed.add_field(name="ミュートしました", value=f"{member}をミュートしました。")

              await i.response.send_message(embed=conf_embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(timeout(bot))
