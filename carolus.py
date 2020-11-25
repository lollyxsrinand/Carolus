from imports import *

valid_prefixes = ['<','>','!','#','$','%','^','&','*','(',')','[',']','{','}',':',';',"'",'"','/','\\','-','+','=']

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    return prefixes[str(message.guild.id)]
     
bot = commands.Bot(command_prefix=get_prefix)
bot.remove_command('help')

def valid_prefix(pre):
    return pre in valid_prefixes
    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    if message.channel.name=='carol-chat' and message.content[0]!='>':
        res = kernel.respond(message.content)
        if res == "":
            res = message.content
        who = str(message.author)[0:-5]
        await message.channel.send(f"`{who}`: {res}")
    await bot.process_commands(message) 
    
@bot.event
async def on_guild_join(guild):
    """Creating Text Channel and saying Thanks for adding"""
    await guild.create_text_channel('carol-chat')
    channel = discord.utils.get(guild.channels, name='general')
    await channel.send("Thanks for adding me :>")
    """Prefix"""
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    prefixes[str(guild.id)] = '>'
    
    with open('prefixes.json', 'w')  as f:
        json.dump(prefixes, f, indent=4)
@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    prefixes.pop(str(guild.id))
    
    with open('prefixes.json', 'w')  as f:
        json.dump(prefixes, f, indent=4)
    
@bot.command()
async def prefix(ctx, pref):
    
    if not valid_prefix(pref):
        await ctx.send(f"`{pref}` is not a valid prefix, length of prefix must be 1 and shouldn't contain Alphabet or numbers")
        return
    
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    guild_id = str(ctx.guild.id)
    prefixes[guild_id] = pref
    
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    
    await ctx.send(f"Prefix changed to `{pref}` :)")
    
@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name="clients on discord | >help")
    await bot.change_presence(status=discord.Status.online, activity=activity) 
    print("Bot ready")
    
"""LOADING COGS"""
bot.load_extension('cogs.MusicCommands')
bot.load_extension('cogs.GenCommands')
bot.load_extension('cogs.FunCommands')
bot.load_extension('cogs.MiscCommands')
"""END OF LOADING COGS"""

"""LOADING AIML"""
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
"""END OF LOADING AIML"""

bot.run('Nzc0NTMwMjcwNTA1MjA1ODAx.X6ZHhg.SG-awP6hOU8kntE5o9yyZZdV5iQ') #RUNNING BOT