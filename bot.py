import random
import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Botが起動しました: {bot.user}")

@bot.command()
async def coin(ctx):
    await ctx.send(f"🪙 コイントスの結果は… **{random.choice(['表', '裏'])}**！")

bot.run(TOKEN)