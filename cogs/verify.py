from discord.ext import commands
from discord import app_commands
import discord
from replit import db

def verify_db(key, data):
    db[f"verify_1_db_{key}"] = data

def verify_db_get(key):
    return db[f"verify_1_db{key}"]

class Button1(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="認証", style=discord.ButtonStyle.primary, custom_id="verify_type_1"
        )

class verify(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.Cog.listener(name="on_interaction")
    async def verify_interaction_callback(self, i: discord.Interaction):
        if i.data.get("custom_id") == "verify_type_1":
            data = verify_db_get(int(i.message.id))
            await i.guild.get_member(i.user.id).add_roles(
                i.guild.get_role(int(data["role_id"]))
            )
            await i.response.send_message("認証が完了しました。", ephemeral=True)
        else:
            return
    
    @app_commands.choices(
        option=[
            app_commands.Choice(name="ワンクリック", value="oneclick")
        ]
    )
    @app_commands.command(name="verify", description="認証をします。")
    async def verify(self, i: discord.Interaction, name: str, description: str, role: discord.Role, option: str):
        buttonView = discord.ui.View(timeout=None)
        buttonView.add_item(Button1())

        msg = await self.bot.get_channel(i.channel.id).send(
            embed=discord.Embed(title=name, description=description).add_field(name="付与するロール", value=f"{role.mention}"), view=buttonView
        )
        verify_db(int(msg.id), {"msg_id": int(msg.id), "role_id": role.id})
        await i.response.send_message("パネルの生成が完了しました。", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(verify(bot))
