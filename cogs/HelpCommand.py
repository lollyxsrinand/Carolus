from imports import *

help_comds = {
    "flip" : "```css\nFlips a coin\nUsage: >flip ```",
    "avatar" : "```css\nShows mentioned user's avatar\nUsage: >av or >avatar```",
    "rand" : "```css\nSelectes random choice from user given choice\nUsage: >rand <choice1> <choice2>...```"
}

class Help(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command()
    async def help(self, ctx):
        msg = str(ctx.message.content)
        msg = msg.replace(msg[0],'')
        if msg == 'help':
            channel = discord.utils.get(ctx.guild.channels, name='carol-chat')
            if channel is not None:
                channel_id=str(channel.id)
                channel_id=f"<#{channel_id}>"
            if channel is None:
                channel_id='#carolus-chat'
            embed=discord.Embed(title="Here are my commands :", description="**You can always get my prefix by pinging me ツ**", color=0x73e600)
            embed.add_field(name="General", value="help | ping | kick |\nclear | prefix | pmath", inline=False)
            embed.add_field(name="Fun", value="flip | avatar | rand", inline=False)
            embed.add_field(name="Music", value="play | stop | move |\nnow | queue | skip |\nforceskip | pause | resume", inline=False)
            embed.add_field(name="Misc", value="google | youtube", inline = False)
            embed.add_field(name="Chat",value=f"`Chat with Carolus in` {channel_id} ` and have fun.\nIf such channel doesn't exist, request admin to create one` ")
            embed.set_footer(text="20 commands in total ツ")
            embed.set_author(name=f'Requested by {str(ctx.author)[:-5]}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        else:
            try:
                await ctx.send(help_comds[msg.split()[1]])
            except:
                await ctx.send(f"Command `{msg.split()[1]}` not found")

    
def setup(bot):
    bot.add_cog(Help(bot))