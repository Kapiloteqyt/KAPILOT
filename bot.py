import contextlib
import inspect
import io
import sqlite3
import textwrap
from email import utils
from traceback import format_exception
import random
import asyncio

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from keep_alive import keep_alive


Intents = discord.Intents().all()





client = commands.Bot(command_prefix="k!", Intents=Intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot jest włączony!")
    await client.change_presence(activity=discord.Game(name="k!pomoc i baw sie moimi komendami!"))
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS info(guild_id, INT, tresc STR)")
    cursor.close()
    db.commit()



@client.command()
async def dev(ctx):
    embed = discord.Embed(title="Developerzy:", description=f"Owner: Kapiloteq#3355\nVOwner: AdamYT#6900\nHeadAdmin: 𝓟𝓲𝓚𝓻𝓸#5868", color=0x4d22ca)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Wywołano przez: {ctx.author.name} ({ctx.author.id})")
    await ctx.send(content=None, embed=embed)


class DiscordUtils:
    pass


@client.command(aliases = ["help"])
async def pomoc(ctx):
    embed = discord.Embed(title="Pomoc", description=":white_check_mark: **Informacyjne**\nPomoc, zapros, dev, serverinfo \n:exclamation: **Moderacyjne**\nkick, ban, unban, clear, ticket, usun, warn\n:globe_with_meridians: **Developerskie**\neval, restart\ndevclear", color=0x159540)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Wywołano przez: {ctx.author.name} ({ctx.author.id})")
    await ctx.send(content=None, embed=embed)





@client.command(aliases = ["b"])
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason="Brak Powodu!"):
    await member.ban(reason=reason)
    embed = discord.Embed(title="Ban!", description=f"Użytkownik: {member.mention}\nAdministrator: {ctx.author.mention}\nPowód: {reason}", color=0xd7342a)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Wywołano przez: {ctx.author.name} ({ctx.author.id})")
    await ctx.send(content=None, embed=embed)





@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, reason="Brak Powodu!"):
    await member.kick(reason=reason)
    embed = discord.Embed(title="Kick!", description=f"Użytkownik: {member.mention}\nAdministrator: {ctx.author.mention}\nPowód: {reason}", color=0xd7342a)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Wywołano przez: {ctx.author.name} ({ctx.author.id})")
    await ctx.send(content=None, embed=embed)
    await ctx.guild.kick



@client.command(aliases = ["ub"])
@has_permissions(ban_members=True)
async def unban(ctx, *, User : discord.User):
    embed = discord.Embed(title="Unban!",
                          description=f"Użytkownik: {User.id}\nAdministrator: {ctx.author.mention}",
                          color=0xd7342a)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Wywołano przez: {ctx.author.name} ({ctx.author.id})")
    await ctx.send(content=None, embed=embed)
    await ctx.guild.unban(User)



def clean_code(code):
    pass


class Pag:
    pass






@client.command()
async def zapros(ctx):
    embed = discord.Embed(title="Zapros Bota!", description="https://discord.com/api/oauth2/authorize?client_id=868223153854378056&permissions=8&scope=bot", color=0x159540)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Wywołano przez: {ctx.author.name} ({ctx.author.id})")
    await ctx.send(content=None, embed=embed)



@client.command()
@has_permissions(ban_members=True)
async def clear(ctx):
  await ctx.channel.purge()
  embed = discord.Embed(title="Czyszczenie Chatu!",
                        description=f"Administrator: {ctx.author.mention}",
                        color=0xd7342a)
  embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Wywołano przez: {ctx.author.name} ({ctx.author.id})")
  await ctx.send(content=None, embed=embed, delete_after=5)





@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title=":x: Error!",
                              description="Nie ma takiej komendy!",
                              color=0xd7342a)
        await ctx.send(content=None, embed=embed)






def _restart_bot():
    pass


@client.command(hidden=True, aliases = ["reset"])
@commands.is_owner()
async def restart(ctx):
        embed = discord.Embed(title="Restart!", description="Restartowanie bota!\nRestart....", color=0x159540)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Wywołano przez: {ctx.author.name} ({ctx.author.id})")
        await ctx.send(content=None, embed=embed)
        await _restart_bot()



@client.command()
@has_permissions(administrator=True)
async def usun(ctx):
        await ctx.channel.delete()


class MissingPermissions:
    pass





@client.command()
@commands.is_owner()
async def devclear(ctx):
    await ctx.channel.purge()
    embed = discord.Embed(title="DevClear!",
                          description=f"Developer bota wyczyscił Chat!",
                          color=0xd7342a)
    await ctx.send(content=None, embed=embed, delete_after=5)


@client.command(aliases = ["info"])
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=f"Informacje o serverze: **{name}**",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Właściciel", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Liczba członków", value=memberCount, inline=True)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Wywołano przez: {ctx.author.name} ({ctx.author.id})")

    await ctx.send(embed=embed)


@client.command(aliases = ["w"])
@commands.has_permissions(ban_members=True)
async def warn(ctx, member : discord.Member, *, reason="Brak!",):
    warns = +1
    warns=warns


    embed = discord.Embed(title="Ostrzeżenie!", url=" ", color=0x570fdb)
    embed.add_field(name="💠 Użytkownik:", value=member.mention, inline=False)
    embed.add_field(name="💠 Administrator:", value=ctx.author.mention, inline=False)
    embed.add_field(name="💠 Powód:", value=reason, inline=False)
    embed.add_field(name="💠 ilość warnów:", value=f'{warns}', inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Wywołano przez: {ctx.author.name} ({ctx.author.id})")
    await ctx.send(embed=embed)



keep_alive()
client.run("ODY4MjIzMTUzODU0Mzc4MDU2.YPsh0g.131MvjHiIPIdSPpN3mtkbuHsU6M")



