from imports import *

class Mod(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member):
        await member.kick(reason="No reason Provided")
        await ctx.send(f"{ctx.author.mention} has <a:slaughtered:789838738565627914> {member.mention}")
        
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f" <:huh:755278797774782637> Seems that you do not have permission to kick members in this server")
            
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member):
        await member.ban(reason="No reason Provided")
        await ctx.send(f"{ctx.author.mention} has banned {member.mention}")  
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f" <:huh:755278797774782637> Seems that you do not have permission to ban members in this server")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(3, 20, commands.BucketType.guild)
    async def clear(self, ctx,*, lim):
        if int(lim)<2000:
            await ctx.channel.purge(limit=int(lim)+1)
        else:   
            await ctx.send('Deleting messages of 2000+ are too much')

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f" <:huh:755278797774782637> Seems that you do not have permission to delete messages in this server")
            return
        await ctx.send("You need to wait 10 seconds after using this command. Please try after {:.0f}s".format(error.retry_after))
        
    @commands.command()
    async def host(self, ctx):
        user_id = ctx.author.id
        if user_id!=319120898869428227 and user_id!=702122543410184253:
            return
        hos = "Third Party Hosting Service"
        latency = round(self.bot.latency*1000)
        if latency > 50:    
            hos = "Local Host machine"
        embed = discord.Embed(color=0x73e600)
        embed.add_field(name="Hosted on: ",value=hos,inline=True)
        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(Mod(bot))   
