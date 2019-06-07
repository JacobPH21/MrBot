import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time
import random
import datetime

bot = commands.Bot(command_prefix='b!')
start = time.time()
players = {}
dt = datetime.datetime.now()

bot.remove_command('help')

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game('b!help'))
  print('Bot is online')
	
@bot.command()
async def invite(ctx):
  embed = discord.Embed(title="Invite MrBot", value="Here", colour=discord.Color.blue(), url="https://discordapp.com/api/oauth2/authorize?client_id=582397024679362560&permissions=8&scope=bot")
  await ctx.send(embed=embed)
	
@bot.command()
async def uptime(ctx):
  now=time.time()
  sec=int(now-start)
  mins=int(sec//60)
  await ctx.send(f'Uptime is {sec} seconds')
	
@bot.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
	
@bot.command()
async def date(ctx):
  await ctx.send(f"Date today is {dt}")
	
@bot.command()
async def dice(ctx):
  await ctx.send(random.choice(['You rolled 1',
 'You rolled 2',
 'You rolled 3',
 'You rolled 4',
 'You rolled 5',
 'You rolled 6']))
	
@bot.command()
async def coin(ctx):
  await ctx.send(random.choice(['Coin flipped into Heads!',
 'Coin flipped into Tails!']))
	
@bot.command()
async def avatar(ctx, member: discord.Member):
  show_avatar = discord.Embed(
	
  color = discord.Color.blue()
 )
  show_avatar.set_image(url='{}'.format(member.avatar_url))
  await ctx.send(embed=show_avatar)
	
@avatar.error
async def avatar_error(ctx, error):
  if isinstance(error, commands.BadArgument):
  await ctx.send('Sorry, I cant find that user :worried:')
	
@bot.command()
async def dm(ctx):
  await ctx.author.send('Hello there im MrBot')
	
@bot.command()
async def help(ctx):
  embed = discord.Embed(title="List of Available Commands", description="**Prefix: b!**")
  embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
  embed.set_footer(text="This bot is created by JacobMC#1758")
	
  embed.add_field(name=":clipboard: **__Information__** :clipboard:", value="`help | userinfo | avatar`")
  embed.add_field(name=":hammer: **__Moderation__** :hammer:", value="`warn | kick | ban | clear`")
  embed.add_field(name=":game_die: **__Games__** :game_die:", value="`dice | coin`")
  embed.add_field(name=":grey_question: **__Others__** :grey_question:", value="`uptime | ping | dm | date`")
  embed.add_field(name=":envelope: **__Invite__** :envelope:", value="`invite`")
  embed.add_field(name="**Need Support?**", value="**Join our Support Server!** > http://bit.ly/MrBotSupport ")
	
  await ctx.send(embed=embed)
	
@bot.command()
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)
  amount = amount
  embed = discord.Embed(title="", description=f"**Cleared {amount} messages**")
  await ctx.send(embed=embed)
	
@bot.command()
async def warn(ctx, member : discord.Member,):
  await ctx.send(f'{member.mention} has been warned')
	
@warn.error
async def warn_error(ctx, error):
  if isinstance(error, commands.BadArgument):
  await ctx.send('Sorry, I cant find that user :worried:')
	
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  embed = discord.Embed(title="", description=f"Kicked {member.mention}")
  await ctx.send(embed=embed)
	
@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.BadArgument):
  await ctx.send('Sorry, I cant find that user :worried:')
	
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  embed = discord.Embed(title="", description=f"Banned {member.mention}")
	
@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    await ctx.send('Sorry, I cant find that user :worried:')
	
@bot.command()
async def userinfo(ctx, member: discord.Member):
	
  roles = (role for role in member.roles)
	
  embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
	
  embed.set_author(name=f"User Info - {member}")
  embed.set_thumbnail(url=member.avatar_url)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)	
  embed.add_field(name="ID:", value=member.id)
  embed.add_field(name="Guild Name:", value=member.display_name)
	
  embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %b %d %Y, %I %p"))
  embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %b %d %Y, %I %p"))
	
  embed.add_field(name=f"Roles", value=" ".join([role.mention for role in roles]))
  embed.add_field(name="Top Roles:", value=member.top_role.mention)
	
  embed.add_field(name="Bot", value=member.bot)
	
  await ctx.send(embed=embed)
	
@userinfo.error
async def userinfo_error(ctx, error):
  if isinstance(error, commands.BadArgument):
  await ctx.send('Sorry, I cant find that user :worried:')

bot.run(str{os.environ.get{BOT_TOKEN}})
