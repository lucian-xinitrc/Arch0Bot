import disnake
import asyncio
from . import config
from . import ai
from . import moderation as md
from . import showingcommands as sc
from disnake.ext import commands, tasks

class DiscordBot():
	c = config.Config()
	token = c.discord_token

	def __init__(self):
		self.c.bot.run(self.token)
		sc.ShowingCommands()
		ai.ArtificialIntelligence()
		md.ServerInfo()
		self.postListener.start()
		
	@tasks.loop(seconds=2)
	async def postListener(self):
		ai.listenerGeth()
    
	def config_bot():
		return self.bot

	@sc.ShowingCommands().prompt.event
	async def on_ready():
		activity = disnake.Game(name="Arch BTW!")
		asyncio.to_thread(ai.listenerGeth(), message)
		await sc.ShowingCommands().prompt.change_presence(status=disnake.Status.idle, activity=activity)
