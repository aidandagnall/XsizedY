import discord
import config
from discord.ext import commands
import csv
import random
import config
import os
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(ctx,member):
    await ctx.send(f'(member) has joined the server')

@client.event
async def on_member_remove(ctx,member):
    await ctx.send(f'(member) has left the server')

@client.command()
async def random(ctx):
    break

@client.command()
async def choice(ctx):
    break

async def fixedNumber(ctx,number,animal):
    break
client.run(config.bot_token)
