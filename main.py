import discord, os, time, sys, json, datetime, asyncio
from discord.ext import commands
from aiohttp import request
from datetime import datetime
now = datetime.now()
intents = discord.Intents().all()

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)
PREFIX=config["prefix_settings"]["prefix"]
TOKEN = config["token"]
RESTART_MESSAGE = config["restart_message"]
SHUTDOWN_MESSAGE = config["shutdown_message"]
if config["prefix_settings"]["use_space"] == True:
    prefix = PREFIX + ' '

client = commands.Bot(command_prefix=PREFIX, help_command=None, intents = intents)

@client.event
async def on_ready():
    current_time = now.strftime("%H:%M:%S")
    print('--------------------------------------\nLogged in as: {0.user}'.format(client),f'\nPrefix => {PREFIX}', '\nLogged in at', current_time, '\nID of the Client =', client.user.id, '\n---------------------------------------')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="PurrBot's API..."))






## Moderation Commands

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command() # Restarting the Bot
@commands.is_owner()
async def r(ctx): 
    await ctx.send(RESTART_MESSAGE)
    restart_bot()


@client.command() #Shutting down the Bot
@commands.is_owner()
async def s(ctx):
    await ctx.send(SHUTDOWN_MESSAGE)
    await client.close()


@client.command() # Can toggle Commands from within Discord
@commands.is_owner()
async def toggle(ctx, *, command):
    command = client.get_command(command)
    if command is None:
        await ctx.send("I can't find a command with this name!")

    elif ctx.command == command:
        await ctx.send("You cannot disable this command with your permissions!")

    else:
        command.enabled = not command.enabled
        ternary = "enabled" if command.enabled else "disabled"
        await ctx.send(f'I have {ternary} {command.qualified_name} for you!')


@client.command() # See all available Commands, im to lazy to make a help Command :)
@commands.has_permissions(ban_members=True)
async def l1(ctx):
    commands = [c.name for c in client.commands]
    await ctx.send(commands)


@client.command(pass_context=True) #Latency Command
async def ping(ctx):
    """ Pong! """
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")








##PurrBot's SFW EndPoints

@client.command()
async def background(ctx):
    URL = "https://purrbot.site/api/img/sfw/background/img" #Returns a random selected Welcome Background Image
    async with request("GET",URL,headers={}) as response:
        if response.status==200:
            data = await response.json()
            embed = discord.Embed(colour=ctx.author.colour)
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Api returned a {response.status} Status.")

