           ###########################################
          #                                         #  # 
         #                        Made             #    #  
        #                        By               #      #  
       #      TELIUM     Jonah Crawford          #        #  
      #                      and                #          #  
     #                Jack Richardson          #            #
    #                                         #              #
   ###########################################     13/6/22    #
    #                                         #              #
     #            Idea                         #            # 
      #              By                         #          #  
       #         Craig Sargent      TELIUM       #        #  
        #              and                        #      #  
         #          David Hillyard                 #    #  
          #                                         #  #  
           ########################################### 

#https://github.com/Jonahc0014/TELIUM

print("\033[1;37;50m")

import random
import os
import sys
import time
import curses
import locale
import curses
import craw
from datetime import datetime
from getkey import getkey, keys
import socket
import statistics
from replit import audio
import psutil
import platform
from replit import db

global null
null = ""
global coins
coins = 0
global passcode
passcode = os.environ['passcode']
total_coins = 0
speed = 0.1
mod1 = []
commands = ("(l)OCK", "(q)UEEN", "(w)ORKERS", "(v)ENTS")
answer_y = ("yes", "Yes", "Y", "y", "YES")
answer_n = ("no", "No", "N", "n", "NO")
answer_e = ("ok", "OK", "Ok", "E", "e", "Enter", "enter", "ENTER")
global options, admin, rains
options = {
    "Speed of text" : speed,
    "Difficulty" : "M",
    "Admin mode" : False ,
    "Rainbow mode" : False,
    "Cut Scenes" : True,
    "Beta mode" : False
}
rains = False
admin = False
speed = options["Speed of text"]
global wins
global worker_destroy
global played
global wins
global loss
played = 0
wins = 0
loss = 0
worker_destroy = 0
global modules_ls
modules_ls = []
num_modules = 18
module = 1
last_module = 0
possible_moves = []
alive = True
won = False
global power
power = 150
global fuel
fuel = 500
locked = 0
queen = 0
vent_shafts = []
info_panels = []
workers = []
shop_items = {
  "More fuel": [150, 225, 340, 500, "Sold out"],
  "More power": [200, 300, 450, 675, "Sold out"],
  "More coins": [500, 750, 1125, 1700, "Sold out"],
  "Less queen moves": [1000, 2000, "Sold out"],
  "Admin powers": [10000, "Sold out"]
}
shop_buys = {
  "More fuel": 0,
  "More power": 0,
  "More coins": 0,
  "Less queen moves": 0,
  "Admin powers": 0
}
#global skip
#skip = False
global exit
answer_e = ("Exit", "exit", "EXIT", "E", "e")
global speed_2
speed_2 = 0.1
enter_shop = False

def sleep(s):
  time.sleep(s)
  return null

def clear():
  command = "clear"
  if os.name in ("nt", "dos"):
    command = "cls"
  os.system(command)
  return null

def d_print(text): 
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(speed)

def setup():
  clear()
  db["global_stats"] = {
    "base" : {
      "Games Played": 0,
      "Games Won": 0,
      "Games Lost": 0,
      "Percentage Won": "0%",
      "Percentage Lost": "0%",
      "Destroyed Workers": 0,
      "Favorite Module": "none",
      "Total Coins": 0,
      "Coins Spent": total_coins
    }
  }
  return null

def colour_box(char):
  colour = ["\033[1;31;50m", "\033[1;33;50m", "\033[1;32;50m", "\033[1;36;50m", "\033[1;34;50m", "\033[1;35;50m", "\033[1;37;50m"]
  for i in range(0, len(colour)):
    for j in range(0, len(colour)):
      print(str(colour[j]) + str(char), end=" ")
    temp = colour[0]
    colour.remove(temp)
    colour.append(temp)
    print("")
  return null

def song(list):
  for i in list:
    audio.play_tone(list[1],list[0], 1)
  return null
  
clear()
colour_box("█")
print("\033[1;37;50m")
print("e2 86 91 e2 86 91 e2 86 93 e2 86 93 e2 86 90 e2 86 92 20 e2 86 90 e2 86 92 41 42")
print("press any letter")

key = getkey()
if key == "u":
  key = getkey()
  if key == "u":
    key = getkey()
    if key == "d":
      key = getkey()
      if key == "d":
        key = getkey()
        if key == "l":
          key = getkey()
          if key == "r":
            key = getkey()
            if key == "l":
              key = getkey()
              if key == "r":
                key = getkey()
                if key == "a":
                  key = getkey()
                  if key == "b":
                    clear()
                    print("Passcode?")
                    code = input()
                    if code == passcode:
                      setup()
                      d_print("global varibles reset")
                      sleep(5)
else:
  clear()

song([[1, 420], [0.5, 750], [2, 300], [0.5, 1000], [1, 500]])

#source = audio.play_file('TELIUM_4.mp3', 1, True, -1)
#volume = 1
#loops = 0
#print('type "up" or "down" to change volume')
#print('press enter to play/pause')
##source.set_loop(10)
#while True:
#	print(f'volume is at {source.volume * 100}%')
#	cmd = input('> ').lower()
#	if cmd == 'up':
#		source.volume += .25
#		volume += .25
#	elif cmd == 'down':
#		source.volume -= .25
#		volume -= .25
#	else:
#		source.paused = not source.paused
#time.sleep(10000)

#comp_name = socket.gethostname()
#print(comp_name)
#time.sleep(5)

#https://replit.com/talk/ask/Python-How-do-I-input-without-pressing-enter/33815

#https://www.thepythoncode.com/article/get-hardware-system-information-python#System_Information

#yes = 1
#buffer = "ye"
#while yes == 1:
#  key = getkey()
#  if key == keys.UP:
#    print("UP")
#  elif key == keys.DOWN:
#    print("DOWN")
#  elif key == 'a':
#    print("A")
#  elif key == 'Y':
#    print("Y")
#  else:
#    # Handle other text characters
#    buffer += key
#    print(buffer)
#    yes = 2

craw.get_time()

locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()
stdscr = curses.initscr()
curses.endwin()
      
#tty.setcbreak(sys.stdin)
#while 1 == 1:
#  print(ord(sys.stdin.read(1)))


d_print("\033[1;37;50m")
clear()

def rain(text):
  if options["Rainbow mode"] == True:
    rainbow(text)
    print("\033[1;37;50m")
  else:
    d_print(text)
  return null

