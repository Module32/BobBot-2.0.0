import discord, asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=["m!", "M!", "m! ", "M! "])
bot.remove_command('help')
TOKEN = "ODQ5NDQ3MDAyNDU0MzYwMDk0.YLbTKw.khPslYRMXDL-OOz-VuM_Yci5I2Q"

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        embed = discord.Embed(
            description=
            f"```css\n[ Permission Error ]\n```\nInvalid permissions",
            color=discord.Color.red())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="User: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.errors.CommandNotFound):
        embed = discord.Embed(
            description=
            f"```css\n[ 404 Command Error ]\n```\nCommand not found",
            color=discord.Color.red())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="User: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.errors.BadArgument):
        embed = discord.Embed(
            description=
            f"```css\n[ 404 General Error ]\n```\nCould not find that",
            color=discord.Color.red())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="User: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        arg = error.param.name
        embed = discord.Embed(
            description=
            f"```css\n[ Argument Error ]\n```\nMissing argument: `{arg}`",
            color=discord.Color.red())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="User: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

bot.run(TOKEN)