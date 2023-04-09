from discord.ext import commands
from discord import app_commands
import discord

class BotInvite(discord.ui.View):
  def __init__(self, inv: str):
    super().__init__()
    self.inv = inv
    self.add_item(discord.ui.Button(label="ボット招待リンク", url=self.inv))

class about(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="about", description="このbotの情報を表示します。")
    async def about(self, i: discord.Interaction):
        inv = "https://discord.com/oauth2/authorize?client_id=1086503771309342830&permissions=8&scope=bot%20applications.commands"
        await i.response.send_message("このボットは1人により作られました。\n招待URL: https://dsc.gg/vbinvite", view=BotInvite(str(inv)))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(about(bot))