def rainbow(text):
  for c in text:
    colour = random.randint(1, 7)
    print("\033[1;3" + str(colour) + ";50m", str(c), end="")
    sleep(options["Speed of text"])
  return null

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def animation(type):
  if options["Cut Scenes"] == True:
  # or skip == True:
    print("\033[1;37;50m")
    clear()
    if type == 1:
      print("                                                         ______")
      print("     _______                                            |______|")
      print("    <   ____)                  _______                  |______|")
      print(" /--|  |(  o|                 |┌-----┐|\                |______|")
      print("|   >   \___|                 ||     || \               |______|")
      print("|  /---------+                ||     ||_\|              |______|")
      print("| |    \     |_________ ____∩_       ||  |              |______|")
      print("|  \    \    |         | #014 |      ||  |              |______|")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |______|")
      print("|   |\    \  |                     \  |  |              |______|")
      print(" \__==\    \==                      \ |  |              |______|")
      print("    |  \   \> \                      \|  |              |______|")   
      print("    |   UUUU   \                      |  |              |______|")
      print("    |   |   \   \                    /    \             |______|")
      print("    |   |   /   /                   /      \            |______|")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(0.5)
      clear()
      print("                                                         ______")
      print("     _______                                            |______|")
      print("    <   ____)                  _______                  |______|")
      print(" /--|  |(  o|                 |┌-----┐|\                |______|")
      print("|   >   \___|                 ||     || \               |______|")
      print("|  /---------+                ||     ||_\|              |______|")
      print("| |    \     |_________ ____∩_       ||  |              |______|")
      print("|  \    \    |         | #014 |    \033[1;31;50m--\033[1;37;50m||  |              |______|")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |______|")
      print("|   |\    \  |                     \  |  |              |______|")
      print(" \__==\    \==                      \ |  |              |______|")
      print("    |  \   \> \                      \|  |              |______|")   
      print("    |   UUUU   \                      |  |              |______|")
      print("    |   |   \   \                    /    \             |______|")
      print("    |   |   /   /                   /      \            |______|")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(0.5)
      clear()
      print("                                                         ______")
      print("     _______                                            |______|")
      print("    <   ____)                  _______                  |______|")
      print(" /--|  |(  o|                 |┌-----┐|\                |______|")
      print("|   >   \___|                 ||     || \               |______|")
      print("|  /---------+                ||     ||_\|              |______|")
      print("| |    \     |_________ ____∩_       ||  |              |______|")
      print("|  \    \    |         | #014 |  \033[1;31;50m----\033[1;37;50m||  |              |______|")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |______|")
      print("|   |\    \  |                     \  |  |              |______|")
      print(" \__==\    \==                      \ |  |              |______|")
      print("    |  \   \> \                      \|  |              |______|")   
      print("    |   UUUU   \                      |  |              |______|")
      print("    |   |   \   \                    /    \             |______|")
      print("    |   |   /   /                   /      \            |______|")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(0.5)
      clear()
      print("                                                         ______")
      print("     _______                                            |______|")
      print("    <   ____)                  _______                  |______|")
      print(" /--|  |(  o|                 |┌-----┐|\                |______|")
      print("|   >   \___|                 ||     || \               |______|")
      print("|  /---------+                ||     ||_\|              |______|")
      print("| |    \     |_________ ____∩_       ||  |              |______|")
      print("|  \    \    |         | #014 |\033[1;31;50m------\033[1;37;50m||  |              |______|")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |______|")
      print("|   |\    \  |                     \  |  |              |______|")
      print(" \__==\    \==                      \ |  |              |______|")
      print("    |  \   \> \                      \|  |              |______|")   
      print("    |   UUUU   \                      |  |              |______|")
      print("    |   |   \   \                    /    \             |______|")
      print("    |   |   /   /                   /      \            |______|")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(2)
      clear()
      print("                                                         ______")
      print("     _______                                            |______|")
      print("    <   ____)                  _______                  |______|")
      print(" /--|  |(  o|                 |┌-----┐|\                |______|")
      print("|   >   \___|                 ||     || \               |______|")
      print("|  /---------+                ||     ||_\|              |______|")
      print("| |    \     |_________ ____∩_       ||  |              |______|")
      print("|  \    \    |         | #014 |      ||  |              |______|")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |______|")
      print("|   |\    \  |                     \  |  |              |______|")
      print(" \__==\    \==                      \ |  |              |______|")
      print("    |  \   \> \                      \|  |              |______|")   
      print("    |   UUUU   \                      |  |              |______|")
      print("    |   |   \   \                    /    \             |______|")
      print("    |   |   /   /                   /      \            |______|")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(2)
      clear()
      print("                                                         ______")
      print("     _______                                            |      |")
      print("    <   ____)                  _______                  |      |")
      print(" /--|  |(  o|                 |┌-----┐|\                |______|")
      print("|   >   \___|                 ||     || \               |______|")
      print("|  /---------+                ||     ||_\|              |______|")
      print("| |    \     |_________ ____∩_       ||  |              |______|")
      print("|  \    \    |         | #014 |      ||  |              |______|")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |______|")
      print("|   |\    \  |                     \  |  |              |______|")
      print(" \__==\    \==                      \ |  |              |______|")
      print("    |  \   \> \                      \|  |              |______|")   
      print("    |   UUUU   \                      |  |              |______|")
      print("    |   |   \   \                    /    \             |______|")
      print("    |   |   /   /                   /      \            |______|")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(0.25)
      clear()
      print("                                                         ______")
      print("     _______                                            |      |")
      print("    <   ____)                  _______                  |      |")
      print(" /--|  |(  o|                 |┌-----┐|\                |      |")
      print("|   >   \___|                 ||     || \               |      |")
      print("|  /---------+                ||     ||_\|              |______|")
      print("| |    \     |_________ ____∩_       ||  |              |______|")
      print("|  \    \    |         | #014 |      ||  |              |______|")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |______|")
      print("|   |\    \  |                     \  |  |              |______|")
      print(" \__==\    \==                      \ |  |              |______|")
      print("    |  \   \> \                      \|  |              |______|")   
      print("    |   UUUU   \                      |  |              |______|")
      print("    |   |   \   \                    /    \             |______|")
      print("    |   |   /   /                   /      \            |______|")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(0.25)
      clear()
      print("                                                         ______")
      print("     _______                                            |      |")
      print("    <   ____)                  _______                  |      |")
      print(" /--|  |(  o|                 |┌-----┐|\                |      |")
      print("|   >   \___|                 ||     || \               |      |")
      print("|  /---------+                ||     ||_\|              |      |")
      print("| |    \     |_________ ____∩_       ||  |              |      |")
      print("|  \    \    |         | #014 |      ||  |              |______|")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |______|")
      print("|   |\    \  |                     \  |  |              |______|")
      print(" \__==\    \==                      \ |  |              |______|")
      print("    |  \   \> \                      \|  |              |______|")   
      print("    |   UUUU   \                      |  |              |______|")
      print("    |   |   \   \                    /    \             |______|")
      print("    |   |   /   /                   /      \            |______|")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(0.25)
      clear()
      print("                                                         ______")
      print("     _______                                            |      |")
      print("    <   ____)                  _______                  |      |")
      print(" /--|  |(  o|                 |┌-----┐|\                |      |")
      print("|   >   \___|                 ||     || \               |      |")
      print("|  /---------+                ||     ||_\|              |      |")
      print("| |    \     |_________ ____∩_       ||  |              |      |")
      print("|  \    \    |         | #014 |      ||  |              |      |")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |      |")
      print("|   |\    \  |                     \  |  |              |______|")
      print(" \__==\    \==                      \ |  |              |______|")
      print("    |  \   \> \                      \|  |              |______|")   
      print("    |   UUUU   \                      |  |              |______|")
      print("    |   |   \   \                    /    \             |______|")
      print("    |   |   /   /                   /      \            |______|")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(0.25)
      clear()
      print("                                                         ______")
      print("     _______                                            |      |")
      print("    <   ____)                  _______                  |      |")
      print(" /--|  |(  o|                 |┌-----┐|\                |      |")
      print("|   >   \___|                 ||     || \               |      |")
      print("|  /---------+                ||     ||_\|              |      |")
      print("| |    \     |_________ ____∩_       ||  |              |      |")
      print("|  \    \    |         | #014 |      ||  |              |      |")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |      |")
      print("|   |\    \  |                     \  |  |              |      |")
      print(" \__==\    \==                      \ |  |              |      |")
      print("    |  \   \> \                      \|  |              |______|")   
      print("    |   UUUU   \                      |  |              |______|")
      print("    |   |   \   \                    /    \             |______|")
      print("    |   |   /   /                   /      \            |______|")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(0.25)
      clear()
      print("                                                         ______")
      print("     _______                                            |      |")
      print("    <   ____)                  _______                  |      |")
      print(" /--|  |(  o|                 |┌-----┐|\                |      |")
      print("|   >   \___|                 ||     || \               |      |")
      print("|  /---------+                ||     ||_\|              |      |")
      print("| |    \     |_________ ____∩_       ||  |              |      |")
      print("|  \    \    |         | #014 |      ||  |              |      |")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |      |")
      print("|   |\    \  |                     \  |  |              |      |")
      print(" \__==\    \==                      \ |  |              |      |")
      print("    |  \   \> \                      \|  |              |      |")   
      print("    |   UUUU   \                      |  |              |      |")
      print("    |   |   \   \                    /    \             |______|")
      print("    |   |   /   /                   /      \            |______|")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(0.25)
      clear()
      print("                                                         ______")
      print("     _______                                            |      |")
      print("    <   ____)                  _______                  |      |")
      print(" /--|  |(  o|                 |┌-----┐|\                |      |")
      print("|   >   \___|                 ||     || \               |      |")
      print("|  /---------+                ||     ||_\|              |      |")
      print("| |    \     |_________ ____∩_       ||  |              |      |")
      print("|  \    \    |         | #014 |      ||  |              |      |")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |      |")
      print("|   |\    \  |                     \  |  |              |      |")
      print(" \__==\    \==                      \ |  |              |      |")
      print("    |  \   \> \                      \|  |              |      |")   
      print("    |   UUUU   \                      |  |              |      |")
      print("    |   |   \   \                    /    \             |      |")
      print("    |   |   /   /                   /      \            |      |")
      print("    |   |  /   /                   /        \           |______|")
      print("    |   |_<   /                   /Scanner 99\          |______|")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(0.25)
      clear()
      print("                                                         ______")
      print("     _______                                            |      |")
      print("    <   ____)                  _______                  |      |")
      print(" /--|  |(  o|                 |┌-----┐|\                |      |")
      print("|   >   \___|                 ||     || \               |      |")
      print("|  /---------+                ||     ||_\|              |      |")
      print("| |    \     |_________ ____∩_       ||  |              |      |")
      print("|  \    \    |         | #014 |      ||  |              |      |")
      print("|   \    \   |--------- ‾UUUU‾ ______||  |              |      |")
      print("|   |\    \  |                     \  |  |              |      |")
      print(" \__==\    \==                      \ |  |              |      |")
      print("    |  \   \> \                      \|  |              |      |")   
      print("    |   UUUU   \                      |  |              |      |")
      print("    |   |   \   \                    /    \             |      |")
      print("    |   |   /   /                   /      \            |      |")
      print("    |   |  /   /                   /        \           |      |")
      print("    |   |_<   /                   /Scanner 99\          |      |")
      print("   _<_____ \__\__                /____________\=========|______|")
      print("")
      sleep(3)
      clear()
    elif type == 2:
      space = " "
      movement = 29
      for dist in range(0, movement): 
        print(space * dist, "                _,--._ ")
        print(space * dist, "              ,'      `. ")
        print(space * dist, "      |\     / ,-.  ,-. \     /| ")
        print(space * dist, "      )o),/ ( ( ~ )( ~ ) ) \.(o( ")
        print(space * dist, "     /o/// /|  `-'  `-'  |\  \\o\ ")
        print(space * dist, "    / / |\ \(   .    ,   )/ /| \ \ ")
        print(space * dist, "    | | \o`-/    `\/'    \-'o/ | | ")
        print(space * dist, "    \ \  `,'              `.'  / / ")
        print(space * dist, " \.  \ `-'  ,'|   /\   |`.  `-' /  ,/ ")
        print(space * dist, "  \`. `.__,' /   /  \   \ `.__,' ,'/ ")
        print(space * dist, "   \o\     ,'  ,'    `.  `.     /o/ ")
        print(space * dist, "    \o`---'  ,'        `.  `---'o/ ")
        print(space * dist, "      `.____,'            `.____,' ")
        print("")
        print("")
        print(space * (movement - dist), "     _______ ")
        print(space * (movement - dist), "    <   ____) ")
        print(space * (movement - dist), " /--|  |(  o| ")
        print(space * (movement - dist), "|   >   \___| ")
        print(space * (movement - dist), "|  /---------+ ")
        print(space * (movement - dist), "| |    \ =========______/|")
        print(space * (movement - dist), "|  \    \=========------\|")
        print(space * (movement - dist), "|   \   \----+--\-))) ")    
        print(space * (movement - dist), "|   |\______|_)))/ ")       
        print(space * (movement - dist), " \__========== ")    
        print(space * (movement - dist), "    |   |-\   \  ")        
        print(space * (movement - dist), "    |   |  \   \   ")       
        print(space * (movement - dist), "    |   |   \   \    ")    
        print(space * (movement - dist), "    |   |   /   /  ")       
        print(space * (movement - dist), "    |   |  /   /  ") 
        print(space * (movement - dist), "    |   |_<   /  ") 
        print(space * (movement - dist), "   _<_____ \__\__ ")
        sleep(0.075)
        clear()
      dist = 30
      print(space * dist, "                _,--._ ")
      print(space * dist, "              ,'      `. ")
      print(space * dist, "      |\     / ,-.  ,-. \     /| ")
      print(space * dist, "      )o),/ ( ( ~ )( ~ ) ) \.(o( ")
      print(space * dist, "     /o/// /|  `-'  `-'  |\  \\o\ ")
      print(space * dist, "    / / |\ \(   .    ,   )/ /| \ \ ")
      print(space * dist, "    | | \o`-/    `\/'    \-'o/ | | ")
      print(space * dist, "    \ \  `,'              `.'  / / ")
      print(space * dist, " \.  \ `-'  ,'|   /\   |`.  `-' /  ,/ ")
      print(space * dist, "  \`. `.__,' /   /  \   \ `.__,' ,'/ ")
      print(space * dist, "   \o\     ,'  ,'    `.  `.     /o/ ")
      print(space * dist, "    \o`---'  ,'        `.  `---'o/ ")
      print(space * dist, "      `.____,'            `.____,' ")
      print("")
      print("")
      movement = 30
      print(space * (movement - dist), "     _______ ")
      print(space * (movement - dist), "    <   ____) ")
      print(space * (movement - dist), " /--|  |(  o| ")
      print(space * (movement - dist), "|   >   \___| ")
      print(space * (movement - dist), "|  /---------+ ")
      print(space * (movement - dist), "| |    \ =========______/|")
      print(space * (movement - dist), "|  \    \=========------\|")
      print(space * (movement - dist), "|   \   \----+--\-))) ")    
      print(space * (movement - dist), "|   |\______|_)))/ ")       
      print(space * (movement - dist), " \__========== ")    
      print(space * (movement - dist), "    |   |-\   \  ")        
      print(space * (movement - dist), "    |   |  \   \   ")       
      print(space * (movement - dist), "    |   |   \   \    ")    
      print(space * (movement - dist), "    |   |   /   /  ")       
      print(space * (movement - dist), "    |   |  /   /  ") 
      print(space * (movement - dist), "    |   |_<   /  ") 
      print(space * (movement - dist), "   _<_____ \__\__ ")
      sleep(2.5)
      clear()
      print("\033[1;37;50m                                       (  )   _,--._     ( )...\033[1;37;50m")
      print("\033[1;37;50m                                 (  )       ,'      `.    )\033[1;37;50m")
      print("\033[1;37;50m                            .(  )   |\     / ,-.  ,-. \     /| (   )..\033[1;37;50m")
      print("\033[1;37;50m                           .(  ) \033[1;31;50m@\033[1;37;50m  )o),/ ( ( @ )( @ ) ) \.(o( (     )  .   .\033[1;37;50m")
      print("\033[1;37;50m                           .(  )   /o/// /|  `-'  `-'  |\  \\o\ (   )\033[1;37;50m")
      print("\033[1;37;50m                          . (  )\033[1;31;50m@\033[1;37;50m / / |\ \(     ___    )/ /| \ \ ( \033[1;31;50m@\033[1;37;50m )\033[1;37;50m")
      print("\033[1;37;50m                          (    )  | | \o`-/    |   |    \-'o/ | |    (\033[1;31;50m@\033[1;37;50m )..\033[1;37;50m")
      print("\033[1;37;50m                     . .(  )   \033[1;31;50m@\033[1;37;50m  \ \  `,'      ‾‾‾     `.'  / / (   ) .   . .\033[1;37;50m")
      print("\033[1;37;50m                          (     \.\033[1;31;50m@\033[1;37;50m \ `-'  ,'|\033[1;31;50m@\033[1;37;50m  /\   |`.  `-' /  ,/ (   )\033[1;37;50m")
      print("\033[1;37;50m                      ..  )    \033[1;31;50m@\033[1;37;50m\`. `.__,'\033[1;31;50m@\033[1;37;50m/   /  \   \ `.__,' ,'/\033[1;31;50m@\033[1;37;50m(  )\033[1;37;50m")
      print("\033[1;37;50m                        .  (  )\033[1;31;50m@@\033[1;37;50m\o\ \033[1;31;50m@@\033[1;37;50m  ,'  ,' \033[1;31;50m@@\033[1;37;50m `.  `. \033[1;31;50m@@\033[1;37;50m  /o/\033[1;31;50m@\033[1;37;50m(  )\033[1;37;50m")
      print("\033[1;37;50m                              \033[1;31;50m@@@@\033[1;37;50m\o`---'  ,' \033[1;31;50m@@@@@\033[1;37;50m `.  `---'o/\033[1;31;50m@@@@@\033[1;37;50m\033[1;37;50m")
      print("\033[1;37;50m                               \033[1;31;50m@@@@@\033[1;37;50m`.____,'\033[1;31;50m@@@@@@@@@\033[1;37;50m`.____,'\033[1;31;50m@@@@@@@@\033[1;37;50m(  )\033[1;37;50m")
      print("\033[1;37;50m                          (   \033[1;31;50m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\033[1;37;50m")
      print("\033[1;37;50m                               \033[1;31;50m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\033[1;37;50m")
      print("\033[1;37;50m     _______                .  \033[1;31;50m@@@@@@@@@@@@@@@@@@@@@@@@@\033[1;37;50m")
      print("\033[1;37;50m    <   ____)                 \033[1;31;50m@@@@@@@@@@@@@@@@@@@@@@\033[1;37;50m     ) .\033[1;37;50m")
      print("\033[1;37;50m /--|  |(  o|            (   \033[1;31;50m@@@@@@@@@@@@@@@@@@@@@\033[1;37;50m")
      print("\033[1;37;50m|   >   \___|           )   \033[1;31;50m@@@@@@@@@@@@@@@@@@@@\033[1;37;50m")
      print("\033[1;37;50m|  /---------+          (  \033[1;31;50m@@@@@@@@@@@@@@@@@@@@\033[1;37;50m")
      print("\033[1;37;50m| |    \ =========______/|\033[1;31;50m@@@@@@@@@@@@@@@@\033[1;37;50m")
      print("\033[1;37;50m|  \    \=========------\|\033[1;31;50m@@@@@@@@\033[1;37;50m")
      print("\033[1;37;50m|   \   \----+--\-))) \033[1;37;50m")    
      print("\033[1;37;50m|   |\______|_)))/ \033[1;37;50m")       
      print("\033[1;37;50m \__========== \033[1;37;50m")    
      print("\033[1;37;50m    |   |-\   \  \033[1;37;50m")        
      print("\033[1;37;50m    |   |  \   \   \033[1;37;50m")       
      print("\033[1;37;50m    |   |   \   \    \033[1;37;50m")    
      print("\033[1;37;50m    |   |   /   /  \033[1;37;50m")       
      print("\033[1;37;50m    |   |  /   /  \033[1;37;50m") 
      print("\033[1;37;50m    |   |_<   /  \033[1;37;50m") 
      print("\033[1;37;50m   _<_____ \__\__ \033[1;37;50m")
      sleep(5)
    elif type == 3:
      print("┌-------------------------------------------┐")
      print("|┌-----------------------------------------┐|")
      for i in range(0, 7):
        print("||                                         ||")
      print("|L_________________________________________⅃|")
      print("L___________________________________________⅃")
      sleep(0.5)
      clear()
      print("┌-------------------------------------------┐")
      print("|┌-----------------------------------------┐|")
      print("||                                         ||")
      print("||                 SCANNER                 ||")
      print("||                                         ||")
      print("||                COMMANDS:                ||")
      print("||                                         ||")
      print("||        \033[1;31;50mLOCK\033[1;37;50m, \033[1;32;50mQUEEN\033[1;37;50m, \033[1;34;50mWORKERS\033[1;37;50m, \033[1;36;50mVENTS      \033[1;37;50m||")
      print("||                                         ||")
      print("|L_________________________________________⅃|")
      print("L___________________________________________⅃") 
      print("")
    elif type == 4:
      clear()
      print("'TELIUM' proudly running on...")
      sleep(2)
      print("\033[1;34;50m")
      sleep(speed_2)
      print("    __  ____    ____  __    __ ")
      sleep(speed_2)
      print("   /  ]|    \  /    T|  T__T  T")
      sleep(speed_2)
      print("  /  / |  D  )Y  o  ||  |  |  |")
      sleep(speed_2)
      print(" /  /  |    / |     ||  |  |  |")
      sleep(speed_2)
      print("/   \_ |    \ |  _  |l  `  '  !")
      sleep(speed_2)
      print("\     ||  .  Y|  |  | \      / ")
      sleep(speed_2)
      print(" \____jl__j\_jl__j__j  \_/\_/  ")
      sleep(speed_2)
      print("                               ")
      sleep(speed_2)
      print("                          ___    _____")
      sleep(speed_2)
      print("                         /   \  / ___/")
      sleep(speed_2)
      print("                        Y     Y(   \_ ")
      sleep(speed_2)
      print("                        |  O  | \__  T")
      sleep(speed_2)
      print("                        |     | /  \ |")
      sleep(speed_2)
      print("                        l     ! \    |")
      sleep(speed_2)
      print("                         \___/   \___j")
      sleep(speed_2)
      print("\033[1;37;50m")
    else:
      print("\033[1;31;50mERROR ANIMATION NOT FOUND")
      sleep(5)
    return null
  else:
    return null
  return null

