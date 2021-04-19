from discord.ext import commands
from discord import channel, utils
import discord
import asyncio
import random
from discord.ext.commands import bot

import discord
from discord.ext import commands
class fun(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball','8b','8B'])
    async def eiball(self,message):
        ba=["Ask Me If I Care","Dumb Question Ask Another", "Forget About It" , "In Your Dreams" , "Not A Chance" , "ofc"," yeasss","I'd say yes but you have to get me some crack B)","You may rely on it","Obviously" , "What Do You Think?" ,  "Who Cares?" , "You've Got To Be Kidding","Yeah Right"," You Wish","Absolutely", "Unclear Ask Later","Chances Aren't Good", "Ask <@261742964441612298> the Coolest Person here", "Indications Say Yes" , "No Doubt About It","The Stars Say No","You Can Count On It","Ask <@533696842613915658> the lozer"]
        
        content=discord.Embed(color=0x2f3136 , description ="<:mmLol:825380160765034507> {}".format(random.choice(ba)))
        msg = await message.send(embed=content)
        await msg.add_reaction("<:thisisfine:827079892797620274>")
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
        await ctx.channel.send(embed=embed)
      except:
        await ctx.channel.send("*Do you want me to snipe air?*")
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
        await ctx.channel.send(embed=embed)
      except:
        await ctx.channel.send("*Do you want me to snipe air?*",delete_after=10)
def setup(bot):
    bot.add_cog(fun(bot))
