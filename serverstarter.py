#!!! FIRST INSTALL PYTHON AND RUN pip install discord.py psutil !!!

import discord
from discord.ext import commands
import psutil
import subprocess
import os

# --- CONFIGURATION ---
TOKEN = 'YOUR_BOT_TOKEN'

# Change this variable to update your prefix
COMMAND_PREFIX = '!'

# ID of the channel where the command works
ALLOWED_CHANNEL_ID = 1234567890

# List of apps that, if running, will prevent the server from starting
FORBIDDEN_APPS = ["vrchat.exe","otherapp.exe"] 

# Absolute path to your startup file
MC_SERVER_PATH = "C:/Users/Server/start.bat" 

# Usually java.exe for Minecraft servers
MC_PROCESS_NAME = "java.exe"
# ---------------------

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

def is_app_running(app_names):
    """Checks the host process list for specific applications."""
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] in app_names:
                return True, proc.info['name']
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False, None

@bot.command()
async def start(ctx):
    if ctx.channel.id != ALLOWED_CHANNEL_ID:
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            print("Permission Error: Bot cannot delete messages in this channel.")
        return 
    mc_running, _ = is_app_running([MC_PROCESS_NAME])
    if mc_running:
        await ctx.send("⚠️ The Minecraft server is already running.")
        return
    app_running, app_name = is_app_running(FORBIDDEN_APPS)
    if app_running:
        await ctx.send(f"‼️ Cannot start server: Host is using **{app_name}** ")
        return
    try:
        await ctx.send(f"✅ Starting the Minecraft server... | Started by {ctx.author.mention}")
        subprocess.Popen(
            [MC_SERVER_PATH], 
            cwd=os.path.dirname(MC_SERVER_PATH), 
            shell=True
        )
    except Exception as e:
        await ctx.send(f"❌ System Error: Could not execute startup file. {e}")

@bot.event
async def on_ready():
    print(f'--- Bot is Online ---')
    print(f'Logged in as: {bot.user.name}')
    print(f'Listening in channel: {ALLOWED_CHANNEL_ID}')
    print(f'---------------------')

bot.run(TOKEN)
