from imports import *
help_comds = {
    "flip" : "```css\nFlips a coin\nUsage: >flip ```",
    "math" : "```css\nDoes math for you\nUsage: >math <operation>",
    "servericon" : "```css\nGives server icon for you",
    "avatar" : "```css\nShows mentioned user's avatar\nUsage: >avatar```",
    "choice" : "```css\nSelectes random choice from user given choice\nUsage: >choice <choice1>,<choice2>...```"

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
                channel_id=f"<#{792750628023566337}>"
            embed=discord.Embed(title="Here is how you can get along with me :", description=f"**Contacting <@{702122543410184253}> for any kind of suggestions or a bug report would be appreciated**", color=0x73e600)
            embed.add_field(name="<:general:792348707004612618> General", value="`help` | `invite` | `math` |\n`avatar` | `servericon` | `youtube`\n `userinfo` | `serverinfo`", inline=False)
            embed.add_field(name="<:settings:792337130621894697> Admin ",   value="`kick` | `ban` | `clear` |\n `lock` | `unlock`", inline = False)
            embed.add_field(name="<:fun:792341688482922526> Fun ",     value="`flip` | `choice` | `dmuser` |\n`slot` | `meme`", inline=False)
            embed.add_field(name="<:music:792344750132690955> Music ",   value="`join` | `play` | `stop` |\n`move` | `nowplaying` | `queue` |\n`skip` | `forceskip` | `loop` |\n`pause` | `resume` | `remove`", inline=False)
            embed.add_field(name="<:chat:792342422163947544> Chat ",    value=f"`Chat with AIML powered Carolus in` {channel_id} ` if you're interested.\nIf such channel doesn't exist, request admin to create one` ", inline=False)
            embed.add_field(name="<:invitation:792796172199919616> I'd love to join new servers", value=f"**[Invite](https://discord.com/api/oauth2/authorize?client_id=774530270505205801&permissions=8&scope=bot)**", inline=False)
            embed.set_footer(text="You can always get my prefix just by pinging me ツ")
            embed.set_author(name=f'Requested by {str(ctx.author)[:-5]}', icon_url=ctx.author.avatar_url)
            await ctx.author.send(embed=embed)
            await ctx.message.add_reaction("<:dm:792337130932142090>")
            await ctx.send("ok")

        else:
            try:
                await ctx.send(help_comds[msg.split()[1]])
            except:
                await ctx.send(f"Command `{msg.split()[1]}` not found")

    
def setup(bot):
    bot.add_cog(Help(bot))