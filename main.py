import discord
from discord.ext import commands
import os
import asyncio
import urllib
import requests
import time
import random
from discord import Intents
from lists import *
from PIL import Image, ImageDraw, ImageFont

client = commands.Bot(command_prefix='-', intents=Intents.all())
client.remove_command('help')

vers = str("v1.4")


@client.event
async def on_ready():
    channel = client.get_channel(719250219803476018)
    print('Bot is ready')
    await client.change_presence(activity=discord.Game(f'Pineappleserver.ga | {vers}'))
    embed = discord.Embed(title="Bot is back online", color=0x37ff00)
    embed.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    embed.set_thumbnail(
        url="https://assets.stickpng.com/images/5aa78e207603fc558cffbf19.png")
    try:
        await channel.send(embed=embed)
    except:
        print("Channel couldn't be reached")


@client.event
async def on_member_join(member):
    guild = member.guild
    channel = discord.utils.get(member.guild.channels, name='member-log')

    base = Image.open("welcome.png").convert("RGBA")
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    # get a font
    fnt = ImageFont.truetype(
        "/usr/share/fonts/googlefonts/JetBrainsMono-VariableFont_wght.ttf", 40)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    d.text((260, 70), "Welcome", font=fnt, fill=(255, 255, 255, 128))
    d.text((260, 120), f"{member.display_name}!",
           font=fnt, fill=(255, 255, 255, 255))

    out = Image.alpha_composite(base, txt)
    out.save('nice.png')
    await member.send(f'Welcom to **{member.guild.name}**!\nYou are the **{guild.member_count}th** member :tada: !')
    await channel.send(content=f'{member.mention} just joined **{member.guild.name}** !', file=discord.File('nice.png'))

    channell = guild.get_channel(814909385457401917)
    await channell.edit(name=f'Members: {guild.member_count}')
    print(f'{member} Joined')


@client.event
async def on_member_remove(member):
    guild = member.guild
    channell = guild.get_channel(814909385457401917)
    await channell.edit(name=f'Members: {guild.member_count}')


@client.event
async def on_member_update(before, after):
    member = before
    guild = member.guild
    channell = guild.get_channel(814909385457401917)
    if before.status != after.status:
        await channell.edit(name=f'Members: {guild.member_count}')


# HELP COMMAND


@client.command(name='help')
async def help(ctx):
    sender = ctx.author

    first = discord.Embed(
        title="Help", description="All bot commands in a single list", color=0x0a4d8b)
    first.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    first.set_thumbnail(url="https://i.imgur.com/uwUVECT.png")
    first.add_field(name="-ping", value="Ping the bot", inline=True)
    first.add_field(name="-version",
                    value="Get the current version of the bot", inline=True)
    first.add_field(name="-say [expression]",
                    value="Let the bot say something", inline=True)
    first.add_field(name="-big", value="Try it out", inline=True)
    first.add_field(name="-hanz", value="Trigger hanz", inline=True)
    first.add_field(name="-pesten [@member]",
                    value="Safe someony from a bully", inline=True)
    first.add_field(name="-hit", value="Hit someone", inline=True)
    first.add_field(name="-shovel", value="Shovel someone", inline=True)
    first.add_field(
        name="-8ball [question]", value="Get an answer to any closed question", inline=True)
    first.add_field(name="-rus", value="Play Russian roulette", inline=True)
    first.add_field(name="-burn [@member]", value="Burn someone", inline=True)
    first.add_field(name="-circle", value="Play circle of death", inline=True)
    first.add_field(name="-poll [expression]",
                    value="Let people vote for something", inline=True)
    first.add_field(name="-choose [option1] [option2]",
                    value="Let people choose between two options", inline=True)
    first.add_field(name="-website",
                    value="Get the link to the pineaple website", inline=True)
    first.add_field(
        name="-invite", value="Get the invite link to the server", inline=True)
    first.add_field(
        name="-levels", value="Get the link to the levels overview page", inline=True)
    first.add_field(name="-chamilo",
                    value="The HoGent learing platform", inline=True)
    first.add_field(
        name="-Ufora", value="The UGent learning platform", inline=True)
    first.add_field(name="-shorturl [link] [custom title]",
                    value="Make a link shorter with a custom name", inline=True)
    first.add_field(
        name="-iplookup [IP]", value="Get geolocation of an ip adress", inline=True)
    first.add_field(name="-qr [link]",
                    value="Create a QR code for a url", inline=True)
    first.add_field(
        name="-screenshot [link]", value="Create a screenshot form a website without having to visit it", inline=True)
    first.add_field(name="-doggo", value="Get a random dog image", inline=True)
    first.add_field(name="-seal [top text] [bottom text]",
                    value="Create a seal meme", inline=True)

    second = discord.Embed(color=0x0a4d8b)
    second.add_field(name="-sanders [top text] [bottom text]",
                     value="Create a Berny Sanders meme", inline=True)
    second.add_field(name="-sponge [top text] [bottom text]",
                     value="Create a SpongeBob meme", inline=True)
    second.add_field(name="-disaster [top text] [bottom text]",
                     value="Create a disastrous meme", inline=True)
    second.add_field(name="-drunkbaby [top text] [bottom text]",
                     value="Create a drunk baby meme", inline=True)
    second.add_field(name="-sponge [top text] [bottom text]",
                     value="Create a SpongeBob meme", inline=True)
    second.add_field(name="-randomfact",
                     value="Get a random fact (sometimes in german whoops)", inline=True)
    second.add_field(
        name="-lovecalc", value="Calculate the compatibility between people", inline=True)
    second.add_field(name="-report [@member] [reason]",
                     value="Report a member to the mods", inline=True)
    second.add_field(name="-modmail [message]",
                     value="Send a modmail", inline=True)
    second.set_footer(text=f"Pineappleserver.ga | {sender}")
    await ctx.send(embed=first)
    await ctx.send(embed=second)
    print(f'{ctx.author} used help')


