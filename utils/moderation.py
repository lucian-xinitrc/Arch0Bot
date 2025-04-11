import disnake
import requests
from . import config
from disnake.ext import commands


class ServerInfo():
	prompt = config.Config().bot

	@prompt.slash_command(description="Informations about a user")
	async def info(inter, ctx, user: disnake.Member = None):
		try:
 			avatarurl = user.avatar.url

 			embed=disnake.Embed(title="User's Details", color=disnake.Colour.red())
 			embed.set_image(url=str(user.avatar.url))
 			creationDate = user.created_at.strftime("%a %#d %B %Y, %I:%M %p")

 			embed.add_field(name="Account created:", value=creationDate)

 			joined_at = user.joined_at.strftime("%b %d, %Y, %T")
 			embed.add_field(name="Joined in server:", value=joined_at)
 			await ctx.response.send_message(embed= embed)
		
		except:
			await ctx.response.send_message(requests.get(config.Config().jokes_api).json()['value'])

	@prompt.slash_command(description="Informations about a user")
	async def membercount(inter: disnake.ApplicationCommandInteraction, ctx):
		try:
			count = ctx.guild.member_count
			embed=disnake.Embed(title="Member Count", color=disnake.Colour.red())
			embed.add_field(name="The total number of members is:", value=count)	
			await ctx.response.send_message(embed= embed)
		except: 
			await ctx.response.send_message(requests.get(config.Config().jokes_api).json()['value'])