from imports import *

l = ['0','1','2','3','4','5','6','7','8','9'] 
class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command()
    async def flip(self, ctx):
        # """ COIN FLIP SIMULATION """
        
        await ctx.send(random.choice(["Aha! It's Heads!", "Yay! It's Tales!"]))

    @commands.command(aliases=["av","avt","pfp"])
    async def avatar(self, ctx, *, user: discord.Member = None):
        """ Get the avatar of you or someone else """
        user = user or ctx.author
        embed = discord.Embed(color=0x73e600)
        embed.set_author(name=f"Requested by {str(ctx.author)[0:-5]}", icon_url=ctx.author.avatar_url)
        embed.set_image(url=f"{user.avatar_url_as(size=1024)}")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def rand(self, ctx, *, choice):
        choice = choice.split(' ')
        random.shuffle(choice)
        await ctx.send(choice[0]) 
    
        
def setup(bot):
    bot.add_cog(Fun(bot))