import os, random
import discord

from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$')

#Vars
global amongUsRoom 
amongUsRoom = '00000'

@bot.command()
async def getRoom(ctx):
	await ctx.send(f'#{amongUsRoom}')

@bot.command()
async def setRoom(ctx, arg):
	global amongUsRoom
	amongUsRoom = arg[0:5]

	await ctx.send(f"Okay. I'll set the AmongUs room to: #{amongUsRoom}")

bot.run(TOKEN)