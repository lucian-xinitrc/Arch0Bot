import disnake, requests, psycopg2, base64
from . import config
from . import ai
from . import moderation as md
from . import showingcommands as sc
from disnake.ext import tasks
from Crypto.Cipher import AES

last_cache = None
class DiscordBot():
	c = config.Config()
	
	db = c.db_url
	token = c.discord_token

	def __init__(self):
		self.c.bot.run(self.token)
		sc.ShowingCommands()
		ai.ArtificialIntelligence()
		md.ServerInfo()
		
	def config_bot():
		return self.bot

	@tasks.loop(seconds=2)
	async def watcher():
	    global last_cache
	    bot = config.Config().bot
	    db = config.Config().db_url
	    print("Running here")
	    conn = psycopg2.connect(db)
	    cur = conn.cursor()

	    cur.execute("SELECT author, message FROM public.last_message WHERE id = 1")
	    row = cur.fetchone()

	    cur.close()
	    conn.close()
	    if not row:
	        return

	    if row != last_cache:
	        last_cache = row

	        author, msg = row
	        channel = bot.get_channel(1469673733580128431)

	        if channel:
	            await channel.send(f"**{config.Config().decrypt(author)}**: {config.Config().decrypt(msg)}")

	watcher.start()
	async def on_ready():
		activity = disnake.Game(name="Arch BTW!")
		
		await sc.ShowingCommands().prompt.change_presence(status=disnake.Status.idle, activity=activity)
