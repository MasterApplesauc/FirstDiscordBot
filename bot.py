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
f = open('.\\.data') 
amongUsRoom = f.readline()
f.close()

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord')

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(os.getenv('DISCORD_CHANNEL'))
	await channel.send(f'Welcome, {member.name}! \nThe current Among Us room is #{amongUsRoom}')

@bot.command()
async def getRoom(ctx):
	await ctx.send(f'#{amongUsRoom}')

@bot.command()
async def setRoom(ctx, arg):
	global amongUsRoom
	amongUsRoom = arg[0:5]
	f = open('.\\.data', 'w')
	f.write(amongUsRoom)
	f.close()

	await ctx.send(f"Okay. I'll set the Among Us room to: #{amongUsRoom}")

bot.run(TOKEN)