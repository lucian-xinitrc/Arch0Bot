import disnake, requests
from . import config
from . import ai
from . import moderation as md
from . import showingcommands as sc

class DiscordBot():
	c = config.Config()
	token = c.discord_token

	def __init__(self):
		self.c.bot.run(self.token)
		sc.ShowingCommands()
		ai.ArtificialIntelligence()
		md.ServerInfo()
		
	def config_bot():
		return self.bot

	@sc.ShowingCommands().prompt.event
	async def on_ready():
		activity = disnake.Game(name="Arch BTW!")
		sys_token = config.Config().token
		data = { "headers": sys_token, "command": "output" }
		response = requests.post('http://gethonis.com:8888/api/getOutput', json=data)
		result = response.json()
		if result['status'] == 'success':
			channel_id = 1440635903617011786
			channel = bot.get_channel(channel_id)
			if channel:
				await channel.send(result['output'])
		await sc.ShowingCommands().prompt.change_presence(status=disnake.Status.idle, activity=activity)
