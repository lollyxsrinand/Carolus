from imports import *

bot = commands.Bot(command_prefix='>')
bot.remove_command('help')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    if message.channel.name=='carol-chat' and message.content[0]!='>':
        res = kernel.respond(message.content)
        who = str(message.author)[0:-5]
        await message.channel.send(f'`{who}`: {res}')
    await bot.process_commands(message) 
    
@bot.event
async def on_guild_join(guild):
    await guild.create_text_channel('carol-chat')
    channel = discord.utils.get(guild.channels, name='general')
    await channel.send("Thanks for adding me :>")
    
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.invisible)
    print("Bot ready")
    
bot.load_extension('cogs.MusicCommands')
bot.load_extension('cogs.GenCommands')
bot.load_extension('cogs.FunCommands')
bot.load_extension('cogs.MiscCommands')
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
bot.run('Nzc0NTMwMjcwNTA1MjA1ODAx.X6ZHhg.SG-awP6hOU8kntE5o9yyZZdV5iQ')
