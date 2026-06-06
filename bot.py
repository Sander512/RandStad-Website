import discord
from discord import app_commands
from discord.ext import commands
import webserver
import os
# --- CONFIGURATIE ---
discord_token = os.getenv("DISCORD_TOKEN")
X_ROLE_ID = 1437496640045977693 # VUL HIER JE ROL ID IN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def is_owner(interaction: discord.Interaction):
    return any(role.id == X_ROLE_ID for role in interaction.user.roles)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Forever RP Bot is online & volledig operationeel!")

# --- 👑 OWNER COMMANDS ---
@bot.tree.command(name="ban", description="Ban een gebruiker")
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = "Geen"):
    if not is_owner(interaction): return await interaction.response.send_message("Geen toegang!", ephemeral=True)
    await member.ban(reason=reason)
    await interaction.response.send_message(f"✅ {member.name} is verbannen.")

@bot.tree.command(name="kick", description="Kick een gebruiker")
async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = "Geen"):
    if not is_owner(interaction): return await interaction.response.send_message("Geen toegang!", ephemeral=True)
    await member.kick(reason=reason)
    await interaction.response.send_message(f"✅ {member.name} is gekicked.")

@bot.tree.command(name="clear", description="Wis aantal berichten")
async def clear(interaction: discord.Interaction, aantal: int):
    if not is_owner(interaction): return await interaction.response.send_message("Geen toegang!", ephemeral=True)
    await interaction.channel.purge(limit=aantal + 1)
    await interaction.response.send_message(f"✅ {aantal} berichten verwijderd.", ephemeral=True)

@bot.tree.command(name="announce", description="Doe een mededeling")
async def announce(interaction: discord.Interaction, bericht: str):
    if not is_owner(interaction): return await interaction.response.send_message("Geen toegang!", ephemeral=True)
    embed = discord.Embed(title="📢 Forever RP Mededeling", description=bericht, color=0xff0000)
    await interaction.channel.send(embed=embed)
    await interaction.response.send_message("Verstuurd!", ephemeral=True)

# --- 🏙️ BURGER COMMANDS ---
@bot.tree.command(name="tweet", description="Stuur een tweet naar de stad")
async def tweet(interaction: discord.Interaction, bericht: str):
    embed = discord.Embed(title="🐦 Twitter", description=f"@{interaction.user.name}: {bericht}", color=0x1da1f2)
    await interaction.channel.send(embed=embed)
    await interaction.response.send_message("Tweet geplaatst!", ephemeral=True)

@bot.tree.command(name="advertise", description="Plaats een advertentie")
async def advertise(interaction: discord.Interaction, bericht: str):
    embed = discord.Embed(title="📢 Advertentie", description=bericht, color=0xffff00)
    await interaction.channel.send(embed=embed)
    await interaction.response.send_message("Advertentie geplaatst!", ephemeral=True)

@bot.tree.command(name="gang-levels", description="Plaats het Gang Levels overzicht")
async def gang_levels(interaction: discord.Interaction):
    # Dit bericht behoudt wel de witregels omdat het geen embed is
    tekst = (
    "👑 **FOREVER ROLEPLAY: BUSINESS & FAMILY LEVELS** 👑\n\n"
    "**Level 1: Starter**\n• Eigen naam in Discord\n• 4 Leden toegang\n💰 €5,00 / 500 R$\n\n"
    "**Level 2: Lokale Ondernemer**\n• 5 Leden toegang\n• Eigen bedrijfsruimte zonder sloten\n💰 €7,50 / 750 R$\n\n"
    "**Level 3: Groeiende Business**\n• 6 Leden toegang\n• Bedrijfsruimte met sloten\n• Eigen opslagruimte\n💰 €12,50 / 1550 R$\n\n"
    "**Level 4: Bekende Naam**\n• 7 Leden toegang\n• Bedrijfsruimte met sloten\n• Eigen parkeerplaats/garage\n• Koffie- of snackleverancier\n💰 €15,00 / 1750 R$\n\n"
    "**Level 5: Luxe Onderneming**\n• 9 Leden toegang\n• Bedrijfsruimte met sloten & garage\n• Eigen reclame-rechten\n• VIP-service voor klanten\n💰 €25,00 / 2750 R$\n\n"
    "**Level 6: Stadsicoon**\n• 11 Leden toegang\n• Exclusief pand in de stad\n• Eigen evenementen-planner\n• Bedrijfs-voertuig voor leveringen\n💰 €30,00 / 3500 R$\n\n"
    "**Level 7: Imperium**\n• 13 Leden / Custom Bedrijfskleding\n• Luxe hoofdkantoor\n• Eigen handelslicentie\n💰 €45,00 / 5000 R$\n\n"
    "**Level 8: Zakenmagnaat**\n• 15 Leden / Eigen wagenpark\n• Toegang tot privé-vergaderruimtes\n• Bedrijf met 24/7 verkoop\n💰 €60,00 / 7500 R$\n\n"
    "**Level 9: Tycoon**\n• 18 Leden / VIP Bedrijfsmenu\n• Grootste pand in het centrum\n• Eigen vastgoedbeheer\n💰 €85,00 / 10.000 R$\n\n"
    "**Level 10: ELITE MOGUL**\n• Onbeperkt leden / Stads-eigendom\n• F6 Menu \n• 'God-tier' status in de economie\n1.000 R$"
    "**GANG,S ZIJN GRATIS ALLEN DAN BEGIN JE VAN 0 EN HEB JE MINDER KANS OM OFFICIELE TE WORDEN INGENOMEN TE KRIJGEN, MAAR JE KAN WEL EEN EIGEN GANG STARTEN EN DIE OPBOUWEN!**"
)
    await interaction.channel.send(tekst)
    await interaction.response.send_message("Gang Levels geplaatst!", ephemeral=True)

@bot.tree.command(name="profile", description="Bekijk je profiel")
async def profile(interaction: discord.Interaction):
    await interaction.response.send_message(f"👤 **{interaction.user.name}**, je bent een burger van Forever RP!")

@bot.tree.command(name="rob", description="Probeer iemand te beroven")
async def rob(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f"🎭 Je probeert {member.name} te beroven...")

webserver.keep_alive()
bot.run(DISCORD_TOKEN)