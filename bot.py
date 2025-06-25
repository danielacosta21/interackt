import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Replace these with actual role NAMES or use role IDs instead
NEW_ROLES = ["FST", "Circuiteer"]     # Roles that trigger the old role removal
OLD_ROLE = "Wanderer"               # Role to remove when new role is added

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    # Roles added = in 'after' but not in 'before'
    added_roles = set(after.roles) - set(before.roles)

    for role in added_roles:
        if role.name in NEW_ROLES:
            old_role = discord.utils.get(after.guild.roles, name=OLD_ROLE)
            if old_role in after.roles:
                await after.remove_roles(old_role)
                print(f"Removed {OLD_ROLE} from {after.display_name} due to gaining {role.name}")
            break  # Only need to process once

# Run your bot with your token
bot.run(os.getenv("MTM4NzQ0MTg0NzA1MTIyMzA5MA.Gvi9sq.Ss50PwWH395GwYPJhpQt4AmOW5HC2UIQ83CezY"))