#animation(1)
#animation(2)
#animation(3)
#animation(4)

animation(4)
sleep(3)
while 1 == 1:  
  rain("Press 'i' to view info or press 's' to start")
  print("")
  info = getkey()
  if info == "i":
    print("=" * 40, "System Information", "=" * 40)
    global uname
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    # Boot Time
    print("=" * 40, "Boot Time", "=" * 40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
    #CPU information
    print("=" * 40, "CPU Info", "=" * 40)
    #cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
      print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")
    # Memory Information
    print("=" * 40, "Memory Information", "=" * 40)
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("=" * 20, "SWAP", "=" * 20)
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")
    # Disk Information
    print("=" * 40, "Disk Information", "=" * 40)
    print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"====== Device: {partition.device} ======")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that isn't ready
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")
    # Network information
    print("=" * 40, "Network Information", "=" * 40)
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
    print("")
    print("To exit, type exit")
    exit = input("> ")
    if exit in answer_e:
      break
    else:
      continue
  else:
    break

def load(waited, type):
  clear()
  percent = 0
  waited = waited / 2
  wait = 0
  for i in range(0, 100):
    tone = random.randint(0, 3)
    if int(tone) == 2:
      audio.play_tone(0.1, 300 + (3 * i), 1)
    waiting = random.randint(0, 1)
    wait = waited + waiting
    print ("""\033[1;37;50mLoading...\n
    [""", percent, "%]\n")
    if type == 1:
      print("\033[1;36;50m♪┏(・o･)┛♪")
    else:
      print("\033[1;36;50m♪ᕕ( ᐛ )ᕗ♪")
    sleep(wait / 100)
    percent = percent + 1
    if percent == 99:
      sleep(0.5)
    clear()
    if percent == 100:
      break
    waiting = random.randint(0, 25)
    wait = waited + waiting
    print ("""\033[1;37;50mLoading...\n
    [""", percent, "%]\n")
    if type == 1:
      print("\033[1;35;50m♪┗ (･o･ ) ┓♪")
    else:
      print("\033[1;35;50m♪ᕕ( ᐕ )ᕗ♪")
    sleep(wait / 100)
    #percent = percent + 1
    if percent == 99:
      sleep(0.5)
    clear()
    if percent == 100:
      break
  print("\033[1;37;50m")
  clear()
  return null

while 1 == 1:
  clear()
  d_print("\033[1;37;50mPlease Fully Expand Your Console")
  print("")
  sleep(2)
  d_print("Done?")
  print("")
  answer = getkey()
  if answer in answer_y:
    break
  #elif answer == "s":
  #  skip = True
  #  break

#Procedure declarations

