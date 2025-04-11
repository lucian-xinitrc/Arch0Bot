import disnake
import openai
import requests
from . import config
from openai import OpenAI
from disnake.ext import commands

messages = [{"role": "system", "content": "You are a helpful assistant"}]

class ArtificialIntelligence():
	prompt = config.Config().bot
	@prompt.event
	async def on_message(message):
		bot = config.Config().bot
		if message.author == bot.user:
			return
		if bot.user in message.mentions:
			async with message.channel.typing():
				messages.append({"role": "user", "content": f"Please write in that {config.Config().ai_mood} the following message and in the language that is in it, please adapt and keep conversation: {message.content}"})
				client = OpenAI(api_key=config.Config().api_key_ai)
				
				response = client.chat.completions.create(
			    	model="gpt-4o",
			    	messages=messages,
			    	stream=False
				)
				messages.append(response.choices[0].message)
				await message.reply(str(response.choices[0].message.content))
	
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
