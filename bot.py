import os, random
import discord

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome to my Discord server!'
	)

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content == '_randomNumber':
		response = random.randint(0, 1000000)
		await message.channel.send(response)

	if message.content == '!WhereAreWe':
		number = 'AX5BD'
		response = f'AmongUs Room: #{number}'
		await message.channel.send(response)


client.run(TOKEN)