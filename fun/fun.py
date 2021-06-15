import discord
from discord.ext import commands
from discord import channel, utils
import discord
import asyncio
import random
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext.commands.core import command
class fun(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot
        
    @commands.command(aliases=['8ball','8b','8B'])
    async def eiball(self,message):
        ba=["Ask Me If I Care","Dumb Question Ask Another", "Forget About It" , "In Your Dreams" , "Not A Chance" , "ofc"," yeasss","I'd say yes but you have to get me some crack B)","You may rely on it","Obviously" , "What Do You Think?" ,  "Who Cares?" , "You've Got To Be Kidding","Yeah Right"," You Wish","Absolutely", "Unclear Ask Later","Chances Aren't Good", "Ask <@261742964441612298> the Coolest Person here", "Indications Say Yes" , "No Doubt About It","The Stars Say No","You Can Count On It","Ask <@533696842613915658> the lozer"]
        
        content=discord.Embed(color=0x2f3136 , description ="<:mmLol:825380160765034507> {}".format(random.choice(ba)))
        msg = await message.reply(embed=content,mention_author=False)
        
    bot.sniped_messages = {}
    @commands.Cog.listener()
    async def on_message_delete(self,message):
      if message.author.id != 813313220739334185: 
        bot.sniped_messages[message.channel.id]=(message.content,message.author,message.channel.name,message.created_at)
        await asyncio.sleep(40)
        bot.sniped_messages[message.channel.id]=None
    @commands.command()
    async def snipe(self,ctx):
      try:
        contents,author,channel_name,time=bot.sniped_messages[ctx.channel.id]
        embed=discord.Embed(description=contents,color=0x2f3136,timestamp=time)
        embed.set_author(name=f'{author.name}#{author.discriminator}',icon_url=author.avatar_url)
        embed.set_footer(text=f'Deleted in: #{channel_name}')
        await ctx.reply(embed=embed,mention_author=False)
      except:
        await ctx.reply("*Do you want me to snipe air?*")
    bot.esniped_messages = {}
    @commands.Cog.listener()
    async def on_message_edit(self,before,after):
      if after.author.id != 813313220739334185: 
        bot.esniped_messages[before.channel.id]=(before.content,before.author,before.channel.name,before.created_at)
        await asyncio.sleep(40)
        bot.esniped_messages[before.channel.id]=None

    @commands.command(aliases=['esnipe'])
    async def editsnipe(self,ctx):
      try:
        contents,author,channel_name,time=bot.esniped_messages[ctx.channel.id]
        embed=discord.Embed(description=contents,color=0x2f3136,timestamp=time)
        embed.set_author(name=f'{author.name}#{author.discriminator}',icon_url=author.avatar_url)
        embed.set_footer(text=f'Edited: #{channel_name}')
        await ctx.reply(embed=embed,mention_author=False)
        
      except:
        await ctx.reply("*Do you want me to snipe air?*",delete_after=10)
    @commands.command(aliases=['gayrate','gayr8'])
    
    async def howgay(self,ctx, member: discord.Member=None):
      x=random.randint(1,100)
      if member is None:
        member=ctx.message.author.name
       
      
      
        
        await ctx.reply(f'<a:homo:835055067337588746> **{member}** is **{x}**% Gay',mention_author=False)
      else:

       
      
      
        
        await ctx.reply(f'<a:homo:835055067337588746> **{member.name}** is **{x}**% Gay',mention_author=False) 
    @commands.command()
    async def pp(self,ctx, member: discord.Member=None):
      x=random.randint(1,20)
      y="8"
      d="D"
      c=y+"="*x+d
      if member is None:
        member=ctx.message.author.name
        if x <=10:
          z=(f''' Your PP Size..
          is **{c}** ''')
          em=discord.Embed(title=" Peepee Sizer - <:smolpp:835052959955157032>",description=f'{z}',color=0x2f3136)
          await ctx.reply(embed=em,mention_author=False)
          
        else:
          z=(f''' Your PP Size..
          **{c}**  ''')
          em=discord.Embed(title=" Peepee Sizer - <:bigpp:835053066994712597>",description=f'{z}',color=0x2f3136)
          await ctx.reply(embed=em,mention_author=False)
          
          
      else:
        if x<=10:
          z=(f''' {member.name}'s PP Size..
          **{c}** ''')
          em=discord.Embed(title="Peepee Sizer - <:smolpp:835052959955157032>",description=f'{z}',color=0x2f3136)
          await ctx.reply(embed=em,mention_author=False)
          

        else:
          
          z=(f'''{member.name}'s Your PP Size..
          **{c}** ''')
          em=discord.Embed(title="Peepee Sizer - <:bigpp:835053066994712597>",description=f'{z}',color=0x2f3136)
          await ctx.reply(embed=em,mention_author=False)
          

    @commands.command(aliases=['hornyrate'])
    async def howhorny(self,ctx, member: discord.Member=None):
      x=random.randint(1,100)
      if member is None:
        member=ctx.message.author.name
        
      
      
        
        await ctx.reply(f'**You** are **{x}**% horny',mention_author=False)
      else:

        
      
      
        
        await ctx.reply(f'**{member.name}** is **{x}**% horny',mention_author=False)
    @commands.command(aliases=['simprate'])
    async def howsimp(self,ctx, member: discord.Member=None):
      x=random.randint(1,100)
      if member is None:
        member=ctx.message.author.name
        
      
      
        
        await ctx.reply(f'**You** are **{x}**% Simpy',mention_author=False)
      else:

       
      
      
        
        await ctx.reply(f'**{member.name}** is **{x}**% Simpy',mention_author=False) 

def setup(bot):
    bot.add_cog(fun(bot))
