############################################################
#########                                         # ########
########                        Made             #  ########
#######                          By             #    #######
######        TELIUM       Jonah Crawford      #      ######
#####                           and           #        #####
####                      Jack Richardson    #          ####
#############################################            ###
####            Idea                         #          ####
#####            By                           #        #####
######      Craig Sargent       TELIUM         #      ######
#######         and                             #    #######
########    David Hillyard                       #  ########
#########                                         # ########
############################################################

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
import statistics
from replit import audio

#https://replit.com/talk/ask/Python-How-do-I-input-without-pressing-enter/33815

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

null = ""
speed = 0.1
mod1 = []
commands = ("(l)OCK", "(q)UEEN", "(w)ORKERS", "(v)ENTS")
answer_y = ("yes", "Yes", "Y", "y", "YES")
answer_n = ("no", "No", "N", "n", "NO")
answer_e = ("ok", "OK", "Ok", "E", "e", "Enter", "enter", "ENTER")
global options, admin, rains
rains = False
admin = False
options_ref = craw.get_options()
speed = options_ref["Speed of text"]
global played, wins, loss, worker_destroy
played = 0
wins = 0
loss = 0
worker_destroy = 0
global module_ls
modules_ls = []


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

d_print("\033[1;37;50m")
clear()

#def rainbow(text):
#  for c in text:
#    colour = random.randint(1, 7)
#    if colour == 7:
#      print("\033[1;3" + str(colour) + ";47m", str(c), end="")
#    else:
#      print("\033[1;3" + str(colour) + ";50m", str(c), end="")
#  return null

def animation(type):
  if options_ref["Cut Scenes"] == True:
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
      print("|  \    \    |         | #420 |      ||  |              |______|")
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
      print("|  \    \    |         | #420 |    \033[1;31;50m--\033[1;37;50m||  |              |______|")
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
      print("|  \    \    |         | #420 |  \033[1;31;50m----\033[1;37;50m||  |              |______|")
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
      print("|  \    \    |         | #420 |\033[1;31;50m------\033[1;37;50m||  |              |______|")
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
      print("|  \    \    |         | #420 |      ||  |              |______|")
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
      print("|  \    \    |         | #420 |      ||  |              |______|")
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
      print("|  \    \    |         | #420 |      ||  |              |______|")
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
      print("|  \    \    |         | #420 |      ||  |              |______|")
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
      print("|  \    \    |         | #420 |      ||  |              |      |")
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
      print("|  \    \    |         | #420 |      ||  |              |      |")
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
      print("|  \    \    |         | #420 |      ||  |              |      |")
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
      print("|  \    \    |         | #420 |      ||  |              |      |")
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
      print("|  \    \    |         | #420 |      ||  |              |      |")
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
      for i in range(0, 11):
        print("||                                         ||")
      print("|L_________________________________________J|")
      print("L___________________________________________J")
      sleep(0.5)
      clear()
      print("┌-------------------------------------------┐")
      print("|┌-----------------------------------------┐|")
      print("||                                         ||")
      print("||                 SCANNER                 ||")
      print("||                                         ||")
      print("||                COMMANDS                 ||")
      print("||                                         ||")
      print("||        \033[1;31;50mLOCK\033[1;37;50m, \033[1;32;50mQUEEN\033[1;37;50m, \033[1;34;50mWORKERS\033[1;37;50m, \033[1;36;50mVENTS      \033[1;37;50m||")
      print("||                                         ||")
      print("|L_________________________________________J|")
      print("L___________________________________________J") 
      print("")
    return null
  else:
    return null
  return null

#animation(1)
#animation(2)
#animation(3)

def load(waited, type):
  clear()
  percent = 0
  waited = waited / 2
  wait = 0
  for i in range(0, 100):
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

#Procedure declarations

