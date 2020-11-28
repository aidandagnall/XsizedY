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
    pair = Generator.createPairRand(gen)
    message = await ctx.send(getOutputString(10, pair))
    await message.add_reaction(pair.x.emoji)

@client.command()
async def choice(ctx):
    await ctx.send('Choice')

@client.command()
async def fixedNumber(ctx,number,animal):
    pair = Generator.createPair(gen, Generator.getAnimal(gen, animal))
    message = await ctx.send(getOutputString(number, pair))
    await message.add_reaction(pair.x.emoji)

def getOutputString(number, pair):
    return f'Would you rather fight 1 {pair.y.name} sized {pair.x.name} or {number} {pair.x.name} sized {pair.y.plural}?'

client.run(config.bot_token)