# ESSENTIALS


@client.command(name='ping')
async def ping(ctx):
    await ctx.send(f"**Pong:** {round(client.latency * 1000)}ms")
    print(f"Ping: {round(client.latency * 1000)}ms")


@client.command(name='version')
async def version(ctx):
    embed = discord.Embed(title="Version", description=vers, color=0x0a4d8b)
    embed.set_thumbnail(
        url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    embed.set_footer(text="Pineappleserver.ga")
    await ctx.send(embed=embed)
    print(f'{ctx.author} Version cmd')


@client.command(name='say')
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()
    try:
        await ctx.send(f"{text}")
    except:
        await ctx.send("Say command usage: `-say [message]`")
    print(f"{ctx.author} used say cmd to say: {text}")


@client.command(name='members')
async def members(ctx):
    member = ctx.author
    guild = member.guild
    await ctx.send(f"We currently have **{guild.member_count}** members! 😀")
    print(f'{ctx.author} used membercount')


# MODDERATION


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    channel = discord.utils.get(member.guild.channels, name='moderation-log')
    message = ctx.message
    await message.delete()
    embed = discord.Embed(title=f"{member} got banned from the server",
                          description=f"Reason: {reason}", color=0xff0000)
    embed.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    embed.set_thumbnail(url="https://i.imgur.com/WPPqs5S.png")
    embed.set_footer(text=f"Pineappleserver.ga | Moderator: {ctx.author}")
    await ctx.send(embed=embed)
    await channel.send(embed=embed)
    print(f'{member} got banned for {reason}')
    await member.ban(reason=reason)
    directmsg = discord.Embed(
        title=f"You got banned from {member.guild.name}", description=f"Reason: {reason}", color=0xff0000)
    directmsg.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    directmsg.set_footer(text=f"Pineappleserver.ga | Moderator: {ctx.author}")
    await member.send(embed=directmsg)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    channel = discord.utils.get(member.guild.channels, name='moderation-log')
    message = ctx.message
    await message.delete()
    embed = discord.Embed(title=f"{member} got kicked from the server",
                          description=f"Reason: {reason}", color=0xff0000)
    embed.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    embed.set_thumbnail(url="https://i.imgur.com/Xxr6OqW.png")
    embed.set_footer(text=f"Pineappleserver.ga | Moderator: {ctx.author}")
    await ctx.send(embed=embed)
    await channel.send(embed=embed)
    directmsg = discord.Embed(
        title=f"You got kicked from {member.guild.name}", description=f"Reason: {reason}", color=0xff0000)
    directmsg.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    directmsg.set_footer(text=f"Pineappleserver.ga | Moderator: {ctx.author}")
    await member.send(embed=directmsg)
    print(f'{member} got kicked for {reason}')
    await member.kick(reason=reason)


@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, reason=None):
    message = ctx.message
    await message.delete()
    channel = discord.utils.get(member.guild.channels, name='moderation-log')
    embed = discord.Embed(
        title=f"You got a warning in {member.guild.name}", description=f"Warning: {reason}", color=0xff0000)
    embed.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    embed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Warning.svg/832px-Warning.svg.png")
    embed.set_footer(text=f"Pineappleserver.ga | Moderator: {ctx.author}")
    await member.send(embed=embed)

    moderation = discord.Embed(
        title=f"{member} got warned", description=f"Warning: {reason}", color=0xff0000)
    moderation.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    moderation.set_footer(text=f"Pineappleserver.ga | Moderator: {ctx.author}")
    await channel.send(embed=moderation)
    print(f'{member} got kicked for {reason}')


