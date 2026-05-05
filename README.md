# Minecraft Server Starter Bot

A simple, lightweight Discord bot written in Python (`discord.py`) that allows authorized users to start a Minecraft server directly from a Discord channel. 

The bot includes safety checks to ensure the server isn't started if it's already running, or if specific resource-heavy applications (like VR games) are currently running on the host machine.

## ✨ Features
- **Remote Startup:** Start your Minecraft server via a simple Discord command (`!start`).
- **Channel Restriction:** The bot only listens to commands in a designated channel.
- **Process Checking:** Prevents starting the server if it's already running or if blacklisted apps are active.
- **Cleanup:** Automatically deletes unauthorized command attempts (requires Manage Messages permission).

## 📋 Prerequisites
Before you begin, ensure you have met the following requirements:
* **Python 3.8 or higher** installed on the host machine.
* A Discord Developer Application with a Bot Token.
* **Privileged Gateway Intents:** The **Message Content Intent** MUST be enabled in your Discord Developer Portal.

## 🚀 Installation

1. **Clone the repository** (or download the script):
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install required dependencies:**
   The bot requires `discord.py` and `psutil`. Install them using pip:
   ```bash
   pip install discord.py psutil
   ```

3. **Invite the bot to your server:**
   * Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   * Create an application and get your bot token.
   * Under `OAuth2` -> `URL Generator`, select the `bot` scope.
   * Select the following permissions: `Send Messages`, `Read Message History`, and `Manage Messages`.
   * Use the generated URL to invite the bot to your server.

## ⚙️ Configuration

Open the Python script and locate the `# --- CONFIGURATION ---` block. Update the variables to match your environment:

```python
# --- CONFIGURATION ---
TOKEN = 'YOUR_BOT_TOKEN' # Replace with your actual bot token

COMMAND_PREFIX = '!' # The prefix used to trigger the bot

ALLOWED_CHANNEL_ID = 1234567890 # ID of the channel where the command is allowed

FORBIDDEN_APPS = ["vrchat.exe", "otherapp.exe"] # Apps that block the server from starting

MC_SERVER_PATH = "C:/Users/Server/start.bat" # Absolute path to your startup file (use forward slashes)

MC_PROCESS_NAME = "java.exe" # Usually java.exe for Java servers, or bedrock_server.exe for Bedrock
# ---------------------
```

### Finding your Channel ID
1. Open Discord Settings > Advanced > Enable **Developer Mode**.
2. Right-click the channel you want the bot to listen to.
3. Click **Copy Channel ID** and paste it into the `ALLOWED_CHANNEL_ID` variable (without quotes).

## 💻 Usage

To start the bot, open your terminal or command prompt, navigate to the directory containing your script, and run:

```bash
python bot.py
```
*(Note: You may need to use `python3` or `py` depending on your OS and installation).*

Once running, type `!start` in your designated Discord channel to launch the server!

## ⚠️ Important Notes
* **File Paths:** If you are on Windows, make sure to use forward slashes (`/`) or double backslashes (`\\`) in your `MC_SERVER_PATH`.
* **The `.bat` File:** Ensure your Minecraft `start.bat` file works flawlessly when double-clicked manually before trying to use the bot. Adding `pause` to the end of your `.bat` file during testing can help catch errors.
* **Keep Alive:** The terminal window running the Python script must remain open for the bot to stay online. Consider setting it up as a background service if you want it to run 24/7.
```
