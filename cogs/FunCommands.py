from imports import *
import praw
class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.reddit = praw.Reddit(client_id="lKo1xzYpmcsSQQ",client_secret="2-DiQ19hPTLdKlNaLhSvn-kqjNb9gw",user_agent="app:'lKo1xzYpmcsSQQ':1.0")

    @commands.command()
    async def flip(self, ctx):
        embed = discord.Embed(color=0x73e600)
        embed.set_author(name="Flipping coin...",icon_url="https://media.tenor.com/images/c177244eceeba20065334b8c58584719/tenor.gif")
        embed.add_field(name="__Result__",value=random.choice(["`Aha! It's Heads!`", "`Yay! It's Tales!`"]))
        await ctx.send(embed=embed)
        
    @commands.command(aliases=["choose"])
    async def choice(self, ctx, *, choice):
        choice = choice.split(',')
        random.shuffle(choice)
        await ctx.send(f"I choose -> `{choice[0]}`") 
            
    @commands.command(aliases=["dm","dmu","pm"])
    async def dmuser(self, ctx, user: discord.User, *, message):
        await ctx.channel.purge(limit=1)
        await ctx.send("Sent DM to specified user :D", delete_after=3)
        await user.send(message)

    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def slot(self, ctx):
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")

    @slot.error
    async def slot_error(self, ctx, error):
        await ctx.send("You need to wait 5 seconds after using this command.Try after {:.0f}s".format(error.retry_after))

    @commands.command()
    @commands.cooldown(2,5,commands.BucketType.guild)
    async def meme(self, ctx):
        async with ctx.typing():
            sub=random.choice(['memes','dankmemes','ProgrammingHumor','gamingmemes','AdviceAnimals',"MemeEconomy","terriblefacebookmemes"])
            pos = random.randint(0,50)
            counter=0
            for submission in self.reddit.subreddit(sub).hot(limit=50):
                counter+=1
                if counter==pos:
                    title = submission.title
                    pic = submission.url
                    # if pic[-3::]!='.jpg' or pic[-3::]!='.gif':
                    if pic[-1]=='/':
                        continue
                    break
        embed=discord.Embed(title=title,color=0x8a0101)
        embed.set_image(url=pic)
        embed.set_author(name=f"Requested by {ctx.author.name}" , icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    
    @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('Aking for memes too quickly. Try again after 5 seconds')
        else:
            embed=discord.Embed(title="No meme for you today ;-;",color=0x73e600)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))