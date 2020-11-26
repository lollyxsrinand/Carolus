from imports import *
class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command()
    async def help(self, ctx):
        channel = discord.utils.get(ctx.guild.channels, name='carol-chat')
        if channel is not None:
            channel_id=str(channel.id)
            channel_id=f"<#{channel_id}>"
        if channel is None:
            channel_id='#carolus-chat'
        embed=discord.Embed(title="Here are my commands :", description="**You can always get my prefix by pinging me ツ**", color=0x73e600)
        embed.add_field(name="General", value="help | ping | kick |\nclear | prefix | pmath", inline=False)
        embed.add_field(name="Fun", value="flip | avatar | rand", inline=False)
        embed.add_field(name="Music", value="play | stop | move |\nnow | queue | skip |\nforceskip | pause | resume", inline=False)
        embed.add_field(name="Misc", value="google | youtube", inline = False)
        embed.add_field(name="Chat",value=f"`Chat with Carolus in` {channel_id} ` and have fun.\nIf such channel doesn't exist, request admin to create one` ")
        embed.set_footer(text="20 commands in total ツ")
        embed.set_author(name=f'Requested by {str(ctx.author)[:-5]}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        
    @commands.command() 
    async def ping(self, ctx):
        embed = discord.Embed(color=0x73e600)
        embed.add_field(name="Here goes my ping: ",value=f"{round(self.bot.latency*1000)}ms")
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def kick(self, ctx, member : discord.Member):
        await member.kick(reason="No reason Provided")
        await ctx.send(f"{ctx.author} has :boot: {member.mention}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, member : discord.Member):
        await member.ban(reason="No reason Provided")
        await ctx.send(f":boot: {member.mention}")       
                
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def clear(self, ctx,*, lim):
        await ctx.channel.purge(limit=int(lim))
    
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="Carolus invite", color=0x73e600)
        embed.add_field(name="I'd love to be invited to your server :D",value="[Invite Carolus](https://discord.com/api/oauth2/authorize?client_id=774530270505205801&permissions=8&scope=bot)")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def host(self, ctx):
        hos = "Third Party Hosting Service"
        latency = round(self.bot.latency*1000)
        if latency > 50:
            hos = "Local Host machine"
        embed = discord.Embed(color=0x73e600)
        embed.add_field(name="Hosted on: ",value=hos,inline=True)
        await ctx.send(embed = embed)
    @commands.command(aliases=['pmath'])
    async def pymath(self, ctx, *, ope):
        resp = eval(ope)
        if resp > 10**1000:
            resp = "The output was too big to be calcluated"
        await ctx.send(resp)
def setup(bot):
    bot.add_cog(General(bot))
