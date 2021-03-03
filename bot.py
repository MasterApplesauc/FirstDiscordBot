import os, random
import discord

from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = os.getenv('DISCORD_CHANNEL')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

#Vars
global amongUsRoom 
amongUsRoom = '00000'

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord')

@bot.event
async def on_member_join(member):
	print('a member has joined.')
	await member.send('yo!')

@bot.command()
async def getRoom(ctx):
	await ctx.send(f'#{amongUsRoom}')

@bot.command()
async def setRoom(ctx, arg):
	global amongUsRoom
	amongUsRoom = arg[0:5]

	await ctx.send(f"Okay. I'll set the AmongUs room to: #{amongUsRoom}")

bot.run(TOKEN)