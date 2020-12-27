from imports import *

valid_prefixes = ['<','>','!','#','$','%','^','&','*','(',')','[',']','{','}',':',';','/','\\','-','+','=','.',',','?']

status = cycle(['clients on discord','>help | DM Bugs :>'])

""" GETTING PREFIX FOR THE PARTICULAR GUILD """
def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

""" CREATING BOT OBJECT """
bot = commands.Bot(command_prefix=get_prefix)
bot.remove_command('help')

""" CREATING CAROL-CHAT AND ADDING GUILD ID AND PREFIX IN PREFIXES.JSON ON GUILD JOIN"""
""" GETS CALLED WHEN BOT JOINS A GUILD """
@bot.event
async def on_guild_join(guild):
    """CREATING TEXT CHANNEL AND SAYING THANKS FOR ADDING"""
    await guild.create_text_channel('carol-chat')
    
    """ADDING GUILD ID TO JSON AND ASSIGNING DEFAULT PREFIX"""
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    prefixes[str(guild.id)] = '>'
    
    with open('prefixes.json', 'w')  as f:
        json.dump(prefixes, f, indent=4)


""" VALIDATING PREFIX """
def valid_prefix(pre):
    return pre in valid_prefixes

""" THIS FUNCTION GETS CALLED WHEN SOMEONE SENDS MESSAGE """
@bot.event
async def on_message(message):
    if message.author == bot.user:return # AVOIDING BOT TO RESPOND TO ITSELF 

    """ COMPLEX STUFF """
    if not message.guild and message.author != bot.user:
        if message.author.id==702122543410184253:
            user = await bot.fetch_user(int(str(message.content).split(' ')[0]))
            await user.send(' '.join(str(message.content).split(' ')[1:]))
            return
        user = await bot.fetch_user(702122543410184253)
        sender = f"<@{message.author.id}>"
        embed = discord.Embed(title = "Message for you",color=0x73e600)
        embed.add_field(name="Sender's id",value=f"```{message.author.id}```",inline=False)
        embed.add_field(name="Sender's name",value=sender,inline=False)
        embed.add_field(name="Message Content",value=f"```{message.content}```",inline=False)
        embed.set_author(name=sender,icon_url=message.author.avatar_url)
        embed.set_thumbnail(url=message.author.avatar_url)
        await user.send(embed=embed)
        return

    """ SENDING PREFIX OF BOT ON MENTION(LAZY TO ADD A COOLDOWN TO THIS)"""
    if bot.user.mentioned_in(message) and "@everyone" not in message.content:
        with open('prefixes.json', 'r') as file:
            prefixes = json.load(file)
            guild_prefix = prefixes[str(message.guild.id)]
        await message.channel.send(f"Hello! Prefix for this server is `{guild_prefix}`")
        return
    
    """AIML RESPONDS TO USER WHEN MESSAGE IN CAROL-CHAT APPEARS"""
    if 'carol-chat' in message.channel.name and message.content[0] not in valid_prefixes:
        if len(message.content)<500:
            res = kernel.respond(message.content)
            if res == "":
                res = message.content
            if   '@702122543410184253' in res:
                res = res.replace('@702122543410184253','<@702122543410184253>')
            who = str(message.author)[0:-5] 
            await message.channel.send(f"`{who}`: {res}")
        else:
            who = str(message.author)[0:-5]
            await message.channel.send(f"`{who}`: your message was more than 500 characters, So I couldn't respond")
    await bot.process_commands(message) 
    
""" REMOVES GUILD ID AND IT'S PREFIX FROM JSON """
@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    prefixes.pop(str(guild.id))
    
    with open('prefixes.json', 'w')  as f:
        json.dump(prefixes, f, indent=4)
    
""" LETS USER ASSIGN A NEW PREFIX """
@bot.command()
@commands.cooldown(5, 10, commands.BucketType.guild)
async def prefix(ctx, pref):
    """VALIDATING PPREFIX"""
    if not valid_prefix(pref):
        await ctx.send(f"`{pref}` is not a valid prefix, length of prefix must be 1 and shouldn't contain Alphabet or numbers")
        return
    
    """CHANGING GUILD DEFAULT PREFIX TO CUSTOM PREFIX"""
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    guild_id = str(ctx.guild.id)
    prefixes[guild_id] = pref
    
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    
    await ctx.send(f"Prefix changed to `{pref}` :)")

""" HANDLING THE COOLDOWN ERROR """
@prefix.error
async def prefix_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("You are trying to change prefix too quickly.Try after {:.0f}s".format(error.retry_after))

""" CHANGING BOT'S STATUS EVERY 5 SECONDS """
@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=next(status)))

""" HANDLING THE COMMAND NOT FOUND ERROR """
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title = "**Command Not Found!**",description = f"{ctx.author} try for a help command for a list of valid commands that I can work on.",color=0x73e600)
        await ctx.send(embed=embed)


@bot.event
async def on_ready():
    print((bot.ws.latency)*1000)
    change_status.start()
    print("Bot ready")
    
"""LOADING COGS"""
bot.load_extension('cogs.GenCommands')
bot.load_extension('cogs.ModCommands')
bot.load_extension('cogs.MusicCommands')
bot.load_extension('cogs.FunCommands')
bot.load_extension('cogs.HelpCommand')
"""END OF LOADING COGS"""

"""LOADING AIML"""
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
"""END OF LOADING AIML"""

"""RUNNING BOT"""
bot.run('Nzc0NTMwMjcwNTA1MjA1ODAx.X6ZHhg.SG-awP6hOU8kntE5o9yyZZdV5iQ')  