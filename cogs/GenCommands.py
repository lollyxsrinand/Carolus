from imports import *

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Here are my commands :", description="**My Prefix is** `>`", color=0x73e600)
        embed.add_field(name="General", value="help | ping | kick |\nclear ", inline=False)
        embed.add_field(name="Music", value="play | stop | move |\nnow | queue | skip |\nforceskip | pause | resume", inline=False)
        embed.add_field(name="Fun", value="flip | avatar | rand", inline=False)
        embed.add_field(name="Misc", value="google | youtube", inline = False)
        embed.add_field(name="AIML Chat",value="`Chat with AIML bot in carol-chat created by A.L.I.C.E foundation`")
        embed.set_author(name=f'Requested by {str(ctx.author)[:-5]}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @commands.command() 
    async def ping(self, ctx):
        print('ping was invoked')
        await ctx.send(f'Pong! {round(self.bot.latency*1000)}ms')
    
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def kick(self, ctx, member: discord.Member, *,reason=None):
        await member.kick(reason=reason)
            
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def clear(self, ctx,*, lim):
        await ctx.channel.purge(limit=int(lim))
    
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="Carolus invite", color=0x73e600)
        embed.add_field(name='[Invite](https://discord.com/api/oauth2/authorize?client_id=774530270505205801&permissions=8&scope=bot) me',value='me to any server')
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(General(bot))
