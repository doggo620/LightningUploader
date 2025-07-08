import threading
from pystyle import Colorate, Colors
import time
import os
from enum import Enum
from typing import Union

logoString = """
   __ _       _     _         _                           _                 _           
  / /(_) __ _| |__ | |_ _ __ (_)_ __   __ _   /\ /\ _ __ | | ___   __ _  __| | ___ _ __ 
 / / | |/ _` | '_ \| __| '_ \| | '_ \ / _` | / / \ | '_ \| |/ _ \ / _` |/ _` |/ _ | '__|
/ /__| | (_| | | | | |_| | | | | | | | (_| | \ \_/ | |_) | | (_) | (_| | (_| |  __| |   
\____|_|\__, |_| |_|\__|_| |_|_|_| |_|\__, |  \___/| .__/|_|\___/ \__,_|\__,_|\___|_|   
        |___/                         |___/        |_|                                                                                           
Version 1.1                                                                                                                       
"""

class Menu:
    def __init__(self, options: list = []):
        self.options = options
    def addOption(self, option:str):
        self.options.append(option)
    def __call__(self):
        i = 0
        for option in self.options:
            i += 1
            print(Colorate.Horizontal(Colors.blue_to_purple, f" |[{i}] {option}"))
        try:
            return int(input(Colorate.Horizontal(Colors.blue_to_cyan, "Select option: ")))
        except Exception:
            return 0

class Animation:
    def __init__(self, desc="Loading"):
        self.desc = desc
        self.running = False
    def setDescription(self, desc: str):
        self.desc = desc
    def stop(self):
        self.running = False
        self.thread.join()
        print(Colorate.Horizontal(Colors.blue_to_purple, f"{self.desc}...OK"))
    def threadFunction(self):
        animation = "|/-\\"
        self.running = True
        while self.running:
            for anim in animation:
                print(Colorate.Horizontal(Colors.blue_to_red, f"{self.desc}...{anim}"), end="\r")
                time.sleep(0.1)
    def __call__(self):
        self.thread = threading.Thread(target=self.threadFunction, daemon=True)
        self.thread.start()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def logo():
    clear()
    print(Colorate.Horizontal(Colors.red_to_purple, logoString))
    print(Colorate.Horizontal(Colors.red_to_blue, "Made with bambi by dogo <3"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "Click ctrl+c to go back!"))

class dColor(Enum):
    INFO = Colors.red_to_yellow
    WARNING = Colors.red_to_white
    DEBUG = Colors.blue_to_purple
    SUCCESS = Colors.green_to_white
    DOGE = Colors.red_to_blue
    
def dPrint(String:str, color: Union[Colors, dColor], flush: bool = False):
    if color.__class__ == dColor: color = color.value
    print(Colorate.Horizontal(color, String), flush=flush)
def dWait():
    input(Colorate.Horizontal(Colors.red_to_yellow, "Click enter to continue!"))
def dInput(String:str):
    return input(Colorate.Horizontal(Colors.blue_to_cyan, String))