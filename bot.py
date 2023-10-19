import discord
from discord.ext import commands

TOKEN = 'MTE2NDU2ODExNTEyMDcxMzc1OA.GaHaN7.-gq0vURwGIua8mSY5ee_PhBXOIAm2vXzrpoI48'  # Replace with your bot token

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

WOLVERINE_ID = 430159483881127948  # Replace with the actual ID of @Wolverine171

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Check if the bot is mentioned and the message is not from the bot itself
    mentioned_users = [user.id for user in message.mentions]
    if WOLVERINE_ID in mentioned_users and message.author != bot.user:
        await message.channel.send(f"Hello {message.author.mention}, Wolverine171 is currently away. He'll get back to you soon!")

    await bot.process_commands(message)

bot.run(TOKEN)

