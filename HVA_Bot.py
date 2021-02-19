import discord
from discord.ext import commands
from discord.ext.commands import Bot

from ics import Calendar as Calendar2
import random
import icalendar
from icalendar import Calendar 
import vobject
import json
import requests
from requests.models import get_auth_from_url

url = "https://rooster.hva.nl/ical?601e9fda&group=true&eu=ZGVra2VybTU1&h=7aYgYS8mHoRrKyYgM56-AnAXnnoVUL02WgXlPGGdQGw="
filename = "data"

data = requests.get(url).text

roasts = [
	", je moeder is een man.",
	", je moeder is zo lelijk dat One Direction de andere kant op liep.",
	", je moeder is zo dik, ik heb afgelopen kerst een foto van haar genomen en hij is nog steeds aan het printen.",
	", je moeder is zo dik dat ze op een iPod ging zitten en zo werd de iPad gemaakt.",
	", je moeder is zo dik, ze heeft cheat codes voor Wii Sport.",
	", sukkel.",
	", heeft seks met dode dieren."
]

BOT_TOKEN = 'ODA2MDY0NTEzNzM1ODUyMDQz.YBkAFA.1l8oJjbNS6Kd2qbgox8_kLwwDsM'

bot = commands.Bot(command_prefix='!', case_insensitive=True)
activity = discord.Game(name="with myself")
bot.remove_command('help')

@bot.event
async def on_ready():
	print("online")
	await bot.change_presence(status=discord.Status.online, activity=activity)


@bot.command()
async def new(ctx, arg2):
	if (ctx.author.id == 322473542182502412):		
		guild = ctx.message.guild
		category = await ctx.guild.create_category(arg2)
		channel = await guild.create_text_channel(f"{arg2}-text", category=category)
		channel = await guild.create_text_channel(f"{arg2}-text", category=category)
		await ctx.send(f"Category {arg2} with text channels {arg2} and {arg2} successfully created")
	else:
		await ctx.channel.send("You have no power here!")

@bot.command()
async def clear(ctx, amount: int):
	if (ctx.author.id == 322473542182502412):				
		await ctx.channel.purge(limit=amount)
		await ctx.channel.send('Messages cleared!') 
	else:
		await ctx.channel.send("You have no power here!")

@bot.command()
async def ping(ctx):
    await ctx.send(':ping_pong:  Pong! {0}ms'.format(round(bot.latency * 1000, 1)))

@bot.command() 
async def roast(ctx, user):
	if user != "<@!322473542182502412>":
		await ctx.send(f"{user} {random.choice(roasts)}")
	else:
		await ctx.send("Oppassen vriend.")


@bot.event
async def on_message(message):
	if "<@!806064513735852043>" in message.content.lower():
		await message.channel.send("Hou je bek, Fred's bitch.")
	if "vieze freddy" in message.content.lower():
      	await message.channel.send(random.choice(freddy))
    if "kanker" in message.content.lower() and message.author.id != 806064513735852043:
      	await message.channel.send("Kanker boef!")
	

	await bot.process_commands(message)


	



bot.run(BOT_TOKEN)