@client.command()
async def report(ctx, member: discord.Member, *, reason=None):
    try:
        message = ctx.message
        mod = discord.utils.get(member.guild.channels, name='moderation')
        log = discord.utils.get(member.guild.channels, name='moderation-log')

        embed = discord.Embed(title="Report", color=0xff0000)
        embed.set_author(
            name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
        embed.add_field(name=f"{ctx.author} has reported {member}",
                        value=f"Reason: {reason}", inline=True)
        embed.set_footer(text="Pineappleserver.ga")
        await mod.send(embed=embed)
        await message.delete()

        lg = discord.Embed(
            title="Report", description=f"{ctx.author.mention} has reported {member.mention}", color=0xff0000)
        lg.set_author(name="Pineapple",
                      icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
        lg.set_footer(text="Pineappleserver.ga")
        await log.send(embed=lg)
        print(f'{member} got reported by {ctx.author} for {reason}')
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(
            name="Usage:", value="`-report [member] [reason]`", inline=False)
        embed.set_footer(text="Pineappleserver.ga")
        await ctx.send(embed=embed)


@client.command()
async def modmail(ctx, *, msg):
    try:
        message = ctx.message
        mod = discord.utils.get(ctx.author.guild.channels, name='moderation')
        log = discord.utils.get(
            ctx.author.guild.channels, name='moderation-log')

        embed = discord.Embed(title="Modmail", color=0xFF5A00)
        embed.set_author(
            name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
        embed.add_field(name=f"{ctx.author} used modmail!",
                        value=f"Message: {msg}", inline=True)
        embed.set_footer(text="Pineappleserver.ga")
        await mod.send(embed=embed)
        await message.delete()

        lg = discord.Embed(
            title="Modmail", description=f"{ctx.author.mention} used modmail!", color=0xFF5A00)
        lg.set_author(name="Pineapple",
                      icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
        lg.set_footer(text="Pineappleserver.ga")
        await log.send(embed=lg)
        print(f'{ctx.author} used modmail: {msg}')
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(
            name="Usage:", value="`-modmail [message]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def dm(ctx, member: discord.Member, *, msg):
    try:
        log = discord.utils.get(
            ctx.author.guild.channels, name='moderation-log')
        message = ctx.message
        await member.send(f"{msg}")
        await message.delete()

        embed = discord.Embed(
            title="DM", description=f"{ctx.author.mention} used DM to message {member.mention}!\n\n **Message:** {msg}",
            color=0xFF5A00)
        embed.set_author(
            name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await log.send(embed=embed)
        print(f"{ctx.author} has sent a dm to {member}: {msg}")
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(
            name="Usage:", value="`-dm [person] [message]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    try:
        log = discord.utils.get(
            ctx.author.guild.channels, name='moderation-log')
        ch = ctx.channel.mention
        await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(f'**{amount}** messages were deleted!')
        embed = discord.Embed(
            title="Clear", description=f"{ctx.author.mention} removed **{amount}** messages in {ch}", color=0xFF5A00)
        embed.set_author(
            name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
        embed.set_footer(text="Pineapple.ga")
        await log.send(embed=embed)
        time.sleep(2)
        await msg.delete()
        print(f"{ctx.author} removed {amount} messages in {ch}")
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(name="Usage:", value="`-clear [number]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def massmention(ctx, person):
    message = ctx.message
    await message.delete()
    print(f"{ctx.author} used massmention on {person}")
    m1 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m2 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m3 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m4 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m5 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m6 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m7 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m8 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m9 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m10 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m11 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m12 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m13 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m14 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m15 = await ctx.send(f"{person}")
    await asyncio.sleep(0.4)
    m16 = await ctx.send(f"{person}")
    time.sleep(2)

    def check(m):
        return m.author == client.user

    await ctx.channel.purge(limit=16, check=check)


@client.command(name='refresh')
async def refresh(ctx):
    while True:
        message = ctx.message
        await message.delete()
        member = ctx.author
        guild = member.guild
        channel = discord.utils.get(
            member.guild.channels, id=814901609573777428)
        await channel.edit(name=f'Member Count: {guild.member_count}')


# FUN COMMANDS


@client.command(name='big')
async def big(ctx):
    await ctx.send("https://tenor.com/view/dick-penis-dildo-forest-running-gif-16272085")
    message = await ctx.send('SLONG!')
    await message.add_reaction("🍆")
    print(f'{ctx.author} used Big cmd')


@client.command(name='hanz')
async def hanz(ctx):
    await ctx.send(
        'https://tenor.com/view/hanz-get-ze-flammenwerfer-flammenwerfer-excited-hans-flamethrower-gif-18658452')
    message = ctx.message
    await message.add_reaction("🔥")
    await message.add_reaction("💥")
    await message.add_reaction("✨")
    print(f'{ctx.author} used Hanz cmd')


@client.command(name='pesten')
async def pesten(ctx, arg1):
    try:
        message = ctx.message
        await message.delete()
        await ctx.send('This might help you {} <:FeelsBadMan:785490392375754842>'.format(arg1))
        embed = discord.Embed(title="Move tegen pesten", url="https://www.youtube.com/watch?v=phO3GxlcmEk",
                              description="Brahim en Charlotte Leysen", color=0xc73333)
        embed.set_author(
            name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
        embed.set_thumbnail(
            url="https://i.ytimg.com/vi/phO3GxlcmEk/maxresdefault.jpg")
        embed.set_footer(text="Pineappleserver.ga")
        await ctx.send(embed=embed)
        print(f'{ctx.author} used pesten for {arg1}')
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(
            name="Usage:", value="`-pesten [person]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name='hit')
async def hit(ctx, person):
    try:
        message = ctx.message
        sender = ctx.author
        gifs = ["https://media.giphy.com/media/srD8JByP9u3zW/giphy.gif",
                "https://media.giphy.com/media/UbzayP2FNPWbm/giphy.gif",
                "https://media.giphy.com/media/vxvNnIYFcYqEE/giphy.gif",
                "https://media.giphy.com/media/Hz3YLyGYc15Oo/giphy.gif",
                "https://media.giphy.com/media/s5zXKfeXaa6ZO/giphy.gif",
                "https://media.giphy.com/media/gSIz6gGLhguOY/giphy.gif",
                "https://media.giphy.com/media/3XlEk2RxPS1m8/giphy.gif", "https://tenor.com/Ez39.gif",
                "https://tenor.com/WTzk.gif", "https://tenor.com/vX72.gif", "https://tenor.com/uSYA.gif",
                "https://tenor.com/oIyd.gif", "https://tenor.com/ycLl.gif", "https://tenor.com/27xQ.gif"]
        await message.delete()
        await ctx.send(f'{random.choice(gifs)}')
        await ctx.send('{} got hit by {}'.format(person, sender))
        print(f'{ctx.author} hit {person}')
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(name="Usage:", value="`-hit [person]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name='shovel')
async def shovel(ctx, person):
    try:
        message = ctx.message
        sender = ctx.author
        await message.delete()
        await ctx.send(f'{random.choice(shovels)}')
        await ctx.send('{} got shoveled by {}'.format(person, sender))
        print(f'{ctx.author} shoveled {person}')
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(
            name="Usage:", value="`-shovel [person]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name='8ball')
async def _8ball(ctx, *, question):
    responses = ["maybe", "nope", 'jep', 'nah',
                 'big chance', 'hell no', 'no doubt']
    await ctx.send(f'{random.choice(responses)}')
    print(f'{ctx.author} used 8ball: {question}')


@client.command(name='rus')
async def rus(ctx):
    responses = ['Click', 'Click', 'Click', 'Click', 'Click', 'BANG! 💥']
    clickresponses = ["Lucky!", "You're lucky!",
                      "Still alive", "Easy, still alive"]
    dieresponses = ["You died!", "Rest in peace my friend",
                    "You're dead!", "You lose!", "Auwch...", "This is so sad...", "Insert sad noises"]
    clicks = random.choice(clickresponses)
    response = random.choice(responses)
    die = random.choice(dieresponses)
    if response == 'BANG! 💥':
        embed = discord.Embed(title="Russian Roulette", color=0xff9500)
        embed.set_thumbnail(
            url="https://emojis.slackmojis.com/emojis/images/1558097714/5705/rip.png?1558097714")
        embed.add_field(name="Bang 💥", value=f"{die}", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Russian Roulette", color=0xff9500)
        embed.set_thumbnail(
            url="https://cdn.emojidex.com/emoji/seal/relieved.png?1417136196")
        embed.add_field(name="Click", value=f"{clicks}", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name='ruslonely')
async def ruslonely(ctx):
    responses = ["Click", "Click", 'Click', 'Click', 'Click', 'BANG! 💥']
    random.shuffle(responses)
    for noice in responses:
        if noice == "BANG! 💥":
            embed = discord.Embed(title="Russian Roulette",
                                  description=f'{noice}', color=0xff9500)
            embed.set_footer(
                text=f"Pineappleserver.ga | It took you {1 + responses.index(noice)} tries")
            await ctx.send(embed=embed)
            return
        else:
            embed = discord.Embed(title="Russian Roulette",
                                  description=f'{noice}', color=0xff9500)
            embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
            await ctx.send(embed=embed)
        await asyncio.sleep(1)

    print(f'{ctx.author} used rus command')


@client.command(name='burn')
async def burn(ctx, person):
    message = ctx.message
    await message.delete()
    await ctx.send("https://tenor.com/view/stranger-things-fire-flame-gif-14920648")
    await ctx.send("{} just got burned!".format(person))
    print(f'{ctx.author} burned {person}')


@client.command(name='circle')
async def circle(ctx):
    kaarten = ["One is for all", "Two is for you", "Three is for me", "Four for the hoes", "Russian Roulette",
               "Six for the dicks", "Seven point to heaven",
               "Eight make a date", "Nine make a rhyme", "Ten is category.", "Jack: Never have i ever",
               "Question queen", "King: Make a rule", ]

    sender = ctx.author

    embed = discord.Embed(title="Circle of Death",
                          description="drinking game", color=0xff9500)
    embed.set_thumbnail(
        url="https://icons.veryicon.com/png/o/food--drinks/food-icon/beer-27.png")
    embed.add_field(
        name="Order:", value=f"{random.choice(kaarten)}", inline=True)
    embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
    await ctx.send(embed=embed)
    print(f'{ctx.author} used circle of death')


@client.command(name="wyr")
async def wyr(ctx):
    wouldyourather = random.choice(wyrlist)
    embed = discord.Embed(title="Would you rather",
                          description=f"{wouldyourather}", color=0x0a4d8b)
    embed.set_thumbnail(
        url="https://image.freepik.com/free-vector/two-possible-choices-design_1133-16.jpg")
    embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
    await ctx.send(embed=embed)


@client.command(name="coin")
async def coin(ctx):
    flip = random.choice(["Heads", "Tails"])
    if flip == "Tails":
        embed = discord.Embed(title="Flip a coin",
                              description="Tails", color=0x0a4d8b)
        embed.set_thumbnail(
            url="https://www.nicepng.com/png/full/84-848244_1-euro-euro-coin-png.png")
        embed.set_footer(text=f"Pineappleserver.ga")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Flip a coin",
                              description="Heads", color=0x0a4d8b)
        embed.set_thumbnail(
            url="https://touchcoins.moneymuseum.com/coins_media/Republic-of-Austria-1-Euro-2002/1367/obverse.png")
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


# POLL COMMANDS


@client.command(name='poll')
async def poll(ctx, *, text):
    try:
        message = ctx.message
        await message.delete()
        msg = await ctx.send(f"{text}")
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")
        print(f'{ctx.author} made a poll: {text}')
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(name="Usage:", value="`-poll [message]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name='choose')
async def choose(ctx, arg1, arg2):
    try:
        msg = ctx.message
        await msg.delete()
        embed = discord.Embed(
            title="Poll", description="Choose by reacting 1 or 2", color=0xff9500)
        embed.add_field(name="{}".format(arg1), value="vote 1️⃣", inline=True)
        embed.add_field(name="{}".format(arg2), value="vote 2️⃣", inline=True)
        embed.set_footer(text="Pineappleserver.ga")
        message = await ctx.send(embed=embed)
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        print(f"{ctx.author} used the choose cmd. Options {arg1} and {arg2}")
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(
            name="Usage:", value="`-choose \"[option1]\" \"[option2]\"`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


# INFORMATION COMMANDS


@client.command(name='website')
async def website(ctx):
    embed = discord.Embed(title="Website", url="https://www.pineappleserver.ga/",
                          description="You can visit our website for more information about the server by clicking on the title.",
                          color=0x0a4d8b)
    embed.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    embed.set_thumbnail(
        url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
    await ctx.send(embed=embed)
    print(f'{ctx.author} used Website cmd')


@client.command(name='invite')
async def invite(ctx):
    await ctx.send('The invite link has been sent to you in a dm!')
    await ctx.author.send(':link:  **- Pineapple invite url-** \n \nhttps://discord.com/invite/c5N3UxT')
    message = ctx.message
    await message.add_reaction("✅")
    print(f'{ctx.author} used Invite cmd')


@client.command(name='levels')
async def levels(ctx):
    embed = discord.Embed(title="Levels", url="https://mee6.xyz/leaderboard/456754639031762944",
                          description="Pineapple server levels", color=0x0a4d8b)
    embed.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
    await ctx.send(embed=embed)
    print(f'{ctx.author} used Levels cmd')


@client.command(name="chamilo")
async def chamilo(ctx):
    embed = discord.Embed(title="HoGent", url="https://login.hogent.be/",
                          description="Hogent login", color=0xffffff)
    embed.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    embed.set_thumbnail(
        url="https://fedserv.ads.hogent.be/adfs/portal/logo/logo.png?id=ED23A82D0E5C16C313E81FBCAE1AB77DF511C0650DEC60879D1607737A4213A6")
    embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
    await ctx.send(embed=embed)
    print(f'{ctx.author} used Chamilo cmd')


@client.command(name='ufora')
async def ufora(ctx):
    embed = discord.Embed(title="UGent", url="https://login.ugent.be/login?",
                          description="UGent login", color=0xffffff)
    embed.set_author(
        name="Pineapple", icon_url="https://pineappleserver.ga/assets/images/pineapple-transp.png")
    embed.set_thumbnail(url="https://www.ugent.be/logo.png")
    embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
    await ctx.send(embed=embed)
    print(f'{ctx.author} used Ufora cmd')


# API COMMANDS


@client.command(name='shorturl')
async def shorturl(ctx, arg1, arg2):
    try:
        key = '9999edf2914f0da88e0224b9b10ba035db4eb'
        url = urllib.parse.quote('{}'.format(arg1))
        name = '{}'.format(arg2)
        r = requests.get(
            'http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url, name))
        print("{}".format(r))
        d = r.json()
        short = d["url"]["shortLink"]
        await ctx.send(":link:  **- Short url -** \n \n <{}>".format(short))
        print(f"{ctx.author} used shorturl for {arg1} and called it {arg2}")
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(
            name="Usage:", value="`-shorturl [url] [name]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name='iplookup')
async def iplookup(ctx, ip):
    try:
        r = requests.get(
            f'http://api.ipstack.com/{ip}?access_key=470a28351104ed5b6aa6259fe76baf9a&format=1')
        d = r.json()
        ip = d["ip"]
        soort = d["type"]
        land = d["country_name"]
        stad = d["city"]
        zip = d["zip"]
        lat = d["latitude"]
        long = d["longitude"]
        embed = discord.Embed(
            title="IP lookup", description="Find the location of an IP adress (not always accurate)", color=0x002aff)
        embed.set_thumbnail(
            url="https://pngimg.com/uploads/hacker/hacker_PNG33.png")
        embed.add_field(name=f"{soort}", value=f"{ip}", inline=False)
        embed.add_field(name="City", value=f"{stad}", inline=True)
        embed.add_field(name="Zip", value=f"{zip}", inline=True)
        embed.add_field(name="Latitude", value=f"{lat}", inline=False)
        embed.add_field(name="Longitude", value=f"{long}", inline=True)
        embed.add_field(name="Country", value=f"{land}", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)
        print(f"{ctx.author} looked up {ip}")
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(name="Usage:", value="`-iplookup [ip]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name='qr')
async def qr(ctx, url):
    try:
        await ctx.send(f"https://www.qrtag.net/api/qr_9.png?url={url}")
        print(f"{ctx.author} made a qr code for {url}")
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(name="Usage:", value="`-qr [url]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name='screenshot')
async def screenshot(ctx, url):
    try:

        msg = await ctx.send('Screenshot is processing!')
        r = requests.get(
            f'https://screenshotapi.net/api/v1/screenshot?url={url}&full_page=true&fresh=true')
        d = r.json()
        screen = d["screenshot"]
        await ctx.send(f'{screen}')
        await msg.delete()
        print(f"{ctx.author} made a screenshot from {url}")
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(
            name="Usage:", value="`-screenshot [url]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name="movie")
async def movie(ctx, *, name):
    try:
        movie = name
        r = requests.get(
            f'https://api.themoviedb.org/3/search/movie?api_key=5e765da300e3f42f23ba5924af46b6c5&query={movie}')
        d = r.json()
        title = d["results"][0]["original_title"]
        description = d["results"][0]["overview"]
        rating = d["results"][0]["vote_average"]
        date = d["results"][0]["release_date"]
        movieimg = d["results"][0]["poster_path"]
        lang = d["results"][0]["original_language"]

        embed = discord.Embed(
            title=f"{title}", description=f"{description}", color=0xffc800)
        embed.add_field(name="⭐Rating", value=f"{rating}/10", inline=True)
        embed.add_field(name="⌛ Release date", value=f"{date}", inline=True)
        embed.add_field(name="💬 Language", value=f"{lang}", inline=True)
        embed.set_image(
            url=f"https://www.themoviedb.org/t/p/w600_and_h900_bestv2{movieimg}")
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(name="Usage:", value="`-movie [name]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name="fruit")
async def fruit(ctx, fruit):
    vrucht = fruit
    try:

        r = requests.get(f"https://www.fruityvice.com/api/fruit/{vrucht}")
        d = r.json()
        name = d["name"]
        carbo = d["nutritions"]["carbohydrates"]
        pro = d["nutritions"]["protein"]
        fat = d["nutritions"]["fat"]
        calo = d["nutritions"]["calories"]
        sug = d["nutritions"]["sugar"]

        embed = discord.Embed(
            title=f"{name}", description="nutritional values (/100g:", color=0xffc800)
        embed.add_field(name="Calories", value=f"{calo}", inline=True)
        embed.add_field(name="Carbohydrates", value=f"{carbo}g", inline=True)
        embed.add_field(name="Protein", value=f"{pro}g", inline=True)
        embed.add_field(name="Fat", value=f"{fat}g", inline=True)
        embed.add_field(name="Sugar", value=f"{sug}g", inline=True)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(name="Usage:", value="`-fruit [name]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name="starwars")
async def starwars(ctx):
    try:
        quote = random.choice(starwarsquotes)
        embed = discord.Embed(
            title="Star Wars", description=f"{quote}", color=0xffc800)
        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/694px-Star_Wars_Logo.svg.png")
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(name="Usage:", value="`-starwars`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name="yoda")
async def yoda(ctx, *, text):
    try:
        message = text
        r = requests.get(
            f"https://yoda-api.appspot.com/api/v1/yodish?text={message}")
        d = r.json()
        output = d["yodish"]
        embed = discord.Embed(
            title="Yoda:", description=f"{output}", color=0x0ecc00)
        embed.set_thumbnail(
            url="https://static0.cbrimages.com/wordpress/wp-content/uploads/2020/05/yoda-revenge-of-the-sith.jpg?q=50&fit=crop&w=960&h=500")
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(name="Usage:", value="`-yoda [message]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name="roastme")
async def roastme(ctx):
    try:
        r = requests.get(
            f"https://evilinsult.com/generate_insult.php?lang=en&type=json")
        d = r.json()
        output = d["insult"]
        embed = discord.Embed(
            title="Roast me:", description=f"{output}", color=0xffee00)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(name="Usage:", value="`-roastme`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


@client.command(name="artist")
async def artist(ctx, *, artist):
    try:
        r = requests.get(
            f"https://api.deezer.com/artist/{artist}")
        d = r.json()
        name = d["name"]
        link = d["link"]
        picture = d["picture_xl"]
        followers = d["nb_fan"]
        albums = d["nb_album"]

        embed = discord.Embed(title=f"{name}", url=f"{link}", color=0x00ccff)
        embed.set_author(
            name="Deezer", icon_url="https://media.glassdoor.com/sqls/786653/deezer-squarelogo-1557480215084.png")
        embed.add_field(name="👨‍👩‍👧‍👦 Followers",
                        value=f"{followers}", inline=True)
        embed.add_field(name="💽 Albums", value=f"{albums}", inline=True)
        embed.set_image(
            url=f"{picture}")
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="⚠ Command error", color=0xff4000)
        embed.add_field(name="Usage:", value="`-artist [name]`", inline=False)
        embed.set_footer(text=f"Pineappleserver.ga | {ctx.author}")
        await ctx.send(embed=embed)


# FUN API COMMANDS


@client.command(name='doggo')
async def doggo(ctx):
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    d = r.json()
    short = d["message"]
    await ctx.send("{}".format(short))
    print(f'{ctx.author} used doggo cmd')


@client.command(name='seal')
async def seal(ctx, top, bottom):
    await ctx.send(ctx.author.mention)
    await ctx.send(f'http://apimeme.com/meme?meme=Awkward-Moment-Sealion&top={top}&bottom={bottom}')
    msg = ctx.message
    await msg.delete()
    print(f'{ctx.author} used seal meme cmd. Top: {top} | Bottom: {bottom}')


@client.command(name='sanders')
async def sanders(ctx, top, bottom):
    await ctx.send(ctx.author.mention)
    await ctx.send(
        f'http://apimeme.com/meme?meme=Bernie-I-Am-Once-Again-Asking-For-Your-Support&top={top}&bottom={bottom}')
    msg = ctx.message
    await msg.delete()
    print(f'{ctx.author} used Sanders meme cmd. Top: {top} | Bottom: {bottom}')


@client.command(name='sponge')
async def sponge(ctx, top, bottom):
    await ctx.send(ctx.author.mention)
    await ctx.send(f'http://apimeme.com/meme?meme=Chicken-Bob&top={top}&bottom={bottom}')
    msg = ctx.message
    await msg.delete()
    print(f'{ctx.author} used sponge meme cmd. Top: {top} | Bottom: {bottom}')


@client.command(name='disaster')
async def disaster(ctx, top, bottom):
    await ctx.send(ctx.author.mention)
    await ctx.send(f'http://apimeme.com/meme?meme=Disaster-Girl&top={top}&bottom={bottom}')
    msg = ctx.message
    await msg.delete()
    print(f'{ctx.author} used disaster meme cmd. Top: {top} | Bottom: {bottom}')


@client.command(name='drunkbaby')
async def drunkbaby(ctx, top, bottom):
    await ctx.send(ctx.author.mention)
    await ctx.send(f'http://apimeme.com/meme?meme=Drunk-Baby&top={top}&bottom={bottom}')
    msg = ctx.message
    await msg.delete()
    print(f'{ctx.author} used drunk baby meme cmd. Top: {top} | Bottom: {bottom}')


@client.command(name='randomfact')
async def randomfact(ctx):
    r = requests.get('https://uselessfacts.jsph.pl/random.json')
    d = r.json()
    short = d["text"]
    await ctx.send("{}".format(short))
    print(f'{ctx.author} used randomfact cmd')


@client.command(name='lovecalc')
async def lovecalc(ctx, pers1, pers2):
    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"fname": "{}".format(pers1), "sname": "{}".format(pers2)}

    headers = {
        'x-rapidapi-key': "56d547268amshd523bc34916b2eep15def3jsnfcd6610c4e3a",
        'x-rapidapi-host': "love-calculator.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    d = response.json()
    p1 = d["fname"]
    p2 = d["sname"]
    desc = d["result"]
    perc = d["percentage"]

    embed = discord.Embed(title=f"{p1} x {p2}", color=0xff4747)
    embed.set_author(name="Love Calculator")
    embed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Heart_coraz%C3%B3n.svg/1200px-Heart_coraz%C3%B3n.svg.png")
    embed.add_field(name=f"{perc}%", value=f"{desc}", inline=True)
    embed.set_footer(text="Pineappleserver.ga")
    await ctx.send(embed=embed)
    print(f"{ctx.author} used lovecalc with {pers1} and {pers2} ({perc})")


client.run(TOKEN)
