from imports import *
class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
                   
    @commands.command() 
    async def ping(self, ctx):
        embed = discord.Embed(color=0x73e600)
        embed.add_field(name="Here goes my ping: ",value=f"{round(self.bot.latency*1000)}ms")   
        await ctx.send(embed=embed)
    
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="Carolus invite", color=0x73e600)
        embed.add_field(name="I'd love to be invited to your server :D",value="**[Invite Carolus](https://discord.com/api/oauth2/authorize?client_id=774530270505205801&permissions=8&scope=bot)**")
        await ctx.send(embed=embed)
        
    @commands.command(aliases=['pmath','math','meth','m'])
    async def pymath(self, ctx, *, ope):
        resp = eval(ope)
        if resp > 10**1000:
            resp = "The output was too big to be calcluated"
        await ctx.send(resp)

    @commands.command(aliases=["av","avt","pfp"])
    async def avatar(self, ctx, *, user: discord.Member = None):
        """ Get the avatar of you or someone else """
        user = user or ctx.author
        embed = discord.Embed(color=0x73e600)
        embed.set_author(name=f"Requested by {str(ctx.author)[0:-5]}", icon_url=ctx.author.avatar_url)
        embed.set_image(url=f"{user.avatar_url_as(size=1024)}")
        await ctx.send(embed=embed)

    @commands.command(aliases=["serverico","servericon","sico","sicon"])
    async def server_icon(self, ctx):
        if len(str(ctx.guild.icon_url))>0:
            embed = discord.Embed(title="Server Icon",description="Looks nice!",color=0x73e600)
            embed.set_author(name=f"Requested by {str(ctx.author)[0:-5]}", icon_url=ctx.author.avatar_url)
            embed.set_image(url=f"{ctx.guild.icon_url}")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Oops! This server doesn't have any icon yet!")
        
    @commands.command(aliases=['yt','YT'])
    async def youtube(self, ctx, *, search):
        search = search.replace(' ','+')
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])

    @commands.command(aliases=["uinfo"])
    @commands.cooldown(3, 5, commands.BucketType.guild)
    async def userinfo(self, ctx, member : discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title=f"{member.name} Info",color=member.color)
        created_time = str(member.created_at).split(' ')
        embed.add_field(name=f"User ID",value=f"**{member.id}**",inline=True)
        embed.add_field(name=f"Mention",value=f"{member.mention}",inline=True)
        embed.add_field(name=f"Tag",value=f"{member.discriminator}",inline=True)
        embed.add_field(name=f"Prominent Role",value=f"{member.top_role.mention}",inline=True)
        embed.add_field(name=f"Member since",value=f"{created_time[0]}",inline=True)
        embed.add_field(name=f"Joined server on",value=f"{str(member.joined_at).split(' ')[0]}",inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("You are trying to use the command too many times.Retry after {:.0f}s".format(error.retry_after))

def setup(bot):
    bot.add_cog(General(bot))
