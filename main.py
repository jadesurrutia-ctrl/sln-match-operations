
import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"⚽ SLN Match Operations conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == "!prueba":
        await message.channel.send(
            "⚽ ¡SLN Match Operations está funcionando correctamente!"
        )

if not TOKEN:
    raise RuntimeError("Falta DISCORD_TOKEN en Railway.")

bot.run(TOKEN)
