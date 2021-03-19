from imports import *

class Mod(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    """ KICKS A USER FROM SERVER, IF YOU MENTION YOURSELF YOU GET KICKED BY YOURSELF TOO """
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
        await ctx.send(f"{ctx.author.mention} has <:kick:818413879138582568> {member.mention} | Reason - {reason}")

    """ HANDLING KICK ERROR ON SOMEONE TRYING TO KICK WITHOUT PERMISSIONS """
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f" <:huh:755278797774782637> Seems that you do not have permission to kick members in this server")

    """ BANS A SPECIFIED USER FROM THE SERVER """  
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        print("UvU i won't ban do anything :lmao:")
        await ctx.send(f"{ctx.author.mention} has banned {member.mention} | Reason : {reason}")  
    
    """ HANDLING BAN ERROR ON SOMEONE TRYING TO BAN WITHOUT PERMISSIONS """
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f" <:huh:755278797774782637> Seems that you do not have permission to ban members in this server")

    """ CLEARS SPECIFIED AMOUNT OF MESSAGES """
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(5, 15, commands.BucketType.guild)
    async def clear(self, ctx, lim : int = None):
        if not lim:
            await ctx.send("You must specify the amount of messages to delete!")
            return
        if int(lim)<=2000:
            await ctx.channel.purge(limit=int(lim)+1)
        else:   
            await ctx.send('Deleting messages of 2000+ are too much')

    """ HANDLING CLEAR ERROR ON SOMEONE TRYING TO CLEAR MESSAGES TOO QUICKLY """
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f" <:huh:755278797774782637> Seems that you do not have permission to delete messages in this server")
            return
        await ctx.send("You need to wait 10 seconds after using this command. Please try after {:.0f}s".format(error.retry_after))
        
    """ SHOWS WHERE THE BOT IS HOSTED WITH REFERENCE TO PING """
    """ THIS COMMAND WORKS ONLY WITH ME AND AVXNSEAR, MY FRIEND """
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

    """ LOCKS SPECIFIED CHANNEL, IF NO CHANNEL IS SPECIFIED IT LOOKS THE CHANNEL IN WHICH IT WAS REQUESTED """
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel : discord.TextChannel = None):
        channel = channel or ctx.channel    
        if not channel.overwrites_for(ctx.guild.default_role).send_messages:
            await ctx.send("Already locked channel")
            return  
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send("Successfully locked the channel")
    
    """ HANDLING LOCK ERROR ON SOMEONE TRYING TO LOCK A CHANNEL WITHOUT PERMISSIONS """
    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:huh:755278797774782637> You don't have permissions to manage channels")
    
    """ UNLOCKS A SPECIFIED CHANNEL, IF NO CHANNEL IS SPECIFIED IT UNLOCKES THE CHANNEL IT WAS REQUESTED """
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel : discord.TextChannel = None):
        channel = channel or ctx.channel
        if channel.overwrites_for(ctx.guild.default_role).send_messages:
            await ctx.send("Channel is not locked")
            return
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send("Successfully unlocked channel")

    """ HANDLING UNLOCK ERROR ON SOMEONE TRYING TO UNLOCK A CHANNEL WITHOUT PERMISSIONS """
    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:huh:755278797774782637> You don't have permissions to manage channels")


def setup(bot):
    bot.add_cog(Mod(bot))   