def check_vent_shafts():
  global num_modules, module, vent_shafts, fuel
  if module in vent_shafts:
    rain("There is a bank of fuel cells here")
    print("")
    rain("You load one into your flamethrower")
    print("")
    if options["Difficulty"] == "E":
      fuel_gained = 75
    if options["Difficulty"] == "M":
      fuel_gained = 50
    if options["Difficulty"] == "H":
      fuel_gained = 25
    print("Fuel was", fuel, "now reading", fuel + fuel_gained)
    fuel = fuel + fuel_gained
    sleep(2)
    rain("The doors suddenly lock shut")
    print("")
    rain("What is happening to the station?")
    print("")
    rain("Our only escape is to climb into the ventiltaion shaft")
    sleep(4)
    print("")
    rain("We have no idea where we are going")
    sleep(4)
    print("")
    rain("We follow the passages and find ourselfs sliding down")
    sleep(3)
    load(0.1, random.randint(1, 2))
    last_module = module
    while module == last_module or module in vent_shafts:
      module = random.randint(1, num_modules)
    load_module()
    check_vent_shafts()

def load_module():
  global module, possible_moves
  possible_moves = get_modules_from(module)
  output_module()
  return null

def lock():
  global num_modules, power, locked
  new_lock = int(input("Enter module to lock: "))
  check4menu(new_lock)
  if new_lock <= 0 or new_lock > num_modules:
    rain("Invalid Module. Operation Failed.")
  elif new_lock == queen:
    rain("Unable To Lock Module Due To Lifeform Present. Operation Failed.")
  else:
    locked = new_lock
    print("Module", locked, "Is Now Locked")
  if options["Difficulty"] == "M":
    power_used = 25 + 5 * random.randint(0, 5)
  elif options["Difficulty"] == "H":
    power_used = 15 + 5 * random.randint(0, 3)
  power = power - power_used
  print("Used", power_used, "power, you now have", power, "power left")
  sleep(2)
  check4death()
  return power

def get_modules_from(module):
  moves = []
  text_file = open("Charles_Darwin/module" + str(module) + ".txt", "r")
  for counter in range(0, 4):
    move_read = text_file.readline()
    move_read = int(move_read.strip())
    if move_read != 0:
      moves.append(move_read)
  return moves

def output_module():
  global module
  clear()
  print("You are in module", str(module))
  return module

def worker_aliens():
  global module, workers, fuel, alive
  global worker_destroy, null
  #Output alien encountered
  if module in workers:
    rain("Startled, a small alien scuttles across the floor.")
    print("")
    rain("It turns and leaps towards us")
    print("")
    #Get the player's action
    successful_attack = False
    while successful_attack == False:
      rain("You can:")
      print("")
      rain("- Short blast your flamethrower to frighten it away")
      print("")
      rain("- Medium blast your flamethrower to try to kill it")
      print("")
      rain("- Long blast your flamethrower to definetly kill it")
      print("")
      rain("How will you react? ((s)MALL,(m)EDIUM, (l)ARGE)")
      action_2 = null
      sleep(2)
      while action_2 not in ("S", "M", "L", "s", "m", "l"):
        action_2 = input("Press the trigger: ")
        check4menu(action_2)
      if action_2 in ("S", "s"):
        fuel_used = random.randint(5, 25)
        dead = random.randint(0, 5)
      elif action_2 in ("L", "l"):
        fuel_used = random.randint(45, 65)
        dead = random.randint(0, 3)
      else:
        fuel_used = random.randint(25, 45)
        dead = 1
        fuel = fuel - fuel_used
      #check if player has ran out of fuel
      check4death()
      if fuel <= 0:
        alive = False
        return null
      #work out how much fuel is needed
      if dead == 1:
        rain("The Alien has been destroyed")
        worker_destroy += 1
        #remove the worker from the module
        workers.remove(module)
        successful_attack = True
      else:
        rain("The alien scuttles away into the corner of the room, but it is not dead")
      #successful action
      print("")
  return null

def get_action(): 
  global module, last_module, possible_moves, power
  valid_action = False
  while valid_action == False:
    print("What do you want to do? (m)OVE (s)CANNER)")
    print("")
    choice = input()
    checked = check4menu(choice)
    if checked == True:
      output_moves()
    if choice in ("m", "M"):
      move = int(input("Enter the module to move to: "))
      check4menu(move)
      if move in possible_moves or admin == True:
        valid_action = True
        last_module = module
        module = move
        modules_ls.append(module)
        animation(1)
        if options["Difficulty"] == "H":
          power_lost = random.randint(1, 5)
          power =- power_lost
          print("Power was", power + power_lost + ",", "now reading", power)
          sleep(2)
      else:
        rain("The module must be connected to the current module.")
        sleep(3)
    elif choice in ("s", "S"):
      animation(3)
      rain("Scanner Ready. Enter Command")
      print("")
      command = input("> ")
      check4menu(command)
      if command in ("LOCK", "Lock", "lock", "L", "l"):
        power = lock()
        return null
      elif command in ("Queen", "QUEEN", "Q", "q", "queen"):
        print("The Queen Alien is in module", queen)
        if options["Difficulty"] == "M":
          power_used = 15 + 5 * random.randint(0, 3)
        elif options["Difficulty"] == "H":
          power_used = 25 + 5 * random.randint(0, 5)
        check4death()        
      if command in ("Workers", "WORKERS", "W", "w", "workers"):
        print("The workers are in module(s)", workers)
        if options["Difficulty"] == "M":
          power_used = 15 + 5 * random.randint(0, 3)
        elif options["Difficulty"] == "H":
          power_used = 25 + 5 * random.randint(0, 5)
        check4death()
      if command in ("Vents", "VENTS", "V", "v", "vents"):
        print("The vents are in modules", vent_shafts)
        if options["Difficulty"] == "M":
          power_used = 15 + 5 * random.randint(0, 3)
        elif options["Difficulty"] == "H":
          power_used = 25 + 5 * random.randint(0, 5)
        check4death()
      check4death()
      print("You had", power, "power but now you have", power - power_used, "power")
      power = power - power_used
      check4death()

