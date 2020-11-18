from imports import *

l = ['0','1','2','3','4','5','6','7','8','9']
class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command()
    async def flip(self, ctx):
        await ctx.send(random.choice(["Aha! It's Heads!", "Yay! It's Tales!"]))
    
    @commands.command(aliases=['av','pfp'])
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        embed = discord.Embed(color=0x73e600)
        embed.set_author(name=f'Requested by {str(ctx.author)[0:-5]}',icon_url=(ctx.author.avatar_url))
        embed.set_image(url=str(userAvatarUrl))
        print(userAvatarUrl)
        await ctx.send(embed=embed)
    @commands.command()
    async def rand(self, ctx):
        random.shuffle(l)
        s = ''
        for x in l[:4]:
            s += str(x)
        await ctx.send(s) 
def setup(bot):
    bot.add_cog(Fun(bot))