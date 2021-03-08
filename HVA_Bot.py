import discord
from discord.ext import commands
from discord.ext.commands import Bot
import csv
import datetime as dt
from datetime import datetime
from datetime import time
from datetime import date
from ics import Calendar as Calendar2
import random
import icalendar
from icalendar import Calendar 
import vobject
import json
import requests
from requests.models import get_auth_from_url
import json
import albert
import platform
import os

roasts = [
	", je moeder is een man.",
	", je moeder is zo lelijk dat One Direction de andere kant op liep.",
	", je moeder is zo dik, ik heb afgelopen kerst een foto van haar genomen en hij is nog steeds aan het printen.",
	", je moeder is zo dik dat ze op een iPod ging zitten en zo werd de iPad gemaakt.",
	", je moeder is zo dik, ze heeft cheat codes voor Wii Sport.",
	", sukkel.",
	", heeft seks met dode dieren.",
	", je moeder is een plopkoek"
]

biertjes = [
  "wi56312/leffe-blond-abdijbier",
  "wi238769/texels-skuumkoppe",
  "wi140290/kasteelbier-bruin",
  "wi386832/brouwerij-t-ij-ijwit",
  "wi231220/heineken-premium-pilsener",
  "wi170811/corona-extra-pils",
  "wi388607/hertog-jan-tripel",
  "wi2708/hertog-jan-pilsener-natuurzuiver-bier",
  "wi210145/heineken-premium-pilsener-krat",
  "wi232949/grolsch-pilsener-krat",
  "wi227163/brand-pilsener-krat",
  "wi2722/amstel-pilsener-krat"
]

ids = {
	"Fred":806064513735852043, 
	"Joost":322473542182502412, 
	"Jip":748132840616493086, 
	"Stefan":393754612722565130
}
admins = [ids["Joost"],ids["Jip"],ids["Stefan"]]

with open("config.json", "r") as configjsonFile:
    configData = json.load(configjsonFile)
    BOT_TOKEN = configData["token"]

bot = commands.Bot(command_prefix='!', case_insensitive=True)
activity = discord.Game(name="!help")
bot.remove_command('help')

data = []
def calendarToJson():
	with open("Rooster/rooster_blok_3.csv") as csv_file:
		csvReader = csv.DictReader(csv_file)
		for rows in csvReader:
			vak = {}			
			vak['Description'] = rows['Description']
			vak['Start date'] = rows['Start date']
			vak['Start time'] = rows['Start time']
			vak['End time'] = rows['End time']
			vak['Docenten'] = rows['Staff member(s)']
			vak['Online'] = rows['Online activity']
			data.append(vak)	
	with open("Rooster/rooster.json", "w") as jsonFile:
		jsonFile.write(json.dumps(data, indent=4))

@bot.event
async def on_ready():
	calendarToJson()
	print("online")
	newList = []

	with open("Rooster/rooster.json", "r") as jsonFile:
		jsonYes = json.load(jsonFile)
		
		for x in jsonYes:			
			past = datetime.strptime(x['Start date'], "%Y-%m-%d")
			present = datetime.now()
			if not (past.date() < present.date()):
				newList.append(x)
	with open("Rooster/rooster.json", "w") as newJson:
		newJson.write(json.dumps(newList, indent=4))

	await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command(name="help", description="Returns all commands available")
async def help(ctx):
    helptext = "```\n"
    for command in bot.commands:
        helptext+=f"!{command}\n"
    helptext+="```"
    await ctx.channel.send(helptext)

@bot.command()
async def new(ctx, arg2):
	if (ctx.author.id == ids["Joost"]):		
		guild = ctx.message.guild
		category = await ctx.guild.create_category(arg2)
		channel = await guild.create_text_channel(f"{arg2}-text", category=category)
		channel = await guild.create_text_channel(f"{arg2}-text", category=category)
		await ctx.send(f"Category {arg2} with text channels {arg2} and {arg2} successfully created")
	else:
		await ctx.channel.send("You have no power here!")

@bot.command()
async def clear(ctx, amount: int):
	if (ctx.author.id in admins):	
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

@bot.command()
async def info(ctx):
	embed=discord.Embed(title=f"System information", description=None)
	embed.add_field(name="OS", value=f"{platform.platform()} ({platform.system()})", inline=False)
	embed.add_field(name="Processor", value=f"{platform.processor()}", inline=False)
	await ctx.send(embed=embed)

