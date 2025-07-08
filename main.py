import logger
import discord
import threading
import base64
import io, asyncio, json, requests, os 
import tkinter as tk
from tkinter.filedialog import askopenfilename
import lzma

tk.Tk().withdraw()

Main_menu = logger.Menu(["Download", "Upload"])
running = True

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
bot = discord.Client(intents=intents)
bot_ready_event = threading.Event()
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.get_channel(LOG_CHANNEL_ID).send("connected new user!")
    bot_ready_event.set()

def startBot():
    bot.run("YOUR_BOT_TOKEN_HERE")


def getName(name:str):
    name = name.split("/")
    return(name[len(name)-1])


anim = logger.Animation()
anim()
thread = threading.Thread(target=startBot,daemon=True)
thread.start()

bot_ready_event.wait()
anim.stop()
try:
    while running:
        logger.logo()
        match Main_menu():
            case 1:
                link = logger.dInput("Enter link: ")
                js = json.loads(requests.get(link).content)
                parts = js["parts"]
                name = js["filename"]
                concatenated_data = bytearray()
                with open(name, 'wb') as output_file:
                    for num, part in enumerate(parts):
                        anim.setDescription(f"Loading file part {num}")
                        anim()
                        req = requests.get(part)
                        anim.stop()
                        if req.status_code == 200:
                            concatenated_data.extend(req.content)
                            logger.dPrint("OK!", logger.dColor.SUCCESS)
                        else:
                            logger.dPrint(f"ERROR!! {req.status_code}", logger.dColor.WARNING)
                            break
                    output_file.write(lzma.decompress(concatenated_data))
                            

                logger.dPrint("DONE!", logger.dColor.DOGE)
                logger.dPrint(f"File saved as: {name}", logger.dColor.INFO)
                logger.dWait()
            case 2:
                async def sender(fileName):
                    name = getName(fileName)
                    logger.dPrint("Compressing..",logger.dColor.DOGE)
                    file1 = open(fileName, "rb")
                    file = lzma.compress(file1.read(), preset=9 | lzma.PRESET_EXTREME)
                    iofile = io.BytesIO(file)
                    file = io.BufferedReader(iofile)
                    
                    file1 = open(fileName, "rb")
                    
                    originalSize = len(file1.read())
                    compressedSize = len(file.read())
                    percentage_reduction = (originalSize - compressedSize) / originalSize
                    
                    logger.dPrint("compressed! ",logger.dColor.DOGE)
                    logger.dPrint(f"original size: {originalSize} ",logger.dColor.DOGE)
                    logger.dPrint(f"compressed size: {compressedSize}",logger.dColor.DOGE)
                    logger.dPrint(f"Percentage reduction:: {percentage_reduction}",logger.dColor.DOGE)
                    
                    iofile.seek(0)
                    file2 = io.BufferedReader(iofile)
                    
                    chunkNumber = 0
                    jsonObj = {
                                "parts": [],
                                "filename": name    
                            }
                    
                    channel = await bot.get_guild(GUILD_ID).create_text_channel(name)
                    while True:
                        chunkNumber+=1
                        anim.setDescription(f"Sending file part {chunkNumber}")
                        anim()
                        chunkD = file2.read(10 * 1024 * 1024)

                        if not chunkD:
                            anim.stop()
                            chunkNumber-=1
                            endjson = discord.File(io.BytesIO(json.dumps(jsonObj).encode()), filename=f"{name}.json")
                            messend = await bot.get_channel(channel.id).send(file=endjson)
                            await messend.pin()
                            linkjs = messend.attachments[0].url
                            logger.dPrint("DONE!",logger.dColor.DOGE)
                            logger.dPrint(f"     | link: {linkjs}",logger.dColor.INFO)
                            break
                            
                        chunk_file = discord.File(io.BytesIO(chunkD), filename=f"{name}.part{chunkNumber}")
                        mess = await bot.get_channel(channel.id).send(file=chunk_file)
                        jsonObj["parts"].append(mess.attachments[0].url)
                        anim.stop()
                asyncio.run_coroutine_threadsafe(sender(askopenfilename()), bot.loop).result()
                logger.dWait()

except KeyboardInterrupt:
    quit()