def check_vent_shafts():
  global num_modules, module, vent_shafts, fuel
  if module in vent_shafts:
    craw.rain("There is a bank of fuel cells here")
    print("")
    craw.rain("You load one into your flamethrower")
    print("")
    if options_ref["Difficulty"] == "E":
      fuel_gained = 75
    if options_ref["Difficulty"] == "M":
      fuel_gained = 50
    if options_ref["Difficulty"] == "H":
      fuel_gained = 25
    print("Fuel was", fuel, "now reading", fuel + fuel_gained)
    fuel = fuel + fuel_gained
    sleep(2)
    craw.rain("The doors suddenly lock shut")
    print("")
    craw.rain("What is happening to the station?")
    print("")
    craw.rain("Our only escape is to climb into the ventiltaion shaft")
    sleep(4)
    print("")
    craw.rain("We have no idea where we are going")
    sleep(4)
    print("")
    craw.rain("We follow the passages and find ourselfs silding down")
    sleep(3)
    load(0.5, random.randint(1, 2))
    last_module = module
    while module == last_module:
      module = random.randint(1, num_modules)
    load_module()
    check_vent_shafts()

def load_module():
  global module, possible_moves
  possible_moves = get_modules_from(module)
  output_module()

def lock():
  global num_modules, power, locked
  new_lock = int(input("Enter module to lock: "))
  check4menu(new_lock)
  if new_lock <= 0 or new_lock > num_modules:
    craw.rain("Invalid Module. Operation Failed.")
  elif new_lock == queen:
    craw.rain("Unable To Lock Module Due to Lifeform Present. Operation Failed.")
  else:
    locked = new_lock
    print("Module", locked, "Is Now Locked")
  if options_ref["Difficulty"] == "M":
    power_used = 25 + 5 * random.randint(0, 5)
  elif options_ref["Difficulty"] == "H":
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
  print("You are in module", module)
  return module

def worker_aliens():
  global module, workers, fuel, alive
  #Output alien encountered
  if module in workers:
    craw.rain("Startled, a small alien scuttles across the floor.")
    craw.rain("It turns and leaps towards us")
    #Get the player's action
    successful_attack = False
    while successful_attack == False:
      craw.rain("You can:")
      print("")
      craw.rain("- Short blast your flamethrower to frighten it away")
      craw.rain("- Medium blast your flamethrower to try to kill it")
      craw.rain("- Long blast your flamethrower to definetly kill it")
      craw.rain("")
      craw.rain("How will you react? ((s)MALL,(m)EDIUM, (l)ARGE)")
      action = 0
      while action not in ("S", "M", "L", "s", "m", "l"):
        action_2 = input("Press the trigger: ")
        check4menu(action_2)
        fuel_used = int(input("How much fuel will you use? ... "))
        check4menu(fuel_used)
        fuel = fuel - fuel_used
        #check if player has ran out of fuel
        check4death()
        if fuel <= 0:
          alive = False
          return null
        #work out how much fuel is needed
        if options_ref["Difficulty"] == "E":
          diff = 4
        elif options_ref["Difficulty"] == "M":
          diff = 5
        elif options_ref["Difficulty"] == "H":
          diff = 6
        if admin == True:
          fuel_needed = 0
          fuel_used = 0
        elif action_2 in ("s", "S"):
          fuel_needed = 30 + 10 * random.randint(0, diff)
        elif action_2 in ("m", "M"):
          fuel_needed = 60 + 10 * random.randint(0, diff)
        elif action_2 in ("l", "L"):
          fuel_needed = 90 + 10 * random.randint(0, diff)
        #Try again if not enough fuel was used
        if fuel_used >= fuel_needed:
          successful_attack = True
        else:
          craw.rain("The Alien squeals but it is not dead. It's angry")
        #successful action
      if action_2 in ("s", "S"):
        print("The alien scuttles away into the corner of the room")
      elif action_2 in ("m", "M"):
        dead_numb = random.randint(1, 10)
        if dead_numb < 4:
          craw.rain("The alien scuttles away into the corner of the room, but it is not dead")
        else:
          craw.rain("The Alien has been destroyed")
          worker_destroy += 1
          #remove the worker from the module
          workers.remove(module)
      elif action_2 in ("l", "L") or admin == True:
        print("The Alien has been destroyed")
        worker_destroy += 1
        #remove the worker from the module
        workers.remove(module)
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
        power_lost = random.randint(1, 5)
        if opt_ref["Difficulty"] == "H":
          power =- power_lost
          print("Power was", power + power_lost + ",", "now reading", power)
          sleep(2)
      else:
        print("The module must be connected to the current module.")
        sleep(3)
    elif choice in ("s", "S"):
      animation(3)
      print("Scanner Ready. Enter Command")
      print("")
      command = input("> ")
      check4menu(command)
      if command in ("LOCK", "Lock", "lock", "L", "l"):
        power = lock()
        return null
      elif command in ("Queen", "QUEEN", "Q", "q", "queen"):
        print("The Queen Alien is in module", queen)
        if options_ref["Difficulty"] == "M":
          power_used = 15 + 5 * random.randint(0, 3)
        elif options_ref["Difficulty"] == "H":
          power_used = 25 + 5 * random.randint(0, 5)
        check4death()        
      if command in ("Workers", "WORKERS", "W", "w", "workers"):
        print("The workers are in module(s)", workers)
        if options_ref["Difficulty"] == "M":
          power_used = 15 + 5 * random.randint(0, 3)
        elif options_ref["Difficulty"] == "H":
          power_used = 25 + 5 * random.randint(0, 5)
        check4death()
      if command in ("Vents", "VENTS", "V", "v", "vents"):
        print("The vents are in modules", vent_shafts)
        if options_ref["Difficulty"] == "M":
          power_used = 15 + 5 * random.randint(0, 3)
        elif options_ref["Difficulty"] == "H":
          power_used = 25 + 5 * random.randint(0, 5)
        check4death()
      check4death()
      print("You had", power, "power but now you have", power - power_used, "power")
      power = power - power_used
      check4death()

