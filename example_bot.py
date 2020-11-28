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
async def choice(ctx, *, information):
    i = information.split(' ')
    words = len(i)
    if words == 4:
        a = i[0] + " " + i[1]
        b = i[2] + " " + i[3]
        pair = gen.createGivenPair(gen.getAnimal(a), gen.getAnimal(b))
    elif words == 3:
        a = i[0] + " " + i[1]
        b = i[2]
        if (gen.getAnimal(a) == None):
            a = i[0]
            b = i[1] + " " + i[2]
        pair = gen.createGivenPair(gen.getAnimal(a), gen.getAnimal(b))
    elif words == 2:
        pair = gen.createGivenPair(gen.getAnimal(i[0]), gen.getAnimal(i[1]))
    else:
        return
    await sendMessage(ctx, 1, pair)

@client.command()
async def fixedNumber(ctx,number, *, animal):
    pair = gen.createPair(Generator.getAnimal(gen, animal))
    await sendMessage(ctx, number, pair)

async def sendMessage(ctx, number, pair):
    yName = pair.y.name if number == 1 else pair.y.plural
    number = "a" if number == 1 else number
    str = f'Would you rather fight a {pair.y.name} sized {pair.x.name} {pair.x.emoji} or {number} {pair.x.name} sized {yName} {pair.y.emoji}?'
    message = await ctx.send(str)
    await message.add_reaction(pair.x.emoji)
    await message.add_reaction(pair.y.emoji)

def getGenerator():
    return gen

client.run(config.bot_token)
