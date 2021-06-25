from imports import *
help_comds = {
    'help' : 'shows list of commands',
    'invite' : 'Invite me with a link that I give',
    'math' : 'Does math calculations for you [This is python based math so you can do like 2**5 for getting 2^5]',
    'avatar' : 'Shows mentioned user avatar if mentioned, otherwise shows avatar of requestor\nAliases - avatar, pfp, av',
    'servericon' : 'Shows server icon\nAliases - servericon, sico',
    'youtube' : 'Gives the top most video url of a search from youtube\nAliases - youtube, yt',
    'userinfo' : 'Gives information about a user'
}

class Help(commands.Cog):
        
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(aliases=['halp','welp','tf'])
    async def help(self, ctx):
        msg = str(ctx.message.content)
        msg = msg.replace(msg[0],'')
        if msg == 'help' or msg == 'halp' or msg == 'welp' or msg == 'tf':
            channel = discord.utils.get(ctx.guild.channels, name='carol-chat')
            if channel is not None:
                channel_id=str(channel.id)
                channel_id=f"<#{channel_id}>"
            if channel is None:
                channel_id='#carolus-chat'
            embed=discord.Embed(title="Here is how you can get along with me :", description=f"**Contacting <@{702122543410184253}> for any kind of suggestions or a bug report would be appreciated**", color=0x73e600)
            embed.add_field(name="<:general:818432179750305842> General", value="`help` | `invite` | `math` |\n`avatar` | `servericon` | `google` | `youtube`\n `userinfo` | `serverinfo`", inline=False)
            embed.add_field(name="<:settings:818425966379794453> Admin ",   value="`kick` | `ban` | `clear` |\n `lock` | `unlock`", inline = False)
            embed.add_field(name="<:fun:818425966531313754> Fun ",     value="`flip` | `choice` | `dmuser` |\n`slot` | `meme` | `say`", inline=False)
            embed.add_field(name="<:music:818432767523815425> Music ",   value="`join` | `play` | `stop` |\n`move` | `nowplaying` | `queue` |\n`skip` | `forceskip` | `loop` |\n`pause` | `resume` | `remove` |\n `shuffle` ", inline=False)
            embed.add_field(name="<:chat:818432878819934258> Chat ",    value=f"`Chat with AIML powered Carolus in` #carol-chat ` if you're interested.\nIf such channel doesn't exist, request admin to create one` ", inline=False)
            embed.add_field(name="<:invitation:818419988272513044> I'd love to join new servers", value=f"**[Invite](https://discord.com/api/oauth2/authorize?client_id=774530270505205801&permissions=8&scope=bot)**", inline=False)
            embed.set_footer(text="You can always get my prefix just by pinging me ツ")
            embed.set_author(name=f'Requested by {str(ctx.author)[:-5]}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await ctx.message.add_reaction("<:dm:818425964165201970>")
            await ctx.send("ok")

        else:
            try:
                await ctx.send(help_comds[msg.split()[1]])
            except:
                await ctx.send(f"Command `{msg.split()[1]}` not found")

    
def setup(bot):
    bot.add_cog(Help(bot))