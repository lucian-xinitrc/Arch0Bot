import os, disnake, datetime
from dotenv import load_dotenv
from disnake.ext import commands
load_dotenv()

class Config():
	bot = commands.Bot(intents=disnake.Intents.all())

	discord_token = os.getenv('discord_token')
	token = os.getenv('token')
	discord_bot_status_name = os.getenv('discord_bot_status_name')
	discord_bot_status_type	= os.getenv('discord_bot_status_type')
	api_key_ai = os.getenv('ai_api_key')
	ai_mood = "happy"
	old_message = ""
	id_part = os.getenv('id_part')
	jokes_api = os.getenv('jokes_api')