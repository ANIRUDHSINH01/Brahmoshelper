import discord
from discord.ext import commands
from main import Brahmoshelper

class PingCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        latency = self.bot.latency * 1000
        embed = discord.Embed(title="Pong!", description=f"Latency: {latency:.2f}ms", color=discord.Color.green())
        await ctx.send(embed=embed)

async def setup(bot: Brahmoshelper):
    await bot.add_cog(PingCog(bot))