def output_moves():
  global possible_moves
  check_vent_shafts()
  print("")
  print("From here you can move to modules: | ", end="")
  for move in possible_moves:
    print(move, "| ", end="")
  print("")
  print("Power:", power, "Fuel:", fuel)
  print("")

def move_queen():
  global num_modules, module, last_module, locked, queen, won, vent_shafts
  #if we are in the same module as the queen
  if module == queen:
    craw.rain("There it is! The queen alien is also in this module...")
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
        craw.rain("... and the door is locked. It's trapped!")
      #otherwise move the queen to an adjacent module
      else:
        if moves_to_make == 1:
          craw.rain("...and has escaped.")
        random.choice(escapes)
        moves_to_make -= 1
        can_move_to_last_module = True
        #handle the queen being in a module with a vent shaft
        while queen in vent_shafts:
          if moves_to_make > 1:
            craw.rain("...and has escaped")
          craw.rain("We can hear scuttling in the vents")
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
      craw.rain("I can hear something scuttling!")
      intu += 1
    if intu != 0:
      return null
    if connected_module in vent_shafts:
      craw.rain("I can feel cold air")
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

speed_2 = 0.1

def start_menu():
  load(2, random.randint(1, 2))
  source = audio.play_file("music/background.wav")
  clear()
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
  ns = " "
  start_point = "\033[1;31;50m◉"
  help_point = ns
  options_point = ns
  credits_point = ns
  stats_point = ns
  quit_point = ns
  global a
  a = 5
  arrow = null
  while 1 == 1:  
    arrow = null
    clear()
    print("\033[1;37;50mType 'u' Or 'd' To Navigate The Menu And Type 'e' To Enter")
    print("")
    print("\033[1;31;50m  ", start_point, "\033[1;31;50m  Start")
    for i in range(0, a):
      print("")
    print("\033[1;32;50m  ", help_point, "\033[1;32;50m  How to play")
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
                help_point = "\033[1;32;50m◉"
              else:
                if help_point != ns:
                  help_point = ns
                  start_point = "\033[1;31;50m◉"
    elif arrow == "e":
      if start_point != ns:
        clear()
        craw.rain("Ok, Starting Program!")
        sleep(3)
        clear()
        return null
      elif help_point != ns:
        clear()
        craw.rain("This is a game where you travel around the Charles Darwin, a spaceship that has been taken over by aliens")
        print("")
        craw.rain("You navigate your surrondings with your keyboard and you alone decide what happens")
        print("")
        craw.rain("The main aim is to defeat the queen alien, Telium. To do so, you move around the map and block doors to trap and kill Telium")
        print("")
        craw.rain("There are helper aliens who help her and you can kill them too, there are vents that can transport you to any random module")
        print("")
        craw.rain("There is a limited amount of fuel and power on the spaceship, so be fast and efficient in your hunt!")
        print("")
        craw.rain("To return to the menu, Type 'menu' when a word input is required, digit inputs won't work!")
        print("")
        craw.rain("But most importantly... have fun!")
        sleep(5)
        continue
      elif options_point != ns:
        options, speed, power, fuel, admin, rains = craw.opt(1)       
      elif credits_point != ns:
        clear()
        craw.rain("Devs: Jonah 'The Craw' Crawford and Jack Richardson")
        print("")
        craw.rain("Idea: Craig Sargent and David Hillyard")
        print("")
        craw.rain("Music: Epic Mountain")
        sleep(5)
        continue
      elif stats_point != ns:
        clear()
        stats()
        continue
      elif quit_point != ns:
        clear()
        craw.rain("Thanks for playing!")
        print("")
        sleep(0.5)
        print("")
        quit()
  clear()
  craw.rain("Ok, Starting Program!")
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
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
    sleep(10)
  return null