@bot.command()
async def biertje(ctx):
	await ctx.send(f"{ctx.message.author.mention}, Proost! 🍻")
	list = "Biertjes in de aanbieding:\n"
	for i in range(1, len(biertjes)):
		product = albert.Product(biertjes[i])
		if product.is_discounted:
			list += f"- {product.brand} (https://www.ah.nl/producten/product/{biertjes[i]})\n"
	if len(list) < 1:
		await ctx.send("Niets is in de aanbieding")  
	else:
		await ctx.send(list)

@bot.event
async def on_message(message):
	if "<@!806064513735852043>" in message.content.lower():
		await message.channel.send("Hou je bek, Fred's bitch.")
	if "vieze freddy" in message.content.lower():
		await message.channel.send(random.choice(freddy))
	if "kanker" in message.content.lower() and message.author.id != ids["Fred"]:
		await message.channel.send("Kanker boef!")
	if "joost" in message.content.lower():
		await message.channel.send("let op je woorden a mattie")
	await bot.process_commands(message)

@bot.command()
async def ah(ctx):
  listString = "Biertjes in de aanbieding:\n"
  for i in range(1, len(biertjes)):
    	product = albert.Product(biertjes[i])
    	if product.is_discounted:
      		listString += f"- {product.brand} (https://www.ah.nl/producten/product/{biertjes[i]})\n"
  if len(listString) < 1:
    await ctx.send("Niets is in de aanbieding")  
  else:
    await ctx.send(listString)

@bot.command()
async def les(ctx, dag):
	if dag == "vandaag":	
		with open("Rooster/rooster.json", "r") as jsonFile:
			roosterJson = json.load(jsonFile)
		for x in roosterJson:
			past = datetime.strptime(x['Start date'], "%Y-%m-%d")
			present = datetime.now()
			if (past.date() == present.date()):
				description = x['Description']
				datum = x['Start date']
				tijdStart = x['Start time']
				tijdEinde = x['End time']
				docenten = x['Docenten']
				embedToSend = create_embed(description, datum, tijdStart, tijdEinde, docenten)
				await ctx.send(embed=embedToSend)
	
@bot.command()
async def meme(ctx):
	random_filename = "memes/" + random.choice(os.listdir(path))
	await ctx.send(file=discord.File(random_filename))


def create_embed(description, datum, tijdStart, tijdEinde, docenten):
	if description == 'Research Skills':
		linkNaam = "Teams link"
		link = "https://teams.microsoft.com/l/meetup-join/19%3ameeting_MWNlMDgyNjUtYzY4YS00NzA1LWFmMTQtNWJmNzFkY2JiOWU5%40thread.v2/0?context=%7b%22Tid%22%3a%220907bb1e-21fc-476f-8843-02d09ceb59a7%22%2c%22Oid%22%3a%22565b138c-8d90-4004-8386-ca03ea1be4cb%22%7d"
	elif description == 'Project Agile Developement':
		linkNaam = "Teams link"
		link = "https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZTkyNzI1YWYtODQ2ZS00MmFjLTllNmMtN2M3NDAyYjM3Njlj%40thread.v2/0?context=%7b%22Tid%22%3a%220907bb1e-21fc-476f-8843-02d09ceb59a7%22%2c%22Oid%22%3a%22565b138c-8d90-4004-8386-ca03ea1be4cb%22%7d"
	else:
		linkNaam = "Link staat op DLO"
		link = "https://dlo.mijnhva.nl/d2l/home"

	embed=discord.Embed(title=f"{description}", description=None)
	embed.add_field(name="Datum", value=f"{datum}", inline=False)
	embed.add_field(name="Tijd", value=f"{tijdStart} - {tijdEinde}", inline=False)
	embed.add_field(name="Docenten", value=f"{docenten}", inline=False)
	embed.add_field(name="Locatie", value=f"[{linkNaam}]({link})", inline=False)

	return embed



bot.run(BOT_TOKEN)


"""
if dag == "morgen":
		with open("Rooster/rooster.json", "r") as jsonFile:
			roosterJson = json.load(jsonFile)
		for x in roosterJson:
			past = datetime.strptime(x['Start date'], "%Y-%m-%d")

						
			present = datetime.now()
			tomorrow = present.date() + dt.timedelta(days=19)
			
			if (past.date() == tomorrow):
				print("yes")
				description = x['Description']
				datum = x['Start date']
				tijdStart = x['Start time']
				tijdEinde = x['End time']
				docenten = x['Docenten']
				embedToSend = create_embed(description, datum, tijdStart, tijdEinde, docenten)
				await ctx.send(embed=embedToSend)
"""



	


	



