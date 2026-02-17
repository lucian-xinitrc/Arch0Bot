import disnake, requests
from . import config
from . import ai
from . import moderation as md
from . import showingcommands as sc

class DiscordBot():
	c = config.Config()
	last_cache = None
	db = c.db_url
	token = c.discord_token

	def __init__(self):
		self.c.bot.run(self.token)
		sc.ShowingCommands()
		ai.ArtificialIntelligence()
		md.ServerInfo()
		
	def config_bot():
		return self.bot

	def get_last_message():
	    conn = psycopg2.connect(db)
	    cur = conn.cursor()

	    cur.execute("SELECT author, message FROM public.last_message WHERE id = 1")
	    row = cur.fetchone()

	    cur.close()
	    conn.close()

	    return row

	@tasks.loop(seconds=2)
	async def watcher():
	    global last_cache

	    row = get_last_message()
	    if not row:
	        return

	    if row != last_cache:
	        last_cache = row

	        author, msg = row
	        channel = bot.get_channel(1469673733580128431)

	        if channel:
	            await channel.send(f"**{author}**: {msg}")

	@sc.ShowingCommands().prompt.event
	async def on_ready():
		activity = disnake.Game(name="Arch BTW!")
		watcher.start()
		await sc.ShowingCommands().prompt.change_presence(status=disnake.Status.idle, activity=activity)