def pause_menu():
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
        map_raw()
        continue
      elif options_point != ns:
        options, speed, power, fuel, admin, rains = craw.opt(2)      
      elif quit_point != ns:
        clear()
        craw.rain("Thanks for playing!")
        print("")
        sleep(0.5)
        print("")
        quit()
      return null

def fav_module():
  favorite = statistics.mode(module_ls)
  return favorite

def stats():
  fav = fav_module()
  if played != 0:
    stat_d = {
      "Games Played": played,
      "Games Won": wins,
      "Games Lossed": loss,
      "Percentage Won": (wins / played) * 100 + "%",
      "Percentage Lossed":(loss / played) * 100 + "%",
      "Destroyed Workers": worker_destroy,
      "Favorite Module": fav
    }
  else:
    stat_d = {
      "Games Played": 0,
      "Games Won": 0,
      "Games Lost": 0,
      "Percentage Won": 0,
      "Percentage Lossed": 0,
      "Destroyed Workers": 0,
      "Favorite Module": 0
    }
  while 1 == 1:  
    clear()
    craw.rain("Stats:")
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
  checked = False
  if answer in ("Menu", "menu", "MENU"):
    checked = True
    pause_menu()
  else:
    checked = False
  return checked

def check4death():
  if power <= 0 or not alive or fuel <= 0:
    if power <= 0:
      craw.rain("The station has ran out of power and unable to sustain life support, you die!")
      sleep(5)
      clear()
      played += 1
      loss += 1
    elif fuel <= 0:
      craw.rain("You have ran put of fuel and are now unable to fine more, you die!")
      sleep(5)
      clear()
      played += 1
      loss += 1
    else:
      craw.rain("The station has ran out of power and unable to sustain life support, you die!")
      sleep(5)
      clear()
      played += 1
      loss += 1

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
    craw.rain("The queen is trapped and you burn it to death with your flamethrower.")
    animation(2)
    craw.rain(". . . . .")
    clear()
    rainbow("You Won!")
    print("\033[1;37;50m")
    if admin == True:
      craw.rickroll()
    won = False
    played += 1
    win += 1
  if alive == False:
    craw.rain("The station has ran out of power and unable to sustain life support, you die!")
    sleep(5)
    clear()
    played += 1
    loss += 1