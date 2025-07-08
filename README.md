# Discord File Transfer Bot 🤖📂

This is a Python-based Discord bot designed to facilitate large file transfers by breaking them into smaller chunks and sending them via Discord channels. It also includes a command-line interface for easy interaction.

## Features ✨

* **Large File Uploads:** Upload files of virtually any size by splitting them into 10MB chunks. ⬆️📁
* **File Downloads:** Download files that were uploaded using the bot. ⬇️💾
* **Compression:** Files are compressed using LZMA before uploading to reduce transfer size. 📦💨
* **User-Friendly CLI:** An interactive command-line interface for choosing between upload and download operations. 🖥️💬
* **Progress Animation:** Visual feedback during file operations. 📊⏳

## Prerequisites 🛠️

Before you begin, ensure you have the following installed:

* Python 3.8+ 🐍
* `discord.py` library 🤖
* `pystyle` library 🎨
* `requests` library 🌐
* `lzma` (usually built-in with Python) 🗜️
* `tkinter` (usually built-in with Python for file dialogs) 🖼️

You can install the required Python libraries using pip:

```bash
pip install discord.py pystyle requests
````

## Setup ⚙️

1.  **Create a Discord Bot:** ➕🤖

      * Go to the [Discord Developer Portal](https://discord.com/developers/applications).
      * Click "New Application" and give your bot a name.
      * Navigate to the "Bot" tab, click "Add Bot", and confirm.
      * **Crucially, enable the "Message Content Intent" and "Guilds Intent" under the "Privileged Gateway Intents" section.** ✅
      * Copy your bot's token. 📋

2.  **Add the Bot to Your Server:** 🤝

      * Go to the "OAuth2" -\> "URL Generator" tab.
      * Select `bot` under "Scopes".
      * Under "Bot Permissions", select `Send Messages`, `Manage Channels`, and `Manage Messages` (for pinning).
      * Copy the generated URL and paste it into your browser to invite the bot to your server. 🔗

3.  **Configure `main.py`:** ✏️

      * Open `main.py`.
      * Replace `"YOUR_BOT_TOKEN_HERE"` with your actual Discord bot token:
        ```python
        bot.run("YOUR_BOT_TOKEN_HERE") # Replace with your token
        ```
      * Identify a Discord Guild (server) ID and a channel ID within that guild where the bot will create new channels for file transfers and send initial connection messages. Replace `LOG_CHANNEL_ID` and `GUILD_ID` with your actual IDs:
        ```python
        await bot.get_channel(LOG_CHANNEL_ID).send("connected new user!") # Your channel ID for connection messages
        # ...
        channel = await bot.get_guild(GUILD_ID).create_text_channel(name) # Your guild ID for creating channels
        ```

## Usage ▶️

To run the bot, simply execute `main.py`:

```bash
python main.py
```

The bot will connect to Discord, and you will be presented with a menu:

```
   __ _       _     _         _                           _                 _           
  / /(_) __ _| |__ | |_ _ __ (_)_ __   __ _   /\ /\ _ __ | | ___   __ _  __| | ___ _ __ 
 / / | |/ _` | '_ \| __| '_ \| | '_ \ / _` | / / \ | '_ \| |/ _ \ / _` |/ _ | '__|
/ /__| | (_| | | | | |_| | | | | | | | (_| | \ \_/ | |_) | | (_) | (_| | (_| |  __| |   
\____|_|\__, |_| |_|\__|_| |_|_|_| |_|\__, |  \___/| .__/|_|\___/ \__,_|\__,_|\___|_|   
        |___/                         |___/        |_|                                                                                           
Version 1.1                                                                                                                       
Made with bambi by dogo <3
Click ctrl+c to go back!
 |[1] Download
 |[2] Upload
Select option:
```

### Uploading a File 📤

1.  Select option `2` (Upload).
2.  A file dialog will open. Choose the file you wish to upload. 📂
3.  The bot will compress the file, split it into chunks, and upload each chunk to a newly created Discord text channel. ➡️ Discord
4.  Once complete, a link to a JSON file containing the URLs of all parts will be provided in the console. Share this link for others to download the file. 🔗

### Downloading a File 📥

1.  Select option `1` (Download).
2.  Enter the JSON link provided after an upload operation. ➡️
3.  The bot will download all parts, decompress them, and reconstruct the original file in the same directory where `main.py` is run. ⬇️💾

## Project Structure 🏗️

  * `main.py`: The main script that handles bot initialization, user interaction, file uploading, and downloading. 🚀
  * `logger.py`: Contains utility classes and functions for a custom menu, animation, and colored console output. 📝✨

## Important Notes ⚠️

  * **Bot Token Security:** Keep your bot token private. Do not share it publicly. 🔒
  * **Discord Rate Limits:** Be mindful of Discord's API rate limits. This bot attempts to handle large files by chunking, but excessive rapid operations might still trigger rate limits. ⏱️
  * **Channel Management:** The bot creates new channels for each upload. You may want to periodically clean up these channels. 🧹
  * **File Size:** While theoretically unlimited, extremely large files might take a significant amount of time to upload/download and consume considerable bandwidth. 🐢

## Todo List ✅

  * **Improve Memory Management:** Optimize memory usage, especially when handling very large files, to prevent excessive RAM consumption. 🧠💡
  * Add error handling for network issues during file transfers. 🚫🌐
  * Implement a more robust way to manage Discord channels created by the bot (e.g., automatic deletion after a certain time). 🗑️
  * Consider adding a progress bar within Discord itself for better user feedback. 📈
  * Explore options for resuming interrupted downloads. ↩️

## Contributing 🤝

Feel free to fork this repository, open issues, or submit pull requests to improve the bot.

## License 📄

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
