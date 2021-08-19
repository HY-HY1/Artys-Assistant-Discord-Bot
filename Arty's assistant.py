import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!a', intents=intents)

@client.event
async def on_ready() :
    await client.change_presence(status=discord.Status.online, activity=discord.Game('[!a]'))
    print('Bot Is Online')

@client.event
async def on_member_join(member):
    channel = client.get_channel(871888793991540738)
    await channel.send(f'Hi {member.mention} Welcome To {member.guild.name} Verify in <#871889321261670431> Read The Rules And Join The Conversation In <#871888350750076931>')


banned_words = ['']

@client.event
async def on_message(message):
    for i in banned_words:
        if message.content in i:
            await message.delete()
            await message.channel.send(f'{message.author.mention} Dont Say That')
            return
        await client.process_commands(message)
@client.command()
async def Hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}')

@client.command()
async def Hi(message) :
    options = ['Hi',
               'Hello',
               "G'day",
               "Bonjour"]
    await message.send(f'{random.choice(options)} {message.author.mention}')


@client.command()
@commands.has_permissions(kick_members=True)
async def Kick(ctx, member: discord.Member, *, Reason=None) :
    await member.kick(reason=Reason)
    await ctx.send(f'{member.mention} Has Been Kicked From {ctx.guild.name} Reason: {Reason}')
    print(f'{member} Has Been Kicked From {ctx.guild.name} Reason: {Reason}')


@client.command()
@commands.has_permissions(ban_members=True)
async def Ban(ctx, member: discord.Member, *, Reason=None) :
    await member.ban(reason=Reason)
    await ctx.delete.member_messages()
    await ctx.send(f'{member.mention} Has Been Banned From {ctx.guild.name} Reason: {Reason}')
    print(f'{member} Has Been Banned From {ctx.guild.name} Reason: {Reason}')


@client.command()  # clear
@commands.has_permissions(manage_messages=True)
async def Clear(ctx, amount: int) :
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Deleted {amount} messages {ctx.author.mention}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention} You Dont Have Permission To Use This Command')

client.run("ODc3MzEyMTA0MjI1NDY0MzQx.YRwykQ.5lWQ4R5A30VC3Eq6_YhGNxXKbAY")
