from imports import *
class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command() 
    async def ping(self, ctx):
        embed = discord.Embed(color=0x73e600)
        embed.add_field(name="Here goes my ping: ",value=f"{round(self.bot.latency*1000)}ms")   
        await ctx.send(embed=embed)
    
    @commands.command(help="I can't help you ")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member):
        await member.kick(reason="No reason Provided")
        await ctx.send(f"{ctx.author} has :boot: {member.mention}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member):
        await member.ban(reason="No reason Provided")
        await ctx.send(f":boot: {member.mention}")       
                
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx,*, lim):
        if int(lim)<=2000:
            await ctx.channel.purge(limit=int(lim))
        else:
            await ctx.send('Deleting messages of 2000+ are too much')
    
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="Carolus invite", color=0x73e600)
        embed.add_field(name="I'd love to be invited to your server :D",value="**[Invite Carolus](https://discord.com/api/oauth2/authorize?client_id=774530270505205801&permissions=8&scope=bot)**")
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
