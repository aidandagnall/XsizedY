from model.generator import Generator
import discord
from discord.ext import commands
import csv
import random
import config
import os
client = commands.Bot(command_prefix = '!')
gen = Generator()

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
    pair = Generator.createPair(gen)
    await ctx.send(f'{pair.x.name} {pair.y.name}')

@client.command()
async def choice(ctx):
    await ctx.send('Choice')

@client.command()
async def fixedNumber(ctx,number,animal):
    await ctx.send(f'{number} {animal}')
client.run(config.bot_token)
