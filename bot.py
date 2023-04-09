from discord.ext import commands, tasks
from discord import Intents, Status, Activity, ActivityType, Game, HTTPException
from itertools import cycle
from os import environ, listdir
from webserver import keep_alive

Token = environ['Token']

class VroomBright(commands.Bot):
  async def setup_hook(self):
    await keep_alive()
    for name in listdir("VroomBright/cogs"):
      if not name.startswith(("_", ".")):
        await bot.load_extension(
          f"cogs.{name[:-3] if name.endswith('.py') else name}"
        )
    await self.tree.sync()


bot = VroomBright(
  command_prefix="vb?",
  intents=Intents.all(),
  activity=Activity(
    type=ActivityType.watching,
    name="起動中...",
  ),
  status=Status.dnd,
  help_command=None,
)

@tasks.loop(seconds=5)
async def status_swap(cycle_d):
  activity = Game(next(cycle_d))
  await bot.change_presence(activity=activity, status=Status.online)

@bot.listen(name="on_ready")
async def bot_ready():
  print("起動完了")
  await status_swap.start(
    cycle(
      [
        f"/help | {len(bot.guilds)} サーバー",
        f"/help | {len(bot.users)} ユーザー数",
        f"/help | {round(bot.latency * 1000)}ms",
      ]
    )
  )

try:
  bot.run(Token)
except HTTPException:
  print("レートリミット制限です。")
