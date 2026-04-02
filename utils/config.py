import os, disnake, datetime, base64
from Crypto.Cipher import AES
from dotenv import load_dotenv
from disnake.ext import commands

load_dotenv()

class Config():
	bot = commands.Bot(
		intents=disnake.Intents.all(), 
		allowed_mentions=disnake.AllowedMentions(everyone=True)
	)
	discord_token = os.getenv('discord_token')
	api_ip = os.getenv('api_ip')
	proxy1_ip = os.getenv('proxy1')
	proxy2_ip = os.getenv('proxy2')
	proxy3_ip = os.getenv('proxy3')
	rules = os.getenv('rules')
	token = os.getenv('token')
	db_url = os.getenv('dburl')
	discord_bot_status_name = os.getenv('discord_bot_status_name')
	discord_bot_status_type	= os.getenv('discord_bot_status_type')
	api_key_ai = os.getenv('ai_api_key')
	ai_mood = "happy"
	old_message = ""
	id_part = os.getenv('id_part')
	jokes_api = os.getenv('jokes_api')


	def decrypt(self, ciphertext_b64):
	    cipher = AES.new(os.getenv('decrypt_key').encode(), AES.MODE_ECB)
	    decrypted = cipher.decrypt(base64.b64decode(ciphertext_b64))
	    pad = decrypted[-1]
	    return decrypted[:-pad].decode('utf-8')