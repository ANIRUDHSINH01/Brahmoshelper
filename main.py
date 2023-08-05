import discord
import os
import asyncpg
from discord.ext import commands

exts = ["cogs.ping"]


class Brahmoshelper(commands.Bot):

  def __init__(self, command_prefix: str, intents: discord.Intents, **kwargs):
    super().__init__(command_prefix, intents=intents, **kwargs)

  async def setup_hook(self):
    try:
      for ext in exts:
        await self.load_extension(ext)
      await self.load_extension("jishaku")
      print("All cogs loaded")
    except Exception as e:
      print(f"Error loading cogs: {e}")

  async def on_ready(self):
    print(f"{self.user} is online")


if __name__ == "__main__":
  bot = Brahmoshelper(command_prefix="!", intents=discord.Intents.all())
  bot.run(os.getenv("TOKEN"))

