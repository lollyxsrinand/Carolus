from imports import *
import time
class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """ SHOWS USER IT'S PING , LOOK NEEDS TO BE UPDATED"""
    @commands.command() 
    async def ping(self, ctx):
        before = time.monotonic()
        temp = await ctx.send("Pong!")
        after = time.monotonic()
        embed = discord.Embed(color=0x73e600)
        embed.add_field(name="<:latency:792811383241572362> My Latency: ",value=f"```{int((after - before)*1000)}ms```", inline=True)   
        print("pong1")
        embed.add_field(name="<:latency:792811383241572362> Discord API Latency: ", value = f"```{round(self.bot.ws.latency*1000)}ms```", inline=True)
        print("pong2")
        await temp.edit(content="",embed=embed)

    """ SENDS AN INVITE LINK IN AN EMBED """
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="Hey! Thanks for thinking of inviting me!", color=0x73e600)
        embed.add_field(name=" <:invitation:792796172199919616> I'd love to be in your server",value="**[Click here to invite](https://discord.com/api/oauth2/authorize?client_id=774530270505205801&permissions=8&scope=bot)**")
        await ctx.send(embed=embed)
    
    """ DOES MATH CALCULATION USING PYMATH LIB """
    @commands.command(aliases=['pmath','math','meth','m'])
    async def pymath(self, ctx, *, ope):
        resp = eval(ope)
        if resp > 10**1000:
            resp = "The output was too big to be calcluated"
        await ctx.send(resp)

    """ DISPLAYES USER AVATAR IN AN EMBED, THERE ARE BUGS THO """
    @commands.command(aliases=["av","avt","pfp"])
    async def avatar(self, ctx, *, user: discord.Member = None):
        """ Get the avatar of you or someone else """
        user = user or ctx.author
        embed = discord.Embed(color=0x73e600)
        embed.set_author(name=f"Requested by {str(ctx.author)[0:-5]}", icon_url=ctx.author.avatar_url)
        embed.set_image(url=f"{user.avatar_url_as(size=1024)}")
        await ctx.send(embed=embed)

    """ SHOWS SERVER ICON """
    @commands.command(aliases=["serverico","servericon","sico","sicon"])
    async def server_icon(self, ctx):
        if len(str(ctx.guild.icon_url))>0:
            embed = discord.Embed(title="Server Icon",description="Looks nice!",color=0x73e600)
            embed.set_author(name=f"Requested by {str(ctx.author)[0:-5]}", icon_url=ctx.author.avatar_url)
            embed.set_image(url=f"{ctx.guild.icon_url}")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Oops! This server doesn't have any icon yet!")
    
    """ SENDS A YOUTUBE VIDEO LINK FOR A SEARCH """
    @commands.command(aliases=['yt','YT'])
    async def youtube(self, ctx, *, search):
        search = search.replace(' ','+')
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        await ctx.send(f"<:youtube:792297534852431892> https://www.youtube.com/watch?v={video_ids[0]}")

    """ SHOWS USERINFORMATION , NEEDS TO BE UPDATED A LITTLE """
    @commands.command(aliases=["uinfo"])
    @commands.cooldown(3, 5, commands.BucketType.guild)
    async def userinfo(self, ctx, member : discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title = f"<:info:792300331895095336> {member.name} ", color = 0x73e600)
        created_time = str(member.created_at).split(' ')
        embed.add_field(name = f"User ID",         value = f"**{member.id}**",                      inline = True)
        embed.add_field(name = f"Mention",         value = f"{member.mention}",                     inline = True)
        embed.add_field(name = f"Tag",             value = f"{member.discriminator}",               inline = True)
        embed.add_field(name = f"Prominent Role",  value = f"{member.top_role.mention}",            inline = True)
        embed.add_field(name = f"Member since",    value = f"{created_time[0]}",                    inline = True)
        embed.add_field(name = f"Joined server on",value = f"{str(member.joined_at).split(' ')[0]}",inline = False)
        embed.set_thumbnail(url = member.avatar_url)
        await ctx.send(embed = embed)

    """ HANDLING USERINFO COMMAND COOLDOWN ERROR """
    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("You are trying to use the command too many times.Retry after {:.0f}s".format(error.retry_after))

    @commands.command(aliases=["sifo"])
    @commands.cooldown(3, 5, commands.BucketType.guild)
    async def serverinfo(self, ctx):
        prem_subs = ctx.guild.premium_subscribers or "No server boosters"
        c = str(ctx.guild.created_at).split(' ')
        embed = discord.Embed(title = "Server Information <:info:792300331895095336>", color = 0x73e600)
        embed.add_field(name = "**Owner**",         value = f"<@{ctx.guild.owner_id}>",       inline = True)
        embed.add_field(name = "**Boosters**",      value = prem_subs,                        inline = True)
        embed.add_field(name = '**Member Count**',  value = f"{ctx.guild.member_count}",      inline = True)
        embed.add_field(name = "**Channel Count**", value = f"{len(ctx.guild.channels)}",     inline = True)
        embed.add_field(name = "**Highest Role**",value = f"<@&{ctx.guild.roles[-1].id}>",  inline = True)
        embed.add_field(name = "**Emoji Count**",   value = f"{len(ctx.guild.emojis)}",       inline = True)
        embed.add_field(name = "**Server ID**",     value = f"{ctx.guild.id}",                inline = True)
        embed.add_field(name = "**Creation **",     value = f"{c[1].split('.')[0]} on {c[0]}",inline = True)
        if ctx.guild.icon_url:
            embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        embed.set_author(name=f"Requested by - {ctx.author.name}",icon_url=f"{ctx.author.avatar_url}")
        await ctx.send(embed = embed)

    @serverinfo.error
    async def serverinfo_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Requesting for guild info too quickly.Try after {:.0f}s".format(error.retry_after))
        else:
            await ctx.send("There was an error processing server information...")

    
def setup(bot):
    bot.add_cog(General(bot))