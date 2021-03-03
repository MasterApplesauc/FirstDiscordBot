import os, random
import discord

from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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
async def on_message(message):
	channel = bot.get_channel(int(os.getenv('DISCORD_CHANNEL')))
	if message.author == bot.user:
		return

	happyBirthdayMessages = [
		'Happy Birthday!',
		'Happy Birthday to you!',
		'Happy Birthday, genius! Hope it\'s the best one yet.',
		'You rock. You are brilliant. I\'ve said enough. My warmest wishes!',
		'Dang you are OLD. Happy birthday anyway!',
		'Beep Boop. I\'m going to wish you a birthday. Happy Birthday!',
		'No matter how old you get, you will always be MY +1. Happy Birthday!',
		'Wow! You\'ve still got all your teeth! Happy Birthday!',
		'Let the party begin, Happy Birthday!'
		]

	if 'happy birthday' in message.content.lower():
		await channel.send(random.choice(happyBirthdayMessages))

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(int(os.getenv('DISCORD_CHANNEL')))
	await channel.send(f'Welcome, {member.name}! \nThe current Among Us room is #{amongUsRoom}')

@bot.command(name='getRoom', help='Displays what the current Among Us room access code is.')
async def getRoom(ctx):
	await ctx.send(f'#{amongUsRoom}')

@bot.command(name= 'setRoom', help='Allows you to change the current Among Us room access code.')
async def setRoom(ctx, arg):
	global amongUsRoom
	amongUsRoom = arg[0:5]
	f = open('.\\.data', 'w')
	f.write(amongUsRoom)
	f.close()

	await ctx.send(f"Okay. I'll set the Among Us room to: #{amongUsRoom}")

bot.run(TOKEN)