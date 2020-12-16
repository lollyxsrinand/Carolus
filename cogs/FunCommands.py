from imports import *

class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command()
    async def flip(self, ctx):
        # """ COIN FLIP SIMULATION """
        embed = discord.Embed(color=0x73e600)
        embed.set_author(name="Flipping coin...",icon_url="https://cdn.discordapp.com/attachments/778305851211382837/788457567973408798/tenor.gif")
        embed.add_field(name="__Result__",value=random.choice(["`Aha! It's Heads!`", "`Yay! It's Tales!`"]))
        await ctx.send(embed=embed)
        # await ctx.send(random.choice(["Aha! It's Heads!", "Yay! It's Tales!"]))

    @commands.command(aliases=["av","avt","pfp"])
    async def avatar(self, ctx, *, user: discord.Member = None):
        """ Get the avatar of you or someone else """
        user = user or ctx.author
        embed = discord.Embed(color=0x73e600)
        embed.set_author(name=f"Requested by {str(ctx.author)[0:-5]}", icon_url=ctx.author.avatar_url)
        embed.set_image(url=f"{user.avatar_url_as(size=1024)}")
        await ctx.send(embed=embed)
        
    @commands.command(aliases=["choose","random","rand"])
    async def choice(self, ctx, *, choice):
        choice = choice.split(',')
        random.shuffle(choice)
        await ctx.send(f"I choose -> `{choice[0]}`") 
        
    @commands.command(aliases=["serverico","servericon","sico","sicon"])
    async def server_icon(self, ctx):
        if len(str(ctx.guild.icon_url))>0:
            embed = discord.Embed(title="Server Icon",description="Looks nice!",color=0x73e600)
            embed.set_author(name=f"Requested by {str(ctx.author)[0:-5]}", icon_url=ctx.author.avatar_url)
            embed.set_image(url=f"{ctx.guild.icon_url}")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Oops! This server doesn't have any icon yet!")
    
        
def setup(bot):
    bot.add_cog(Fun(bot))