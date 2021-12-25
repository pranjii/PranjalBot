import os
import discord
import requests
from discord.ext import commands
from random import randint
import json
import asyncio

abuses = ['bc','fuck','fuck you', 'piss off', 'dick head', 'Asshole', 'son of a bitch', 'bastard', 'bitch','bimbo', 'jock', 'jerk', 'wimp', 'retard', 'shag	wanker', 'taking the piss', 'twat', 'bollocks']

intents = discord.Intents.default()
intents.messages = True

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

@bot.command(name='kick', pass_context=True)
@commands.has_permissions(kick_members=True)
async def on_kick(ctx, userName: discord.User):
  if userName == ctx.message.author.mention:
    ctx.send("You can't kick yourself")
    return
  
  if ctx.message.author.guild_permissions.administrator:
    await userName.kick()
    ctx.channel.send(f"{userName} has been kicked")
  else:
    await ctx.channel.send(f"Only admins can give this command")

@bot.command(name='ban')
async def on_ban(ctx, userName: discord.User):
  if userName == ctx.message.author.mention:
    ctx.send("You can't ban yourself")
    return
  
  if ctx.message.author.guild_permissions.administrator:
    await userName.ban()
    ctx.channel.send(f"{userName} has been banned")
  else:
    ctx.channel.send("Only admins can give this command")


@bot.command(name='amiadmin')
async def who_am_i(ctx):
  await ctx.send(ctx.message.author.guild_permissions.administrator)

@bot.command(name='unban')
async def on_unban(ctx, userName):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = userName.split('#')
  for ban_entry in banned_users:
    user = ban_entry.user
    if (user.name, user.discriminator) == (member_name, member_discriminator): 
      await  ctx.guild.unban(user)
      await ctx.channel.send(f"Unbanned {userName}")
      return

@bot.command(name='infoabout')
async def on_info_user(ctx, userName: discord.Member):
  await ctx.channel.send(f"Name:{userName.name}\nJoined at:{userName.joined_at}\nStatus:{userName.status}")

@bot.listen()
async def on_message(message):
  if message.author==client.user:
    return
  for abuse in abuses:
    if message.content.find(abuse)!=-1 and message.content.startswith('$add')==False:
      await message.channel.send("Please don't abuse")

@bot.command(name='add')
async def add_abuse(ctx, abuse):
  abuses.append(abuse)
  await ctx.channel.send("Abuse added")

@bot.command(name='quote')
async def get_quote(ctx):
  request = requests.get("https://zenquotes.io/api/quotes")
  json_data = json.loads(request.text)
  k = randint(0,50)
  await ctx.channel.send(str(json_data[k]['q'])+'-'+str(json_data[k]['a']))

my_secret = os.environ['TOKEN']
bot.run(my_secret)