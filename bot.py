from discord.ext import commands

from db import insert_search_query, get_search_history
from google_api import google_search
import settings

TOKEN = settings.DISCORD_TOKEN

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    # protect against a potentially recursive case where the bot sends a message that it might, itself, handle
    if message.author == bot.user:
        return

    if message.content.startswith('hi'):
        msg = 'hey'
        await message.channel.send(msg)
    await bot.process_commands(message)


@bot.command(name='google')
async def google(ctx):
    query = ctx.message.content.split(' ', 1)
    author_id = ctx.message.author.id
    response = ''
    if len(query) == 1:
        response = 'query required'
        pass
    elif len(query) == 2:
        query = query[1]
        insert_search_query(author_id, query)
        response = google_search(query)
        response = ' \n'.join(response)
    await ctx.send(response)


@bot.command(name='recent')
async def recent(ctx):
    query = ctx.message.content.split(' ', 1)
    author_id = ctx.message.author.id
    response = ''
    if len(query) == 1:
        response = 'query required'
        pass
    elif len(query) == 2:
        query = query[1]
        response = get_search_history(author_id, query)
        if response:
            response = ' \n'.join([x[0] for x in response])
        else:
            response = 'No history found'
    await ctx.send(response)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found')
        return
    raise error


bot.run(TOKEN)
