import discord
from discord.ext import commands
import json
import asyncio

intents = discord.Intents.default()
intents.messages = True
# intents.ban = True
# intents.invite = True

bot = commands.Bot(command_prefix='$', case_insensitive=True, intents=intents)

client = discord.Client()

@bot.event
async def on_ready():
  print('The bot is ready')

@bot.command(name='intro')
async def on_intro(ctx):
  await ctx.send(f"Hi I am PranjalBot.U can find me on https://github.com/pranjii/PranjalBot ")

@bot.event
async def on_member_join(member):
  channel = bot.get_channel(916677924684451874)
  await channel.send(f"Welcome {member.name}")

# @bot

# bot.add_command(on_intro())

bot.run('OTE2NjUxNTcxMTg4NzQ0MjEy.YatQTQ.8ZwqKp1Sat2vQQS6-691k8O8BSY')
