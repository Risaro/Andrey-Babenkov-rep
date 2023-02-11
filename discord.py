import discord
from discord.ext import commands

config = {
    'token' : 'MTA3Mzg3MTc2MzcwNTk3MDgyOA.GmAx7D._zr5k7EAB54sIsETBRhxInR4YgbsF25x12db8I',
    'prefix': '!',
}
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

import random
@bot.command()
async def rand(ctx, *args):
    await ctx.reply(random.randint(0,100))


@bot.command()
async def info(ctx, *args):
    await ctx.reply(ctx.message)

@bot.command()
async.def getmember (ctx.member :str):
print ({i.name+ '#'+ i.disciminator for i in ctx.message.gild.members if member in i.name+"#+i.discriminator"})
@bot.event
async def  on_member_join(member)
    now = datetime.datetime.now
    embed = discord.Embed
    title='Приветсвуем на сервере "Бар 100 ренген"!'
    description=''
    color=0x0000FF
)
embed set.author(name=f'{member.name}{member.discriminator}',
        icon_url=member.avatar.url
embed.set_footer(text=f"Ваш ID: {member.id} ^ "
               f"-{now.hour}:{now.minute}")
await member.sens(embed=embed)
bot.run(config['token'])
