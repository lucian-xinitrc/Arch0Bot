import disnake
import requests
from enum import Enum
from disnake.ext import commands
from . import config

class types(str, Enum):
	say = "say"
	op = "op"
	custom = "custom"

class ShowingCommands():
	prompt = config.Config().bot
	sys_token = config.Config().token

	@prompt.slash_command(description="Sends the bot's latency.")
	async def arch(inter, ctx):
		await ctx.response.send_message(f"# Windows isn't a virus, viruses do something.")

	@prompt.slash_command(description="Opens the minecraft server")
	async def start_mc_server(inter, ctx):
		try:
			if ctx.author.id == 1135659932000202942 or ctx.author.id == 1027255470429319228:
				data = { "headers": "string", "command": "start" }
				response = requests.post('http://gethonis.com:8888/api/insertCommand', json=data)
				result = response.json()
				if result['status'] == "started":
					await ctx.response.send_message("Server Started")
			else:
				await ctx.response.send_message("You have no permission!")
		except:
			await ctx.response.send_message("There was an error!")

	@prompt.slash_command(description="Inserts a command")
	async def command_mc_server(inter, ctx, type: types, command):
		try:
			if ctx.author.id == 1135659932000202942 or ctx.author.id == 1027255470429319228:
				data = { "headers": sys_token, "command": command, "type": type }
				response = requests.post('http://gethonis.com:8888/api/insertCustomCommand', json=data)
				result = response.json()
				if result['status'] == "started":
					await ctx.response.send_message("Server Started")
			else:
				await ctx.response.send_message("You have no permission!")
		except:
			await ctx.response.send_message("There was an error")

	@prompt.slash_command(description="Closes the Minecraft Server")
	async def stop_mc_server(inter, ctx):
		try:
			if ctx.author.id == 1135659932000202942 or ctx.author.id == 1027255470429319228:
				data = { "headers": "string", "command": "close" }
				response = requests.post('http://gethonis.com:8888/api/insertCommand', json=data)
				result = response.json()
				if result['status'] == "closed":
					await ctx.response.send_message("Server closed")
			else:
				await ctx.response.send_message("You have no permission!")
		except:
			await ctx.response.send_message("There was an error!")
	@prompt.slash_command(description="First Prompt")
	async def help(inter, ctx):
		await ctx.response.send_message("Hi")

	@prompt.slash_command(description="Deploy Test")
	async def deploytest(inter, ctx):
		await ctx.response.send_message("The deployment was done!")

	@prompt.slash_command(description="A random Joke")
	async def joke(inter, ctx):
		await ctx.response.send_message(requests.get(config.Config().jokes_api).json()['value'])
	
	@prompt.slash_command(description="Inspiring quote")
	async def inspire(inter, ctx):
		try:
			quote = requests.get("https://zenquotes.io/api/random").json()[0]["q"]	
			await ctx.response.send_message(quote)
		except:
			await ctx.response.send_message(requests.get(config.Config().jokes_api).json()['value'])

	@prompt.slash_command(description=":3")
	async def lovespam(inter: disnake.ApplicationCommandInteraction, ctx):
		try:
			i = 0
			channel_id = 1220501381706944552
			id_darling = ""
			channel = inter.guild.get_channel(channel_id)
			if channel:
				while i < 1:
					await channel.send(f"TE IUBESCCCCCC babe :3 mult de toooot")
		except:
			await ctx.response.send_message("TE IUBESCCCCC")

	@prompt.slash_command(description="Daily Verse")
	async def verse(inter, ctx):
		try:
			data = requests.get("https://beta.ourmanna.com/api/v1/get?format=json&order=daily").json()
			verse_text = data["verse"]["details"]["text"]
			verse_reference = data["verse"]["details"]["reference"]
			embed = disnake.Embed(title="Daily verse", description=verse_text, color=disnake.Colour.red())

			embed.add_field(name="Reference", value=verse_reference)
			embed.add_field(name="Version", value=data["verse"]["details"]["version"])
			await ctx.response.send_message(embed = embed)
		except:
			await ctx.response.send_message(requests.get(config.Config().jokes_api).json()['value'])

	# Daily Orthodox Calendar
	@prompt.slash_command(description="Orthodox Calendar")
	async def orth(inter, ctx):
		try:
			data = requests.get("https://orthocal.info/api/gregorian/").json()
			date = str(str(data["day"]) + ' ' + str(data["month"]) + ' ' + str(data["year"]))
			await ctx.response.send_message("# Orthodox Calendar" + '\n' + "`Date:` " + date + '\n' + "`Title:` " + data["titles"][0] )
		except:
			await ctx.response.send_message(requests.get(config.Config().jokes_api).json()['value'])

	@prompt.slash_command(description="Welcome message")
	async def welcome(inter, ctx):
		await ctx.response.send_message(f"### Bine ai venit, rau ai nimerit!!!")

	@prompt.slash_command(description="How the bot will greet u")
	async def sal(inter, ctx):
		await ctx.response.send_message(f"## Buna, ca salut esti deja!")

	@prompt.slash_command(description="Does spam")
	async def spam(inter, ctx, arg, number: int):
		await ctx.response.send_message("Spam incoming")
		while number:
			await ctx.send(arg)

	@prompt.command(description="You know what the command does")
	async def loveyou(inter, ctx):
		try:
			if inter.author.id == "":
				await inter.ctx.response.send_message("Babe, dacă citești asta, înseamnă că nu sunt aici, sunt ocupat sau dorm, sau nu ți-am răspuns încă. Îți reamintesc eu aici că te iubesc mult de tot, ești tot ce mi-am dorit vreodată. Te iubesc și te voi iubi mereu. Dacă te-a supărat cineva, nu-ți face griji, eu tot te iubesc și sunt pentru tine tot timpul, mă întorc cât pot de repede. Tot timpul caut să te înțeleg prin ce treci, nu ești singură, babe, sunt cu tine mereu. Un reminder aici cât de frumoasă ești și cât de mult însemni pentru mine. Sper să revin cât mai repede, dar până atunci ai mesajul ăsta să-l citești. Nu te evit, babe, de aia las mesajul acesta. Muahhh! Te iubesc!!! Încearcă să te gândești cât de fericiți vom fi în viitor și câte vom face. Ce locuri vom vizita, cât de mult ne vom distra. Chiar dacă te-a supărat mama ta sau oricine altcineva, lasă, tot eu cu tine rămân la final. Ne ținem în brațe și ne gândim prin câte am trecut și vom trece împreună.")
		except:
			await ctx.response.send_message(requests.get(config.Config().jokes_api).json()['value'])