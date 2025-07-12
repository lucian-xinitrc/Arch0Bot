import disnake
import openai
import requests
import asyncio
import gethonis as geth
from . import config
from openai import OpenAI
from disnake.ext import commands

# The 
messages = [{"role": "system", "content": "You are a helpful assistant for an arch linux community named Arch0, your coder and creator is arch0tic, You say Hail Arch0tic when you are asked that."}]

class ArtificialIntelligence():
	prompt = config.Config().bot
	
	@prompt.event 	
	async def on_message(message):
		bot = config.Config().bot
		if message.author == bot.user:
			return
		if bot.user in message.mentions:  

			async with message.channel.typing():
				messages.append({"role": "user", "content": message.content})
				client = OpenAI(api_key=config.Config().api_key_ai)
				response = client.chat.completions.create(
			    	model="gpt-4o",
			    	messages=messages,
			    	stream=False
				)
				messages.append(response.choices[0].message)
				await message.reply(response.choices[0].message.content)

	@prompt.slash_command(description="Gethonis")
	async def geth(inter, ctx, message):
		try:
			await ctx.response.defer()
			msg = await ctx.followup.send("Please Wait a little...")
			bot = geth.Gethonis("geth-Ecuw2g7oy9FIlN3RZMAOxw", "https://api.gethonis.com/")
			bot.set_message("gethonis", False)
			async with ctx.channel.typing():
				response = await asyncio.to_thread(bot.get_message, message)
				await msg.edit(content=response)
		except:
			await msg.edit("Your token expired.")

	@prompt.slash_command(description="Image Generator")
	async def image(inter, ctx, arg):
		try:
			await ctx.send("Please wait...")
			client = OpenAI(api_key=config.Config().api_key_ai)
			response = client.images.generate(
			    model="dall-e-3",
			    prompt=arg,
			    size="1024x1024",
			    quality="standard",
			    n=1,
			)

			image_url = response.data[0].url

			embed=disnake.Embed(title="Prompt: `" + str(arg) + "`", color=disnake.Colour.from_rgb(23, 146, 208))

			embed.set_image(url=str(image_url))

			await ctx.send(embed= embed)
		except:
			await ctx.send(requests.get(config.Config().jokes_api).json()['value'])
