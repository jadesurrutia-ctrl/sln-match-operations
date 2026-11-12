
import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"SLN Match Operations está en línea: {bot.user}")

if not TOKEN:
    raise RuntimeError("Falta configurar DISCORD_TOKEN en Railway.")

bot.run(TOKEN)
