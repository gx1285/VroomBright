from discord.ext import commands
from discord import app_commands
import requests
from os import environ
import discord

api_key = environ['openweatherkey']

class weather(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="weather", description="天気を調べます。")
    @app_commands.describe(city="検索したい県を入力してください。（英語、一部日本語可）")
    async def weather(self, i: discord.Interaction, city: str):
        # 天気情報を取得します。
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
        weather_data = response.json()['weather'][0]
        temperature_data = response.json()['main']

        # 取得した天気情報を表示します。
        message = f"{city}の天気: {weather_data['description']}\n温度: {round(temperature_data['temp'] - 273.15, 2)}°C\n湿度: {temperature_data['humidity']}%\n風の速度: {response.json()['wind']['speed']}m/s"
        await i.response.send_message(message)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(weather(bot))
