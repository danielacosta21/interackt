import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

NEW_ROLES = ["FST", "Circuiteer"]
OLD_ROLE = "Wanderer"

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Playing with Iskolotl🌻"))
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    added_roles = set(after.roles) - set(before.roles)
    for role in added_roles:
        if role.name in NEW_ROLES:
            old_role = discord.utils.get(after.guild.roles, name=OLD_ROLE)
            if old_role in after.roles:
                await after.remove_roles(old_role)
                print(f"Removed {OLD_ROLE} from {after.display_name} due to gaining {role.name}")
            break

bot.run(os.getenv("DISCORD_TOKEN"))