import os, json, disnake, openai, requests, asyncio, textwrap
import gethonis as geth
from . import config
from openai import OpenAI
from dotenv import load_dotenv, dotenv_values
from disnake.ext import commands, tasks
load_dotenv()
messages = [{"role": "system", "content": os.getenv('arch0_training') }]

def reload_env(path='.env'):
    env_dict = dotenv_values(path)
    for k, v in env_dict.items():
        os.environ[k] = v

class ArtificialIntelligence():
	load_dotenv()
	prompt = config.Config().bot

	async def listenerGeth():
		bot = config.Config().bot
		print("Arch0 is running.")
		
	@prompt.event 	
	async def on_message(message):
		bot = config.Config().bot
		if message.author == bot.user:
			return
		if True:
			load_dotenv('.env')
			reload_env('.env')
			channel_id = int(os.getenv('channel_posts'))
			channel = bot.get_channel(channel_id)
			if channel:
				getho = geth.Gethonis(os.getenv('token_gethonis'), os.getenv('baseurl_gethonis'))
				getho.set_listener(str(bot.user.id))
				result = getho.get_postaslistener()
				try:
					raw_result = result[0]
					parsed_data = json.loads(raw_result)
					if parsed_data['Post']:
						post = parsed_data['Post']
						title = post.get("Title", "Untitled Post")
						paragraphs = post.get("paragraphs", [])
						footer_text = post.get("Footer", "")
						joined_paragraphs = "\n\n".join(paragraphs)

						embed = disnake.Embed(
						    title=title,
						    description="\n\n".join(paragraphs),
						    color=disnake.Color.gold()
						)
						embed.set_footer(text=footer_text)
						output = textwrap.dedent(f"""
						# {title}
						{joined_paragraphs}
						{footer_text}
						""")
						await channel.send(embed=embed)
					else:
						await channel.send("Looking for post")
				except:
					print("Looking for post")
		if bot.user in message.mentions:  
			async with message.channel.typing():
				load_dotenv()
				messages[0]["content"] = os.getenv('arch0_training')
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