@client.command()
async def bite(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/bite/gif"  ## Returns a bite gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} bites themselves!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} bites {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def blush(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/blush/gif"  ## Returns a blush gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} blushes!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} blushes at {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def comfy(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/comfy/gif"  ## Returns a comfy gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is comfy!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is comfy with {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def cry(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/cry/gif"  ## Returns a crying gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is crying!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is crying with {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def cuddle(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/cuddle/gif"  ## Returns a cuddling gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is cuddeling with themselves!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is cuddeling with {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def dance(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/dance/gif"  ## Returns a dancing gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is dancing!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is dancing with {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def eeveeg(ctx):
    URL = "https://purrbot.site/api/img/sfw/eevee/gif"  ## Returns an eevee gif
    async with request("GET",URL,headers={}) as response:
        if response.status==200:
            data = await response.json()
            embed = discord.Embed(colour=ctx.author.colour, title=f'Here is an eevee Gif for {ctx.author.name}!')
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def eeveei(ctx):
    URL = "https://purrbot.site/api/img/sfw/eevee/img"  ## Returns an eevee img
    async with request("GET",URL,headers={}) as response:
        if response.status==200:
            data = await response.json()
            embed = discord.Embed(colour=ctx.author.colour, title=f'Here is an eevee Image for {ctx.author.name}!')
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def feed(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/feed/gif"  ## Returns a feeding gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is feeding themselves!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is feeding {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def fluff(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/fluff/gif"  ## Returns a fluffy gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is fluffy!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} thinks {member.display_name} is fluffy!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


# Holo command isnt working, getting a 403 response Status (will be listed if it is working in the future) (remove the # infront of the code to try it)

#@client.command()
#async def holo(ctx, member:discord.Member=None):
    #URL = "https://purrbot.site/api/img/sfw/holo/gif"  ## Returns a gif from Holo from "Spice and Wolf"
    #async with request("GET",URL,headers={}) as response:
        #if response.status==200:
            #data = await response.json()
            #embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} thinks {member.display_name} is fluffy!')
            #embed.set_image(url=data["link"])
            #await ctx.send(embed=embed)
        #else:
            #await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def hug(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/hug/gif"  ## Returns a hugging gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is hugging themselves!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is hugging {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def icon(ctx):
    URL = "https://purrbot.site/api/img/sfw/icon/img"  ## Returns a randomly selected Welcome Icon
    async with request("GET",URL,headers={}) as response:
        if response.status==200:
            data = await response.json()
            embed = discord.Embed(colour=ctx.author.colour)
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def kiss(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/kiss/gif"  ## Returns a kissing gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is kissing themselves!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is kissing {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def kitsune(ctx):
    URL = "https://purrbot.site/api/img/sfw/kitsune/img"  ## Returns a kitsune img
    async with request("GET",URL,headers={}) as response:
        if response.status==200:
            data = await response.json()
            embed = discord.Embed(colour=ctx.author.colour)
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def lick(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/lick/gif"  ## Returns a licking gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is licking themselves!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is licking {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def nekoi(ctx):
    URL = "https://purrbot.site/api/img/sfw/neko/img"  ## Returns a neko img
    async with request("GET",URL,headers={}) as response:
        if response.status==200:
            data = await response.json()
            embed = discord.Embed(colour=ctx.author.colour)
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def nekog(ctx):
    URL = "https://purrbot.site/api/img/sfw/neko/gif"  ## Returns a neko gif
    async with request("GET",URL,headers={}) as response:
        if response.status==200:
            data = await response.json()
            embed = discord.Embed(colour=ctx.author.colour)
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def okami(ctx):
    URL = "https://purrbot.site/api/img/sfw/okami/img"  ## Returns a okami img
    async with request("GET",URL,headers={}) as response:
        if response.status==200:
            data = await response.json()
            embed = discord.Embed(colour=ctx.author.colour)
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def pat(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/pat/gif"  ## Returns a patting gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is patting themselves!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is patting {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def poke(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/poke/gif"  ## Returns a poking gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is poking themselves!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is poking {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def senko(ctx):
    URL = "https://purrbot.site/api/img/sfw/senko/img"  ## Returns a senko img from the Anime "The Helpful Fox Senko-san"
    async with request("GET",URL,headers={}) as response:
        if response.status==200:
            data = await response.json()
            embed = discord.Embed(colour=ctx.author.colour)
            embed.set_image(url=data["link"])
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"API returned a {response.status} Status.")


# Slapping command isnt working, getting a 403 response Status (will be listed if it is working in the future) (remove the # infront of the code to try it)

#@client.command()
#async def slap(ctx, member:discord.Member=None):
    #URL = "https://purrbot.site/api/img/sfw/slapping/gif"  ## Returns a slapping gif
    #async with request("GET",URL,headers={}) as response:
        #if member==None:
            #if response.status==200:
                #data = await response.json()
                #embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is slapping themselves!")
                #embed.set_image(url=data["link"])
                #await ctx.send(embed=embed)
            #else:
                #await ctx.send(f"Api returned a {response.status} Status.")
        #else:
            #if response.status==200:
                #data = await response.json()
                #embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is slapping {member.display_name}!')
                #embed.set_image(url=data["link"])
                #await ctx.send(embed=embed)
            #else:
                #await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def smile(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/smile/gif"  ## Returns a smiling gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is smiling at themselves!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is smiling at {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")


# Tail command isnt working, getting a 403 response Status (will be listed if it is working in the future) (remove the # infront of the code to try it)

#@client.command()
#async def tail(ctx, member:discord.Member=None):
    #URL = "https://purrbot.site/api/img/sfw/tial/gif"  ## Returns a tail wagging gif
    #async with request("GET",URL,headers={}) as response:
        #if member==None:
            #if response.status==200:
                #data = await response.json()
                #embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is wagging theier tail!")
                #embed.set_image(url=data["link"])
                #await ctx.send(embed=embed)
            #else:
                #await ctx.send(f"Api returned a {response.status} Status.")
        #else:
            #if response.status==200:
                #data = await response.json()
                #embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is wagging theier tail at {member.display_name}!')
                #embed.set_image(url=data["link"])
                #await ctx.send(embed=embed)
            #else:
                #await ctx.send(f"API returned a {response.status} Status.")


@client.command()
async def tickle(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/sfw/tickle/gif"  ## Returns a tickling gif
    async with request("GET",URL,headers={}) as response:
        if member==None:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title = f"{ctx.author.name} is tickling themselves!")
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Api returned a {response.status} Status.")
        else:
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is tickling {member.display_name}!')
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")







#PurrBot's NSFW EndPoints

@client.command()
async def anal(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/nsfw/anal/gif"  ## Returns an anal gif
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if member==None:
                if response.status==200:
                    data = await response.json()
                    embed = discord.Embed(colour=ctx.author.colour)
                    embed.set_image(url=data["link"])
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Api returned a {response.status} Status.")
            else:
                if response.status==200:
                    data = await response.json()
                    embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is fucking {member.display_name} anal!')
                    embed.set_image(url=data["link"])
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


@client.command()
async def blowjob(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/nsfw/blowjob/gif"  ## Returns a blowjob gif
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if member==None:
                if response.status==200:
                    data = await response.json()
                    embed = discord.Embed(colour=ctx.author.colour)
                    embed.set_image(url=data["link"])
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Api returned a {response.status} Status.")
            else:
                if response.status==200:
                    data = await response.json()
                    embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is giving {member.display_name} a blowjob!')
                    embed.set_image(url=data["link"])
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


@client.command()
async def cum(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/nsfw/cum/gif"  ## Returns a cumming gif
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if member==None:
                if response.status==200:
                    data = await response.json()
                    embed = discord.Embed(colour=ctx.author.colour, title = f'{ctx.author.name} is cumming!')
                    embed.set_image(url=data["link"])
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Api returned a {response.status} Status.")
            else:
                if response.status==200:
                    data = await response.json()
                    embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is cumming on {member.display_name}!')
                    embed.set_image(url=data["link"])
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


# Fuck command isnt working, getting a 403 response Status (will be listed if it is working in the future) (remove the # infront of the code to try it)

#@client.command()
#async def fuck(ctx, member:discord.Member=None):
    #URL = "https://purrbot.site/api/img/nsfw/fuuck/gif"  ## Returns a fucking gif
    #async with request("GET",URL,headers={}) as response:
        #if ctx.channel.is_nsfw():
            #if member==None:
                #if response.status==200:
                    #data = await response.json()
                    #embed = discord.Embed(colour=ctx.author.colour)
                    #embed.set_image(url=data["link"])
                    #await ctx.send(embed=embed)
                #else:
                    #await ctx.send(f"Api returned a {response.status} Status.")
            #else:
                #if response.status==200:
                    #data = await response.json()
                    #embed = discord.Embed(colour=ctx.author.colour, title=f'{ctx.author.name} is fucking {member.display_name}!')
                    #embed.set_image(url=data["link"])
                    #await ctx.send(embed=embed)
                #else:
                    #await ctx.send(f"API returned a {response.status} Status.")
        #else:
            #await ctx.send("This channel needs to be an NSFW Channel!")


@client.command()
async def nekonsfwi(ctx):
    URL = "https://purrbot.site/api/img/nsfw/neko/img"  ## Returns a nsfw neko img 
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour)
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


@client.command()
async def nekonsfwg(ctx):
    URL = "https://purrbot.site/api/img/nsfw/neko/gif"  ## Returns a nsfw neko gif 
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour)
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


@client.command()
async def pussylick(ctx, member:discord.Member=None):
    URL = "https://purrbot.site/api/img/nsfw/pussylick/gif"  ## Returns a pussylicking gif
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if member==None:
                if response.status==200:
                    data = await response.json()
                    embed = discord.Embed(colour=ctx.author.colour, title = f'{ctx.author.name} is licking theier own pussy!')
                    embed.set_image(url=data["link"])
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Api returned a {response.status} Status.")
            else:
                if response.status==200:
                    data = await response.json()
                    embed = discord.Embed(colour=ctx.author.colour, title=f"{ctx.author.name} is licking on {member.display_name}'s pussy!")
                    embed.set_image(url=data["link"])
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


@client.command()
async def solo(ctx):
    URL = "https://purrbot.site/api/img/nsfw/solo/gif"  ## Returns a solo gif 
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour)
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


@client.command()
async def threesome_fff(ctx):
    URL = "https://purrbot.site/api/img/nsfw/threesome_fff/gif"  ## Returns a randomly selected Threesome Gif (Females only)
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour)
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


@client.command()
async def threesome_ffm(ctx):
    URL = "https://purrbot.site/api/img/nsfw/threesome_ffm/gif"  ## Returns a randomly selected Threesome Gif (2 Females, 1 Male)
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour)
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


@client.command()
async def threesome_mmf(ctx):
    URL = "https://purrbot.site/api/img/nsfw/threesome_mmf/gif"  ## Returns a randomly selected Threesome Gif (1 Female, 2 Males)
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour)
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


@client.command()
async def yaoi(ctx):
    URL = "https://purrbot.site/api/img/nsfw/yaoi/gif"  ## Returns a yaoi gif
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour)
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


@client.command()
async def yuri(ctx):
    URL = "https://purrbot.site/api/img/nsfw/yuri/gif"  ## Returns a yuri gif
    async with request("GET",URL,headers={}) as response:
        if ctx.channel.is_nsfw():
            if response.status==200:
                data = await response.json()
                embed = discord.Embed(colour=ctx.author.colour)
                embed.set_image(url=data["link"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"API returned a {response.status} Status.")
        else:
            await ctx.send("This channel needs to be an NSFW Channel!")


client.run(TOKEN)