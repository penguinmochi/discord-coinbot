import random
import discord
from discord.ext import commands
import os

# Botのトークンは環境変数DISCORD_TOKENに設定
TOKEN = os.getenv("DISCORD_TOKEN")

# プレフィックス（!coin のように呼び出す）
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Botが起動しました: {bot.user}")

@bot.command()
async def coin(ctx):
    """コイントスをして表/裏を返す"""
    result = random.choice(["表", "裏"])
    await ctx.send(f"🪙 コイントスの結果は… **{result}**！")

bot.run(TOKEN)
