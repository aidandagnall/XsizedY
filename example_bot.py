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
async def on_reaction_add(reaction, user):
    if (user.id == client.user.id):
        return
    for animal in gen.animals:
        if animal.emoji == reaction.emoji:
            animal.score += 1
            return

@client.event
async def on_raw_reaction_remove(payload):

    channel = client.get_channel(payload.channel_id)
    if (payload.user_id == client.user.id):
        return
    for animal in gen.animals:
        if animal.emoji == payload.emoji.name:
            animal.score -= 1
            return

@client.event
async def on_member_join(ctx,member):
    await ctx.send(f'(member) has joined the server')

@client.event
async def on_member_remove(ctx,member):
    await ctx.send(f'(member) has left the server')

@client.command()
async def random(ctx):
    pair = Generator.createPairRand(gen)
    n = 3 * (pair.y.size - pair.x.size)
    await sendMessage(ctx, n, pair)

@client.command()
async def choice(ctx):
    await ctx.send('Choice')

@client.command()
async def fixedNumber(ctx,number, *, animal):
    pair = Generator.createPair(gen, Generator.getAnimal(gen, animal))
    await sendMessage(ctx, number, pair)

async def sendMessage(ctx, number, pair):
    str = f'Would you rather fight 1 {pair.y.name} sized {pair.x.name} {pair.x.emoji} or {number} {pair.x.name} sized {pair.y.plural} {pair.y.emoji}?'
    message = await ctx.send(str)
    await message.add_reaction(pair.x.emoji)
    await message.add_reaction(pair.y.emoji)

client.run(config.bot_token)
