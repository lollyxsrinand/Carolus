from imports import *

class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command(aliases=['yt','YT'])
    async def youtube(self, ctx, *, search):
        search = search.replace(' ','+')
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])
        
    @commands.command(aliases=['G','g','gs','GS','Gsearch','gsearch','links'])
    async def google(self, ctx, *, entry):
        embed=discord.Embed(title='Google',description='**Search Results**', color = 0x73e600)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/774532878104920077/777873275111866439/Googles_G_but_better.png')
        cnt = 1
        for i in search(entry, tld='co.in', num=10, stop=10, pause=2):
            embed.add_field(name=f'{cnt}',value=f'{i}', inline=False)
            cnt+=1
        await ctx.send(embed=embed)  


def setup(bot):
    bot.add_cog(Misc(bot))