def output_moves():
  global possible_moves, options
  check_vent_shafts()
  print("")
  if options["Beta mode"] == True:
    modone = possible_moves[0]
    modtwo = possible_moves[1]
    try:
      modthree = possible_moves[2]
    except:
      modthree = "0"
    try:
      modfour = possible_moves[3]
    except:
      modfour = "0"
    if int(modone) < 10:
      modone = "0" + str(modone)
    if int(modtwo) < 10:
      modtwo = "0" + str(modtwo)
    if int(modthree) < 10:
      modthree = "0" + str(modthree)
    if int(modfour) < 10:
      modfour = "0" + str(modfour)
    if len(possible_moves) == 4 and module not in queen and module not in vent_shafts and module not in info_panels and module not in workers:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                  =======                 \\\         | |")
      print("   | |        //                  /   ", modthree ,"  \                 \\\        | |")
      print("   | |       //  =======         ∠=========⦣       =======   \\\       | |")
      print("   | |      //  /  ", modtwo ,"   \                         /   ", modfour ,"  \   \\\      | |")
      print("   | |     //  ∠=========⦣                       ∠=========⦣   \\\     | |")
      print("   | |    //                                                    \\\    | |")
      print("   | |   //                                                      \\\   | |")
      print("   | |  //                         =======                        \\\  | |")
      print("   | | //                         /  ", modone ,"   \                        \\\ | |")
      print("   | |//                         ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 3 and module not in queen and module not in vent_shafts and module not in info_panels and module not in workers:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                                          \\\         | |")
      print("   | |        //                                            \\\        | |")
      print("   | |       //  =======                           =======   \\\       | |")
      print("   | |      //  /  ", modtwo ,"   \                         /  ", modthree ,"   \   \\\      | |")
      print("   | |     //  ∠=========⦣                       ∠=========⦣   \\\     | |")
      print("   | |    //                                                    \\\    | |")
      print("   | |   //                                                      \\\   | |")
      print("   | |  //                         =======                        \\\  | |")
      print("   | | //                         /  ", modone ,"   \                        \\\ | |")
      print("   | |//                         ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 2 and module != queen and module not in vent_shafts and module not in info_panels and module not in workers:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                  =======                 \\\         | |")
      print("   | |        //                  /  ", modtwo ," \                 \\\        | |")
      print("   | |       //                  ∠=========⦣                 \\\       | |")
      print("   | |      //                                                \\\      | |")
      print("   | |     //                                                  \\\     | |")
      print("   | |    //                                                    \\\    | |")
      print("   | |   //                                                      \\\   | |")
      print("   | |  //                         =======                        \\\  | |")
      print("   | | //                         /  ", modone ," \                        \\\ | |")
      print("   | |//                         ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 4 and module in vent_shafts:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                  =======                 \\\         | |")
      print("   | |        //                  /  ", modthree ,"   \                 \\\        | |")
      print("   | |       //  =======         ∠=========⦣       =======   \\\       | |")
      print("   | |      //  /  ", modtwo ,"   \                         /  ", modfour ,"   \   \\      | |")
      print("   | |     //  ∠=========⦣                       ∠=========⦣   \\\     | |")
      print("   | |    //     _____                                          \\\    | |")
      print("   | |   //     /|||||\ < VENT                                   \\\   | |")
      print("   | |  //     /|||||||\           =======                        \\\  | |")
      print("   | | //     /|||||||||\         /  ", modone ,"   \                        \\\ | |")
      print("   | |//      ‾‾‾‾‾‾‾‾‾‾‾        ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 3 and module in vent_shafts:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                                          \\\         | |")
      print("   | |        //                                            \\\        | |")
      print("   | |       //  =======                           =======   \\\       | |")
      print("   | |      //  /  ", modtwo ,"   \                         /  ", modfour ,"   \   \\\      | |")
      print("   | |     //  ∠=========⦣                       ∠=========⦣   \\\     | |")
      print("   | |    //     _____                                          \\\    | |")
      print("   | |   //     /|||||\ < VENT                                   \\\   | |")
      print("   | |  //     /|||||||\           =======                        \\\  | |")
      print("   | | //     /|||||||||\         /  ", modone ,"   \                        \\\ | |")
      print("   | |//      ‾‾‾‾‾‾‾‾‾‾‾        ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 2 and module in vent_shafts:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                  =======                 \\\         | |")
      print("   | |        //                  /  ", modtwo ,"   \                 \\\        | |")
      print("   | |       //                  ∠=========⦣                 \\\       | |")
      print("   | |      //                                                \\\      | |")
      print("   | |     //                                                  \\\     | |")
      print("   | |    //     _____                                          \\\    | |")
      print("   | |   //     /|||||\ < VENT                                   \\\   | |")
      print("   | |  //     /|||||||\           =======                        \\  | |")
      print("   | | //     /|||||||||\         /  ", modone ,"   \                        \\\ | |")
      print("   | |//      ‾‾‾‾‾‾‾‾‾‾‾        ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 4 and module in info_panels:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                  =======                 \\\         | |")
      print("   | |        //                  /  ", modthree ,"   \                 \\\        | |")
      print("   | |       //  =======         ∠=========⦣       =======   \\\       | |")
      print("   | |      //  /  ", modtwo ,"   \                         /  ", modfour ,"   \   \\\      | |")
      print("   | |     //  ∠=========⦣                       ∠=========⦣   \\\     | |")
      print("   | |    //     _____                                          \\\    | |")
      print("   | |   //     /QUEEN\ < INFO                                   \\\   | |")
      print("   | |  //     / IS IN \           =======                        \\\  | |")
      print("   | | //     /MODULE ", queen , "\         /  ", modone ,"   \                        \\ | |")
      print("   | |//      ‾‾‾‾‾‾‾‾‾‾‾        ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 3 and module in info_panels:   
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                                          \\\         | |")
      print("   | |        //                                            \\\        | |")
      print("   | |       //  =======                           =======   \\\       | |")
      print("   | |      //  /  ", modtwo ,"   \                         /  ", modfour ,"   \   \\\      | |")
      print("   | |     //  ∠=========⦣                       ∠=========⦣   \\\     | |")
      print("   | |    //     _____                                          \\\    | |")
      print("   | |   //     /QUEEN\ < INFO                                   \\\   | |")
      print("   | |  //     / IS IN \           =======                        \\\  | |")
      print("   | | //     /MODULE ", queen , "\         /   ", modone , "  \                        \\\ | |")
      print("   | |//      ‾‾‾‾‾‾‾‾‾‾‾        ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 2 and module in info_panels:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                  =======                 \\\         | |")
      print("   | |        //                  /  ", modtwo , "   \                 \\\        | |")
      print("   | |       //                  ∠=========⦣                 \\\       | |")
      print("   | |      //                                                \\\      | |")
      print("   | |     //                                                  \\\     | |")
      print("   | |    //     _____                                          \\\    | |")
      print("   | |   //     /QUEEN\ < INFO                                   \\\   | |")
      print("   | |  //     / IS IN \           =======                        \\\  | |")
      print("   | | //     /MODULE ", queen , "\         /  ", modone , "   \                        \\\ | |")
      print("   | |//      ‾‾‾‾‾‾‾‾‾‾‾        ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 4 and module in workers:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                  ,'""`.                  \\\         | |")
      print("   | |        //                  / _  _ \                  \\\        | |")
      print("   | |       //  =======          |(@)(@)|         =======   \\\       | |")
      print("   | |      //  /  ", modtwo , "   \         )  __  (        /  ", modfour , "   \   \\\      | |")
      print("   | |     //  ∠=========⦣       /,'))((`.\      ∠=========⦣   \\\     | |")
      print("   | |    //                    (( ((  )) ))                    \\\    | |")
      print("   | |   //                      `\ `)(' /'                      \\\   | |")
      print("   | |  //                         =======                        \\\  | |")
      print("   | | //                         /  ", modone , "   \                        \\\ | |")
      print("   | |//                         ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 3 and module in workers:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                  ,'""`.                  \\\         | |")
      print("   | |        //                  / _  _ \                  \\\        | |")
      print("   | |       //  =======          |(@)(@)|         =======   \\\       | |")
      print("   | |      //  /  ", modtwo , "   \         )  __  (        /  ", modthree , "   \   \\\      | |")
      print("   | |     //  ∠=========⦣       /,'))((`.\      ∠=========⦣   \\\     | |")
      print("   | |    //                    (( ((  )) ))                    \\\    | |")
      print("   | |   //                      `\ `)(' /'                      \\\   | |")
      print("   | |  //                         =======                        \\\  | |")
      print("   | | //                         /  ", modone , "   \                        \\\ | |")
      print("   | |//                         ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 2 and module in workers:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||                                      ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                  ,'""`.                  \\\         | |")
      print("   | |        //                  / _  _ \                  \\\        | |")
      print("   | |       //                   |(@)(@)|                   \\\       | |")
      print("   | |      //                    )  __  (                    \\\      | |")
      print("   | |     //                    /,'))((`.\                    \\\     | |")
      print("   | |    //                    (( ((  )) ))                    \\\    | |")
      print("   | |   //                      `\ `)(' /'                      \\\   | |")
      print("   | |  //                         =======                        \\\  | |")
      print("   | | //                         /  ", modone , "   \                        \\\ | |")
      print("   | |//                         ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 4 and module in queen:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                _,--._                ||           | |")
      print("   | |           ||              ,'      `.              ||           | |")
      print("   | |           ||      |\     / ,-.  ,-. \     /|      ||           | |")
      print("   | |           ||      )o),/ ( ( ~ )( ~ ) ) \.(o(      ||           | |")
      print("   | |           ||     /o/// /|  `-'  `-'  |\  \\o\     ||           | |")
      print("   | |           ||    / / |\ \(   .    ,   )/ /| \ \    ||           | |")
      print("   | |           ||    | | \o`-/    `\/'    \-'o/ | |    ||           | |")
      print("   | |           ||    \ \  `,'              `.'  / /    ||           | |")
      print("   | |           || \.  \ `-'  ,'|   /\   |`.  `-' /  ,/ ||           | |")
      print("   | |           ||  \`. `.__,' /   /  \   \ `.__,' ,'/  ||           | |")
      print("   | |           ||   \o\     ,'  ,'    `.  `.     /o/   ||           | |")
      print("   | |           ||    \o`==='--/          \--`==='o/    ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                  =======                 \\\         | |")
      print("   | |        //                  /  ", modthree , "   \                 \\\        | |")
      print("   | |       //  =======         ∠=========⦣       =======   \\\       | |")
      print("   | |      //  /  ", modtwo , "   \                         /  ", modfour , "   \   \\\      | |")
      print("   | |     //  ∠=========⦣                       ∠=========⦣   \\\     | |")
      print("   | |    //                                                    \\\    | |")
      print("   | |   //                                                      \\\   | |")
      print("   | |  //                         =======                        \\\  | |")
      print("   | | //                         /  ", modone , "   \                        \\ | |")
      print("   | |//                         ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 3 and module in queen:   
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                _,--._                ||           | |")
      print("   | |           ||              ,'      `.              ||           | |")
      print("   | |           ||      |\     / ,-.  ,-. \     /|      ||           | |")
      print("   | |           ||      )o),/ ( ( ~ )( ~ ) ) \.(o(      ||           | |")
      print("   | |           ||     /o/// /|  `-'  `-'  |\  \\o\     ||           | |")
      print("   | |           ||    / / |\ \(   .    ,   )/ /| \ \    ||           | |")
      print("   | |           ||    | | \o`-/    `\/'    \-'o/ | |    ||           | |")
      print("   | |           ||    \ \  `,'              `.'  / /    ||           | |")
      print("   | |           || \.  \ `-'  ,'|   /\   |`.  `-' /  ,/ ||           | |")
      print("   | |           ||  \`. `.__,' /   /  \   \ `.__,' ,'/  ||           | |")
      print("   | |           ||   \o\     ,'  ,'    `.  `.     /o/   ||           | |")
      print("   | |           ||    \o`==='--/          \--`==='o/    ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                                          \\\         | |")
      print("   | |        //                                            \\\        | |")
      print("   | |       //  =======                           =======   \\\       | |")
      print("   | |      //  /  ", modtwo , "   \                         /   ", modthree , "  \   \\\      | |")
      print("   | |     //  ∠=========⦣                       ∠=========⦣   \\\     | |")
      print("   | |    //                                                    \\\    | |")
      print("   | |   //                                                      \\\   | |")
      print("   | |  //                         =======                        \\\  | |")
      print("   | | //                         /  ", modone , "   \                        \\\ | |")
      print("   | |//                         ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    elif len(possible_moves) == 2 and module in queen:
      print("    ____________________________________________________________________")
      print("   | |‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾TT‾‾‾‾‾‾‾‾‾‾‾| |")
      print("   | |           ||                _,--._                ||           | |")
      print("   | |           ||              ,'      `.              ||           | |")
      print("   | |           ||      |\     / ,-.  ,-. \     /|      ||           | |")
      print("   | |           ||      )o),/ ( ( ~ )( ~ ) ) \.(o(      ||           | |")
      print("   | |           ||     /o/// /|  `-'  `-'  |\  \\o\     ||           | |")
      print("   | |           ||    / / |\ \(   .    ,   )/ /| \ \    ||           | |")
      print("   | |           ||    | | \o`-/    `\/'    \-'o/ | |    ||           | |")
      print("   | |           ||    \ \  `,'              `.'  / /    ||           | |")
      print("   | |           || \.  \ `-'  ,'|   /\   |`.  `-' /  ,/ ||           | |")
      print("   | |           ||  \`. `.__,' /   /  \   \ `.__,' ,'/  ||           | |")
      print("   | |           ||   \o\     ,'  ,'    `.  `.     /o/   ||           | |")
      print("   | |           ||    \o`==='--/          \--`==='o/    ||           | |")
      print("   | |           ||______________________________________||           | |")
      print("   | |          // ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ \\\          | |")
      print("   | |         //                  =======                 \\\         | |")
      print("   | |        //                  /  ", modtwo , "   \                 \\\        | |")
      print("   | |       //                  ∠=========⦣                 \\\       | |")
      print("   | |      //                                                \\\      | |")
      print("   | |     //                                                  \\\     | |")
      print("   | |    //                                                    \\\    | |")
      print("   | |   //                                                      \\\   | |")
      print("   | |  //                         =======                        \\\  | |")
      print("   | | //                         /  ", modone , "   \                        \\\ | |")
      print("   | |//                         ∠=========⦣                        \\\| |")
      print("   | |/______________________________________________________________\\| |")
      print("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    else:
      print("image not found, possible overlay of multiple elements")
    sleep(1) 
  else:
    print("you can move to any of the", len(possible_moves), "modules connected")
    print("you can move to")
    print("| ", end="")
    for i in range(0, len(possible_moves)):
      print(str(possible_moves[i]) + " | ", end="")
  print("")
  print("Power:", power, "Fuel:", fuel)
  print("")
  return null

def move_queen():
  global num_modules, module, last_module, locked, queen, won, vent_shafts
  #if we are in the same module as the queen
  if module == queen:
    #main_source_1 = audio.play_file('audio.wav')
    rain("There it is! The queen alien is also in this module...")
    #decide how many moves the queen should take
    moves_to_make = random.randint(1, 3)
    can_move_to_last_module = False
    while moves_to_make > 0:
      #get the escapes the queen can make
      escapes = get_modules_from(queen)
      #remove the current module as an escape
      if module in escapes:
        escapes.remove(module)
      #allow queen to double back behind us from another module
      if last_module in escapes and can_move_to_last_module == False:
        escapes.remove(last_module)
      #remove a module that is locked as an escape
      if locked in escapes:
        escapes.remove(locked)
      #if there is no escape then player has won
      if len(escapes) == 0:
        won = True
        moves_to_make = 0
        rain("... and the door is locked. It's trapped!")
      #otherwise move the queen to an adjacent module
      else:
        if moves_to_make == 1:
          rain("...and has escaped.")
        random.choice(escapes)
        moves_to_make -= 1
        can_move_to_last_module = True
        #handle the queen being in a module with a vent shaft
        while queen in vent_shafts:
          if moves_to_make > 1:
            rain("...and has escaped")
          rain("We can hear scuttling in the vents")
          valid_move = False
          #queen cannot land in a module with another vent
          while valid_move == False:
            valid_move = True
            queen = random.randint(1, num_modules)
            if queen in vent_shafts:
              valid_move = False
            #queen always stops moving after travelling through shaft
            moves_to_make = 0
          
def intuition():
  intu = 0
  global possible_moves, workers, vent_shafts
  #Check what is in each of the possible 
  for connected_module in possible_moves:
    if connected_module in workers:
      rain("I can hear something scuttling!")
      intu += 1
    if intu != 0:
      return null
    if connected_module in vent_shafts:
      rain("I can feel cold air")
      intu += 1
    if intu != 0:
      return null
  return null

def spawn_npcs():
  global num_modules, queen, vent_shafts, info_panels, workers
  module_set = []
  for counter in range(2, num_modules + 1):
    module_set.append(counter)
  random.shuffle(module_set)
  i = 0
  queen = module_set[i]
  for counter in range(0, 3):
    i = i + 1
    vent_shafts.append(module_set[i])
  for counter in range (0, 2):
    i = i + 1
    info_panels.append(module_set[i])
  for counter in range(0, 3):
    i = i + 1
    workers.append(module_set[i])
  return null

def start_menu():
  global enter_shop, coins, admin, rains, power, fuel
  #  if skip != True:
  load(2, random.randint(1, 2))
  #skip = False
#  if options["Beta mode"] == True:
#    main_source = audio.play_file("main.mp3")
#    main_source.set_loop(-1)
  main_source = audio.play_file("main.mp3")
  clear()
  if played == 0:
  # and skip != True:
    print("      \033[1;31;50m___           \033[1;32;50m___           \033[1;34;50m___                   \033[1;36;50m___           \033[1;35;50m___      ")
    sleep(speed_2)
    print("     \033[1;31;50m/\  \         \033[1;32;50m/\  \         \033[1;34;50m/\__\      \033[1;37;50m___        \033[1;36;50m/\__\         \033[1;35;50m/\__\     ")
    sleep(speed_2)
    print("     \033[1;31;50m\:\  \       \033[1;32;50m/::\  \       \033[1;34;50m/:/  /     \033[1;37;50m/\  \      \033[1;36;50m/:/  /        \033[1;35;50m/::|  |    ")
    sleep(speed_2)
    print("      \033[1;31;50m\:\  \     \033[1;32;50m/:/\:\  \     \033[1;34;50m/:/  /      \033[1;37;50m\:\  \    \033[1;36;50m/:/  /        \033[1;35;50m/:|:|  |    ")
    sleep(speed_2)
    print("      \033[1;31;50m/::\  \   \033[1;32;50m/::\~\:\  \   \033[1;34;50m/:/  /       \033[1;37;50m/::\__\  \033[1;36;50m/:/  /  ___   \033[1;35;50m/:/|:|__|__  ")
    sleep(speed_2)
    print("     \033[1;31;50m/:/\:\__\ \033[1;32;50m/:/\:\ \:\__\ \033[1;34;50m/:/__/     \033[1;37;50m__/:/\/__/ \033[1;36;50m/:/__/  /\__\ \033[1;35;50m/:/ |::::\__\ ")
    sleep(speed_2)
    print("    \033[1;31;50m/:/  \/__/ \033[1;32;50m\:\~\:\ \/__/ \033[1;34;50m\:\  \    \033[1;37;50m/\/:/  /    \033[1;36;50m\:\  \ /:/  / \033[1;35;50m\/__/~~/:/  / ")
    sleep(speed_2)
    print("   \033[1;31;50m/:/  /       \033[1;32;50m\:\ \:\__\    \033[1;34;50m\:\  \   \033[1;37;50m\::/__/      \033[1;36;50m\:\  /:/  /        \033[1;35;50m/:/  /  ")
    sleep(speed_2)
    print("   \033[1;31;50m\/__/         \033[1;32;50m\:\ \/__/     \033[1;34;50m\:\  \   \033[1;37;50m\:\__\       \033[1;36;50m\:\/:/  /        \033[1;35;50m/:/  /   ")
    sleep(speed_2)
    print("                  \033[1;32;50m\:\__\        \033[1;34;50m\:\__\   \033[1;37;50m\/__/        \033[1;36;50m\::/  /        \033[1;35;50m/:/  /    ")
    sleep(speed_2)
    print("                   \033[1;32;50m\/__/         \033[1;34;50m\/__/                 \033[1;36;50m\/__/         \033[1;35;50m\/__/     ")
    print("\033[1;37;50m")
    sleep(2)
    print(" _______           _          ______           _______                 _     ")
    sleep(speed_2)
    print("(_______)         | |        (____  \         (_______)               | |    ")
    sleep(speed_2)  
    print(" _  _  _ _____  __| |_____    ____)  )_   _        _  ___  ____  _____| |__  ")
    sleep(speed_2)
    print("| ||_|| (____ |/ _  | ___ |  |  __  (| | | |   _  | |/ _ \|  _ \(____ |  _ \ ")
    sleep(speed_2)
    print("| |   | / ___ ( (_| | ____|  | |__)  ) |_| |  | |_| | |_| | | | / ___ | | | |")
    sleep(speed_2)
    print("|_|   |_\_____|\____|_____)  |______/ \__  |   \___/ \___/|_| |_\_____|_| |_|")
    sleep(speed_2)
    print("                                     (____/                                  ")
    sleep(speed_2)
    print(" _______                      ___               _                    _ ")
    sleep(speed_2)
    print("(_______)                    / __)             | |                  | |")
    sleep(speed_2)
    print(" _        ____ _____ _ _ _ _| |__ ___   ____ __| |   _____ ____   __| |")
    sleep(speed_2)
    print("| |      / ___|____ | | | (_   __) _ \ / ___) _  |  (____ |  _ \ / _  |")
    sleep(speed_2)
    print("| |_____| |   / ___ | | | | | | | |_| | |  ( (_| |  / ___ | | | ( (_| |")
    sleep(speed_2)
    print(" \______)_|   \_____|\___/  |_|  \___/|_|   \____|  \_____|_| |_|\____|")
    sleep(speed_2)
    print("")
    sleep(speed_2)
    print(" _______           _     ")
    sleep(speed_2)
    print("(_______)         | |    ")
    sleep(speed_2)
    print("     _ _____  ____| |  _ ")
    sleep(speed_2)
    print(" _  | (____ |/ ___) |_/ )")
    sleep(speed_2)
    print("| |_| / ___ ( (___|  _ ( ")
    sleep(speed_2)
    print(" \___/\_____|\____)_| \_)")
    sleep(speed_2)
    print("")
    sleep(speed_2)
    print(" ______  _       _                    _                  ")
    sleep(speed_2)
    print("(_____ \(_)     | |                  | |                 ")
    sleep(speed_2)
    print(" _____) )_  ____| |__  _____  ____ __| | ___  ___  ____  ")
    sleep(speed_2)
    print("|  __  /| |/ ___)  _ \(____ |/ ___) _  |/___)/ _ \|  _ \ ")
    sleep(speed_2)
    print("| |  \ \| ( (___| | | / ___ | |  ( (_| |___ | |_| | | | |")
    sleep(speed_2)  
    print("|_|   |_|_|\____)_| |_\_____|_|   \____(___/ \___/|_| |_|")
    sleep(speed_2)
    print("")
    sleep(7)
  #skip = False
  ns = " "
  start_point = "\033[1;31;50m◉"
  help_point = ns
  shop_point = ns
  options_point = ns
  credits_point = ns
  stats_point = ns
  quit_point = ns
  global a
  a = 4
  arrow = null
  if played == 0:
    coins = 0
  while 1 == 1:  
    arrow = null
    clear()
    print("\033[1;37;50mType 'u' Or 'd' To Navigate The Menu And Type 'e' To Enter")
    for i in range(0, a - 1):
      print("")
    print("Coins:", coins)
    for i in range(0, a - 1):
      print("")
    print("\033[1;31;50m  ", start_point, "\033[1;31;50m  Start")
    for i in range(0, a):
      print("")
    print("\033[1;32;50m  ", help_point, "\033[1;32;50m  How to play")
    for i in range(0, a):
      print("")
    print("\033[1;33;50m  ", shop_point, "\033[1;33;50m  Shop")
    for i in range(0, a):
      print("")
    print("\033[1;34;50m  ", options_point, "\033[1;34;50m  Options")
    for i in range(0, a):
      print("")
    print("\033[1;37;50m  ", credits_point, "\033[1;37;50m  Credits")
    if played != 0:
      for i in range(0, a):
        print("")
      print("\033[1;36;50m  ", stats_point, "\033[1;36;50m  Stats")
    for i in range(0, a):
      print("")
    print("\033[1;35;50m  ", quit_point, "\033[1;35;50m  Quit")
    print("\033[1;37;50m")
    #d_print("This is the Menu, where you can operate commands and the like")
    #print("")
    arrow = getkey()
    if arrow == "d":
      if start_point != ns:
        start_point = ns
        help_point = "\033[1;32;50m◉"
      else:
        if help_point != ns:
          help_point = ns
          shop_point = "\033[1;33;50m◉"
        else:
          if shop_point != ns:
            shop_point = ns
            options_point = "\033[1;34;50m◉"
          else:
            if options_point != ns:
              options_point = ns
              credits_point = "\033[1;37;50m◉"
            else:
              if credits_point != ns and played != 0:
                credits_point = ns
                stats_point = "\033[1;36;50m◉"
              elif stats_point != ns:
                  stats_point = ns
                  quit_point = "\033[1;35;50m◉"
              elif credits_point != ns and played == 0:
                credits_point = ns
                quit_point = "\033[1;35;50m◉" 
              elif quit_point != ns:
                quit_point = ns
                start_point = "\033[1;31;50m◉"
    elif arrow == "u":
      if start_point != ns:
        start_point = ns
        quit_point = "\033[1;35;50m◉"
      else:
        if quit_point != ns and played != 0:
          quit_point = ns
          stats_point = "\033[1;36;50m◉"
        elif stats_point != ns:
          stats_point = ns
          credits_point = "\033[1;37;50m◉"
        elif quit_point != ns and played == 0:
          quit_point = ns
          credits_point = "\033[1;37;50m◉"
        else:    
            if credits_point != ns:
              credits_point = ns
              options_point = "\033[1;34;50m◉"
            else:
              if options_point != ns:
                options_point = ns
                shop_point = "\033[1;33;50m◉"
              else:
                if shop_point != ns:
                  shop_point = ns
                  help_point = "\033[1;32;50m◉"
                else:
                  if help_point != ns:
                    help_point = ns
                    start_point = "\033[1;31;50m◉"
    elif arrow == "e":
      if start_point != ns:
        clear()
        rain("Ok, Starting Program!")
        sleep(3)
        clear()
        return null
      elif help_point != ns:
        clear()
        rain("This is a game where you travel around the Charles Darwin, a spaceship that has been taken over by aliens")
        print("")
        rain("You navigate your surrondings with your keyboard and you alone decide what happens")
        print("")
        rain("The main aim is to defeat the queen alien, Telium. To do so, you move around the map and block doors to trap and kill Telium")
        print("")
        rain("There are helper aliens who help her and you can kill them too, there are vents that can transport you to any random module")
        print("")
        rain("There is a limited amount of fuel and power on the spaceship, so be fast and efficient in your hunt!")
        print("")
        rain("To return to the menu, Type 'menu' when a word input is required, digit inputs won't work!")
        print("")
        rain("But most importantly... have fun!")
        sleep(5)
        continue
      elif shop_point != ns:
        while 1 == 1:
          enter_shop = True
          mf = ("more fuel", "MORE FUEL", "More Fuel", "More fuel", "fuel", "FUEL", "Fuel", "MF", "mf")
          mp = ("more power", "MORE POWER", "More Power", "More power", "power", "POWER", "Power", "MP", "mp")
          mc = ("more coins", "MORE COINS", "More Coins", "More coins", "coins", "COINS", "Coins", "MC", "mc")
          qm = ("less queen moves", "LESS QUEEN MOVES", "Less Queen Moves", "Less queen moves", "queen moves", "QUEEN MOVES", "Queen Moves", "Queen moves", "queen", "QUEEN", "Queen", "moves", "MOVES", "Moves", "lqm", "LQM", "qm", "QM")
          ap = ("admin powers", "ADMIN POWERS", "Admin Powers", "Admin powers", "admin", "ADMIN", "Admin", "powers", "POWERS", "Powers", "ap", "AP")
          clear()
          if enter_shop == True:
            rain("Welcome to the Shop, to purchase an item, type the item's name. To exit, type 'exit'")
            print("")
          print("Coins:", coins)
          print("")
          for i in shop_items:
            print(i + ("..." * 3), shop_items[i][shop_buys[i]])
          print("")
          buying = input("> ")
          if buying in mf:
            buying = "More fuel"
          elif buying in mp:
            buying = "More power"
          elif buying in mc:
            buying = "More coins"
          elif buying in qm:
            buying = "Less queen moves"
          elif buying in ap:
            buying = "Admin powers"
          elif buying in answer_e:
            break
          if str(shop_items[buying][shop_buys[buying]]) != "Sold Out":
            try:
              if coins >= int(shop_items[buying][shop_buys[buying]]):
                rain("Are you sure? ")
                sure = input("> ")
                if sure in answer_y:
                  rain("Item bought!")
                  coins -= int(shop_items[buying][shop_buys[buying]])
                  print("You now have", coins, "coins")
                  sleep(2)
                  shop_buys[buying] = int(shop_buys[buying]) + 1
                  shop_items.update()
                  shop_buys.update()
              else:
                rain("You dont have enough coins!")
                sleep(2)
            except ValueError:
              rain("That item is sold out!")
              sleep(2)
          else:
            rain("That item is sold out!")
            sleep(2)
      elif options_point != ns:
        menu = 1
        global speed
        #global options
        global changing_diff
        changing_diff = 0
        while 1 == 1:
          clear()
          speed = options["Speed of text"]
          rain("What option do you want to edit? (Type exit to leave)")
          print("")
          for i in options:
            print(i, "=", options[i])
          print("")
          change = input("> ")
          if change not in options:
            if change in answer_e:
              break
            else:
              continue
          else:
            if change in ("Difficulty", "difficulty", "Diff", "diff", "DIFF", "DIFFICULTY"):
              if menu == 1:  
                changing_diff += 1
                rain("What is the new value for difficulty?")
                print("")
                changed = input("> ")
                if changed in ("easy", "EASY", "Easy", "E", "e"):
                  options["Difficulty"] = "E"
                  power = 250
                  fuel = 750
                elif changed in ("medium", "Medium", "MEDIUM", "normal", "Normal", "NORMAL", "M", "m", "N", "n"):
                  options["Difficulty"] = "M"
                  power = 150
                  fuel = 500
                elif changed in ("hard", "Hard", "HARD", "H", "h"):
                  options["Difficulty"] = "H"
                  power = 75
                  fuel = 400
                options.update()
              else:
                rain("This option can't be changed in-game")
            if change in ("speed of text", "speed of Text", "speed Of text", "speed Of Text", "Speed of text", "Speed of Text", "Speed Of text", "Speed Of Text", "SPEED OF TEXT", "Speed", "speed", "SPEED"):
              rain("What is the new value for Speed of text?")
              print("")
              raw_changed = input("> ")
              changed = float(raw_changed)
              if type(changed) != "<class 'str'>":
                numbered = True
              if numbered == True:
                if changed > 1:
                  rain("That value is too big!")
                  sleep(2)
                  continue
                elif changed < 0.075:
                  rain("That value is too small!")
                  sleep(2)
                  continue
                else:
                  options["Speed of text"] = changed
                  options.update()
                  speed = options["Speed of text"]
              else:
                rain("That's not a number")
                sleep(2)
                continue
            if change in ("Admin Mode", "Admin mode", "admin mode", "Admin", "admin", "ADMIN MODE", "ADMIN"):
              rain("What is change for Admin mode?")
              print("")
              changed = input("> ")
              if changed in ("true", "True", "TRUE", "t", "T"):
                rain("Passcode? ")
                password = input("> ")
                passcode = os.environ['passcode']
                if password == passcode:
                  rain("Admin powers now granted!")
                  admin = True
                  coins += 100000
                  options["Admin mode"] = True
                  continue
                else:
                  rain("Incorrect passcode")
                  admin = False
                  continue
              elif changed in ("False", "false", "F", "f"):
                admin = True
                options["Admin mode"] = True
                continue
            if change in ("Rainbow mode", "rainbow mode", "RAINBOW MODE", "Rainbow Mode"):
              rain("This mode isnt recommended! What is the new value for Rainbow mode?")
              print("")
              changed = input("> ")
              if changed in ("True", "true", "T"):
                rains = True
                options["Rainbow mode"] = True
                continue
              elif changed in ("False", "false", "F", "f"):
                rains = False
                options["Rainbow mode"] = False
                continue
              if change in ("Cut Scenes", "cut scenes", "Cut scenes", "CUT SCENES", "CUT", "cut", "SCENES", "Scenes", "scenes", "Cut"):
                if menu == 1:
                  rain("What is the new value?")
                  changed = input("> ")
                  if changed in ("True", "true", "T", "t"):
                    options["Cut Scenes"] = True
                  else:
                    options["Cut Scenes"] = False
                else:
                  rain("This option can't be changed in-game")
            if change in ("beta mode", "Beta mode", "Beta Mode", "BETA MODE", "BETA", "Beta", "beta"):
              if menu == 1:
                if options["Beta mode"] == False:
                  rain("Warning! These features may cause errors whilst playing the game! Are you sure you want to continue?")
                  sure = input("> ")
                  if sure in ("yes", "Yes", "YES", "y", "Y"):
                    options["Beta mode"] = True
                    rain("Beta mode is now on")
                  else:
                    continue
                else:
                  rain("Beta mode is now off")
                  options["Beta mode"] == False
              else:
                rain("This option can't be changed in-game")
        options.update()
        if changing_diff == 0:
          power = 150
          fuel = 500      
      elif credits_point != ns:
        clear()
        rain("Devs: Jonah 'The Craw' Crawford and Jack Richardson")
        print("")
        rain("Idea: Craig Sargent and David Hillyard")
        print("")
        rain("Music: Epic Mountain")
        sleep(5)
        continue
      elif stats_point != ns:
        clear()
        stats()
        continue
      elif quit_point != ns:
        clear()
        rain("Thanks for playing!")
        print("")
        sleep(0.5)
        print("")
        quit()
  clear()
  rain("Ok, Starting Program!")
  sleep(3)
  clear()
  return null


def map_raw():
  numb = output_module()
  if numb == 1: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | \033[1;36;50m1 \033[1;37;50m|")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 2: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | \033[1;36;50m2 \033[1;37;50m|___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 3: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| \033[1;36;50m3 \033[1;37;50m|            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 4: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | \033[1;36;50m4 \033[1;37;50m|            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 5: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | \033[1;36;50m5 \033[1;37;50m|")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 6: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | \033[1;36;50m6 \033[1;37;50m| ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 7: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | \033[1;36;50m7 \033[1;37;50m| ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 8: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |\033[1;36;50mS1 \033[1;37;50m| \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 9: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | \033[1;36;50m9 \033[1;37;50m| ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 10: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |\033[1;36;50m10 \033[1;37;50m|")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 11: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |\033[1;36;50m11 \033[1;37;50m| ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 12: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |\033[1;36;50m12 \033[1;37;50m|")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 13: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |\033[1;36;50m13 \033[1;37;50m|")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 14: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |\033[1;36;50mS2 \033[1;37;50m|   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 15: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |\033[1;36;50m15 \033[1;37;50m|       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 16: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |\033[1;36;50m16 \033[1;37;50m|")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 17: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |\033[1;36;50m17 \033[1;37;50m| ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  elif numb == 18: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |\033[1;36;50m18 \033[1;36;50m|")
    print("     ‾‾‾         ‾‾‾")
    print("")
  else: 
    clear()
    print("\033[1;37;50m")
    print("                                ___")
    print("                               | 1 |")
    print("                                ‾‾‾")
    print("                               |   |")
    print("           ___              ___     ___              ___")
    print("          | 4 |            | 2 |___| 3 |            | 5 |")
    print("           ‾‾‾              ‾‾‾     ‾‾‾              ‾‾‾")
    print("   ___    /   \    ___    /     ___     \    ___    /   \    ___")
    print("  | 6 | ‾‾     ‾‾ | 7 | ‾‾   / |S1 | \   ‾‾ | 9 | ‾‾     ‾‾ |10 |")
    print("   ‾‾‾             ‾‾‾ ‾‾‾‾‾‾   ‾‾‾   ‾‾‾‾‾‾ ‾‾‾             ‾‾‾")
    print("    \               /                         \               /")
    print("      ‾ \  ___  / ‾                             ‾ \  ___  / ‾")
    print("          |11 | ----------------------------------- |12 |")
    print("           ‾‾‾                                       ‾‾‾")
    print("")
    print("")
    print("           ___")
    print("          |13 |")
    print("     ___ / ‾‾‾ \ ___")
    print("    |15 |       |16 |")
    print("     ‾‾‾   ___ / ‾‾‾")
    print("      |   |S2 |   |")
    print("     ___ / ‾‾‾   ___")
    print("    |17 | ----- |18 |")
    print("     ‾‾‾         ‾‾‾")
    print("")
  return null

def pause_menu():
  global num_modules, queen, vent_shafts, info_panels, workers
  global coins
  clear()
  ns = " "
  continue_point = "\033[1;31;50m◉"
  map_point = ns
  options_point = ns
  quit_point = ns
  while 1 == 1:
    clear()
    print("\033[1;37;50mType 'u' Or 'd' To Navigate The Menu And Type 'e' To Enter")
    print("")
    print("\033[1;31;50m  ", continue_point, "\033[1;31;50m  Continue")
    for i in range(0, a):
      print("")
    print("\033[1;34;50m  ", map_point, "\033[1;34;50m  Map")
    for i in range(0, a):
      print("")
    print("\033[1;36;50m  ", options_point, "\033[1;36;50m  Options")
    for i in range(0, a):
      print("")
    print("\033[1;35;50m  ", quit_point, "\033[1;35;50m  Quit")
    print("\033[1;37;50m")
    arrow = getkey()
    if arrow == "d":
      if continue_point != ns:
        continue_point = ns
        map_point = "\033[1;34;50m◉"
      else:
        if map_point != ns:
          map_point = ns
          options_point = "\033[1;36;50m◉"
        else:
          if options_point != ns:
            options_point = ns
            quit_point = "\033[1;35;50m◉"
          else:
              if quit_point != ns:
                quit_point = ns
                continue_point = "\033[1;31;50m◉"
    elif arrow == "u":
      if continue_point != ns:
        continue_point = ns
        quit_point = "\033[1;31;50m◉"
      else:
        if quit_point != ns:
            quit_point = ns
            options_point = "\033[1;37;50m◉"
        else:
          if options_point != ns:
            options_point = ns
            map_point = "\033[1;35;50m◉"
          else:
            if map_point != ns:
              map_point = ns
              continue_point = "\033[1;34;50m◉"
    elif arrow == "e":
      if continue_point != ns:
        clear()
        return null
      elif map_point != ns:
        while 1 == 1:
          map_raw()
          print("\033[1;36;50mBlue \033[1;37;50mis your current position")
          rain("type 'exit' to exit")
          leave = input()
          if leave in ("exit", "Exit"):
            break
          else:
            continue
        continue    
      elif options_point != ns:
        menu = 2
        global speed
        global options
        global changing_diff
        changing_diff = 0
        while 1 == 1:
          clear()
          speed = options["Speed of text"]
          rain("What option do you want to edit? (Type exit to leave)")
          print("")
          for i in options:
            print(i, "=", options[i])
          print("")
          change = input("> ")
          if change not in options:
            if change in answer_e:
              break
            else:
              continue
          else:
            if change in ("Difficulty", "difficulty", "Diff", "diff", "DIFF", "DIFFICULTY"):
              if menu == 1:  
                changing_diff += 1
                rain("What is the new value for difficulty?")
                print("")
                changed = input("> ")
                if changed in ("easy", "EASY", "Easy", "E", "e"):
                  options["Difficulty"] = "E"
                  power = 250
                  fuel = 750
                elif changed in ("medium", "Medium", "MEDIUM", "normal", "Normal", "NORMAL", "M", "m", "N", "n"):
                  options["Difficulty"] = "M"
                  power = 150
                  fuel = 500
                elif changed in ("hard", "Hard", "HARD", "H", "h"):
                  options["Difficulty"] = "H"
                  power = 75
                  fuel = 400
                options.update()
              else:
                rain("This option can't be changed in-game")
            if change in ("speed of text", "speed of Text", "speed Of text", "speed Of Text", "Speed of text", "Speed of Text", "Speed Of text", "Speed Of Text", "SPEED OF TEXT", "Speed", "speed", "SPEED"):
              rain("What is the new value for Speed of text? (Must be in between 1 and 0.05 (inclusive))")
              print("")
              raw_changed = input("> ")
              changed = float(raw_changed)
              if type(changed) != "<class 'str'>":
                numbered = True
              if numbered == True:
                if changed > 1:
                  rain("That value is too big!")
                  sleep(2)
                  continue
                elif changed < 0.025:
                  rain("That value is too small!")
                  sleep(2)
                  continue
                else:
                  options["Speed of text"] = changed
                  options.update()
                  speed = options["Speed of text"]
              else:
                rain("That's not a number")
                sleep(2)
                continue
            if change in ("Admin Mode", "Admin mode", "admin mode", "Admin", "admin", "ADMIN MODE", "ADMIN"):
              rain("What is change for Admin mode?")
              print("")
              changed = input("> ")
              if changed in ("true", "True", "TRUE", "t", "T"):
                rain("Passcode? ")
                password = input("> ")
                passcode = os.environ['passcode']
                if password == passcode:
                  rain("Admin powers now granted!")
                  admin = True
                  coins += 100000
                  options["Admin mode"] = True
                  continue
                else:
                  rain("Incorrect passcode")
                  admin = False
                  continue
              elif changed in ("False", "false", "F", "f"):
                admin = True
                options["Admin mode"] = True
                continue
            if change in ("Rainbow mode", "rainbow mode", "RAINBOW MODE", "Rainbow Mode"):
              rain("This mode isnt recommended! What is the new value for Rainbow mode?")
              print("")
              changed = input("> ")
              if changed in ("True", "true", "T"):
                rains = True
                options["Rainbow mode"] = True
                continue
              elif changed in ("False", "false", "F", "f"):
                rains = False
                options["Rainbow mode"] = False
                continue
              if change in ("Cut Scenes", "cut scenes", "Cut scenes", "CUT SCENES", "CUT", "cut", "SCENES", "Scenes", "scenes", "Cut"):
                if menu == 1:
                  rain("What is the new value?")
                  changed = input("> ")
                  if changed in ("True", "true", "T", "t"):
                    options["Cut Scenes"] = True
                  else:
                    options["Cut Scenes"] = False
                else:
                  rain("This option can't be changed in-game")
        options.update()
        if changing_diff == 0:
          power = 150
          fuel = 500
      elif quit_point != ns:
        clear()
        rain("Thanks for playing!")
        print("")
        sleep(0.5)
        print("")
        quit()
      return null

def fav_module():
  favorite = statistics.mode(modules_ls)
  return favorite

def stats():
  fav = fav_module()
  if played != 0:
    stat_d = {
      "Games Played": played,
      "Games Won": wins,
      "Games Lost": loss,
      "Percentage Won": (wins / played) * 100 + "%",
      "Percentage Lost":(loss / played) * 100 + "%",
      "Destroyed Workers": worker_destroy,
      "Favorite Module": fav,
      "Total Coins": total_coins,
      "Coins Spent": total_coins - coins
    }
  else:
    stat_d = {
      "Games Played": 0,
      "Games Won": 0,
      "Games Lost": 0,
      "Percentage Won": "0%",
      "Percentage Lost": "0%",
      "Destroyed Workers": 0,
      "Favorite Module": "none",
      "Total Coins": 0,
      "Coins Spent": total_coins
    }
  db["global stats"][uname.node] = stat_d
  while 1 == 1:  
    clear()
    rain("Stats:")
    print("")
    for i in stat_d:
      print("")
      print(i, stat_d[i])
    print("")
    print("Exit?")
    exit = getkey()
    if exit == "y":
      return null
    else:
      continue
  return null

def check4menu(answer):
  global played
  global loss
  global admin
  checked = False
  if answer in ("Menu", "menu", "MENU"):
    checked = True
    pause_menu()
  elif admin == True and answer not in ("Menu", "menu", "MENU"):
    commands = ["cls", "wks", "qen", "vnt", "ifo"]
    raw = answer.split()
    if raw[0] in ("CMD", "cmd", "Cmd"):
      cmd = raw[1].lower()
      for i in commands:
        if cmd == "cls":
          clear()
        elif cmd == "wks":
          print(workers)
        elif cmd == "qen":
          print(queen)
        elif cmd == "vnt":
          print(vent_shafts)
        elif cmd == "ifo":
          print(info_panels)
        else:
          rain("no command found")
  else:
    checked = False
  return checked

def check4death():
  global played
  global loss
  if power <= 0 or not alive or fuel <= 0:
    if power <= 0:
      rain("The station has ran out of power and unable to sustain life support, you die!")
      sleep(3)
      clear()
    elif fuel <= 0:
      rain("You have ran put of fuel and are now unable to fire your flamethrower anymore more, the station eventually gets broken enough to crass into a nearby moon. You die!")
      sleep(3)
      clear()
    else:
      rain("The station has ran out of energy and unable to sustain life support, you die!")
      sleep(3)
      clear()
    played += 1
    loss += 1
  return played, loss

  # Main program starts here

while 1 == 1:  
  if admin == True:
    played += 1
  #played += 1
  start_menu()
  spawn_npcs()
  if admin == True:
    print("Queen alien is located in module:", queen)
    print("Ventilation shafts are located in modules:", vent_shafts)
    print("Info panels are located in modules:", info_panels)
    print("Worker aliens are located in modules:", workers)
    sleep(7)
  while alive and not won:
    load_module()
    check_vent_shafts()
    move_queen()
    worker_aliens()
    if won == False and alive == True:
      intuition()
      output_moves()
      get_action()
  if won == True:
    rain("The queen is trapped and you burn it to death with your flamethrower.")
    animation(2)
    rain(". . . . .")
    clear()
    rainbow("You Won!")
    print("\033[1;37;50m")
    if admin == True:
      craw.rickroll()
    won = False
    played += 1
    wins += 1
    if shop_buys["More coins"] == 1:
      coins += random.randint(30, 125)
    elif shop_buys["More coins"] == 2:
      coins += random.randint(50, 145)
    elif shop_buys["More coins"] == 3:
      coins += random.randint(50, 155)
    elif shop_buys["More coins"] == 4:
      coins += random.randint(65, 160)
    else:
      coins += random.randint(75, 175)
    total_coins += coins
  if alive == False:
    rain("The station has ran out of power and unable to sustain life support, you die!")
    sleep(5)
    clear()
    played += 1
    loss += 1
    if shop_buys["More coins"] == 1:
      coins += random.randint(10, 50)
    elif shop_buys["More coins"] == 2:
      coins += random.randint(20, 60)
    elif shop_buys["More coins"] == 3:
      coins += random.randint(30, 70)
    elif shop_buys["More coins"] == 4:
      coins += random.randint(40, 70)
    else:
      coins += random.randint(50, 75)
    total_coins += coins