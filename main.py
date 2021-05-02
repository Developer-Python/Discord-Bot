import discord
from discord.ext import commands
from config import settings
from discord import Member
client = discord.Client()
bot = commands.Bot(command_prefix = settings['prefix'])

# role
print('[BOT] - ON')

@bot.command()
async def addrole(ctx, role: discord.Role, author: discord.Member=None):
    try:
        if ctx.channel.id == 835171568916234280:
            author = ctx.author
            await author.add_roles(role)
    except:
        print('У бота не достаточно прав для выдачи этой роли, или этой роли не существует!')

bot.run(settings['token'])
