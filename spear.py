import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server at {member.joined_at.strftime("%A, %d %B %Y, Time- %I:%M:%S %p")}.')
    message.channel.send

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server at {member.joined_at.strftime("%A, %d %B %Y, Time- %I:%M:%S %p")}.')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency*1000)} ms")

@client.command(aliases=['8ball','test'])
async def _8ball(ctx,*,question):
    responses=['It certainly is.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes, definitely',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Dont count on it.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.'
                ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def calculator():
    pass



client.run('NjYxOTY5ODUwOTg1NDgwMjEz.Xj7Sng.cfDSUn3VUBQPI9uKwj-Ek9KMSU0')