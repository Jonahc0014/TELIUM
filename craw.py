import random
import os
import sys
import time
import curses
import locale
import curses
from datetime import datetime
#from vpython import *
from replit import audio

global null
null = ""
global speed
speed = 0.1
global options
options = {
    "Speed of text": speed,
    "Difficulty": "M",
    "Admin mode": False ,
    "Rainbow mode": False,
    "Cut Scenes": True
}
global power, fuel, admin, rains
power = 250
fuel = 750
admin = False
rains = False

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

def get_time():
  clear()
  for i in range(0, 50):
      now = datetime.now()
      current_time = now.strftime("%H:%M")
      print("\033[1;37;50m--------- Date:", now)
      sleep(0.08)
      clear()
  return null

def get_options():
  return options

def rickroll():
  print("\033[1;37;50m")
  clear()
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
  sleep(2)
  print("We're no strangers to love")
  sleep(2)
  print("You know the rules and so do I")
  sleep(2)
  print("A full commitment's what I'm thinking of")
  sleep(2)
  print("You wouldn't get this from any other guy")
  sleep(2)
  print("I just wanna tell you how I'm feeling")
  sleep(2)
  print("Gotta make you understand")
  sleep(2)
  print("Never gonna give you up")
  sleep(2)
  print("Never gonna let you down")
  sleep(2)
  print("Never gonna run around and desert you")
  sleep(2)
  print("Never gonna make you cry")
  sleep(2)
  print("Never gonna say goodbye")
  sleep(2)
  print("Never gonna tell a lie and hurt you")
  sleep(2)
  print(" We've known each other for so long")
  sleep(2)
  print("Your heart's been aching, but")
  sleep(2)
  print("You're too shy to say it")
  sleep(2)
  print("Inside, we both know what's been going on")
  sleep(2)
  print("We know the game and we're gonna play it")
  sleep(2)
  print(" And if you ask me how I'm feeling")
  sleep(2)
  print("Don't tell me you're too blind to see")
  sleep(2)
  print(" Never gonna give you up")
  sleep(2)
  print("Never gonna let you down")
  sleep(2)
  print("Never gonna run around and desert you")
  sleep(2)
  print("Never gonna make you cry")
  sleep(2)
  print("Never gonna say goodbye")
  sleep(2)
  print("Never gonna tell a lie and hurt you")
  sleep(2)
  print("Never gonna give you up")
  sleep(2)
  print("Never gonna let you down")
  sleep(2)
  print("Never gonna run around and desert you")
  sleep(2)
  print("Never gonna make you cry")
  sleep(2)
  print("Never gonna say goodbye")
  sleep(2)
  print("Never gonna tell a lie and hurt you")
  sleep(2)
  print("(Ooh, give you up)")
  sleep(2)
  print("(Ooh, give you up)")
  sleep(2)
  print("Never gonna give, never gonna give")
  sleep(2)
  print("(Give you up)")
  sleep(2)
  print("Never gonna give, never gonna give")
  sleep(2)
  print("(Give you up)")
  sleep(2)
  print("We've known each other for so long")
  sleep(2)
  print("Your heart's been aching, but")
  sleep(2)
  print("You're too shy to say it")
  sleep(2)
  print("Inside, we both know what's been going on")
  sleep(2)
  print("We know the game and we're gonna play it")
  sleep(2)
  print("I just wanna tell you how I'm feeling")
  sleep(2)
  print("Gotta make you understand")
  sleep(2)
  print("Never gonna give you up")
  sleep(2)
  print("Never gonna let you down")
  sleep(2)
  print("Never gonna run around and desert you")
  sleep(2)
  print("Never gonna make you cry")
  sleep(2)
  print("Never gonna say goodbye")
  sleep(2)
  print("Never gonna tell a lie and hurt you")
  sleep(2)
  print("Never gonna give you up")
  sleep(2)
  print("Never gonna let you down")
  sleep(2)
  print("Never gonna run around and desert you")
  sleep(2)
  print("Never gonna make you cry")
  sleep(2)
  print("Never gonna say goodbye")
  sleep(2)
  print("Never gonna tell a lie and hurt you")
  sleep(2)
  print("Never gonna give you up")
  sleep(2)
  print("Never gonna let you down")
  sleep(2)
  print("Never gonna run around and desert you")
  sleep(2)
  print("Never gonna make you cry")
  sleep(2)
  print("Never gonna say goodbye")
  sleep(2)
  print("Never gonna tell a lie and hurt you")
  while 1 == 1:
    print("Get rickrolled")
    sleep(0.1)
  return null


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
    print("\033[1;3" + str(colour) + ";50m" + str(c), end="")
  print("\033[1;37;50m", end="\n")
  return null

def opt(menu):
  global speed
  global options
  global changing_diff
  global power
  global fuel
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
      if change in ("Exit", "exit", "EXIT", "E", "e"):
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
        changed = input("> ")
        numbered = changed.isalnum()
        if numbered == True:
          if int(changed) > 1:
            rain("That value is too big!")
            sleep(2)
            continue
          elif int(changed) < 0.075:
            rain("That value is too small!")
            sleep(2)
            continue
          else:
            options["Speed of text"] = int(changed)
            options.update()
            speed = options["Speed of text"]
        else:
          continue
      if change in ("Admin Mode", "Admin mode", "admin mode", "Admin", "admin", "ADMIN MODE", "ADMIN"):
        rain("What is change for Admin mode?")
        print("")
        changed = input("> ")
        if changed in ("true", "True", "TRUE", "t", "T"):
          rain("Passcode?")
          password = input("> ")
          passcode = os.environ['passcode']
          if password == passcode:
            rain("Admin powers now granted!")
            admin = True
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
        rain("This mode isnt recomended! What is the new value for Rainbow mode?")
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
  return null
  
def credits(wait = 0.25):
  print("\033[1;31;50m __ __    ___   ____  ___        ___      ___  __ __    ___  _       ___   ____     ___  ____  ")
  sleep(wait)
  print("|  T  T  /  _] /    T|   \      |   \    /  _]|  T  |  /  _]| T     /   \ |    \   /  _]|    \ ")
  sleep(wait)
  print("|  l  | /  [_ Y  o  ||    \     |    \  /  [_ |  |  | /  [_ | |    Y     Y|  o  ) /  [_ |  D  )")
  sleep(wait)
  print("|  _  |Y    _]|     ||  D  Y    |  D  YY    _]|  |  |Y    _]| l___ |  O  ||   _/ Y    _]|    / ")
  sleep(wait)
  print("|  |  ||   [_ |  _  ||     |    |     ||   [_ l  :  !|   [_ |     T|     ||  |   |   [_ |    \ ")
  sleep(wait)
  print("|  |  ||     T|  |  ||     |    |     ||     T \   / |     T|     |l     !|  |   |     T|  .  Y")
  sleep(wait)
  print("l__j__jl_____jl__j__jl_____j    l_____jl_____j  \_/  l_____jl_____j \___/ l__j   l_____jl__j\_j")
  sleep(wait)
  print("                                                                                              ")
  sleep(wait)
  print("  ____   ___   ____    ____  __ __         __  ____    ____  __    __  _____   ___   ____   ___ ")  
  sleep(wait)
  print(" |    | /   \ |    \  /    T|  T  T       /  ]|    \  /    T|  T__T  T|     | /   \ |    \ |   \  ")
  sleep(wait)
  print(" l__  |Y     Y|  _  YY  o  ||  l  |      /  / |  D  )Y  o  ||  |  |  ||   __jY     Y|  D  )|    \ ")
  sleep(wait)
  print(" __j  ||  O  ||  |  ||     ||  _  |     /  /  |    / |     ||  |  |  ||  l_  |  O  ||    / |  D  Y")
  sleep(wait)
  print("/  |  ||     ||  |  ||  _  ||  |  |    /   \_ |    \ |  _  |l  `  '  !|   _] |     ||    \ |     |")
  sleep(wait)
  print("\  `  |l     !|  |  ||  |  ||  |  |    \     ||  .  Y|  |  | \      / |  T   l     !|  .  Y|     |")
  sleep(wait)
  print(" \____j \___/ l__j__jl__j__jl__j__j     \____jl__j\_jl__j__j  \_/\_/  l__j    \___/ l__j\_jl_____j")
  sleep(wait)
  print("                                                                                                  ")
  sleep(wait)
  print("\033[1;33;50m  ____   _____  _____ ____   _____ ______      ___      ___  __ __    ___  _       ___   ____     ___  ____  ")
  sleep(wait)
  print(" /    T / ___/ / ___/l    j / ___/|      T    |   \    /  _]|  T  |  /  _]| T     /   \ |    \   /  _]|    \ ")
  sleep(wait)
  print("Y  o  |(   \_ (   \_  |  T (   \_ |      |    |    \  /  [_ |  |  | /  [_ | |    Y     Y|  o  ) /  [_ |  D  )")
  sleep(wait)
  print("|     | \__  T \__  T |  |  \__  Tl_j  l_j    |  D  YY    _]|  |  |Y    _]| l___ |  O  ||   _/ Y    _]|    / ")
  sleep(wait)
  print("|  _  | /  \ | /  \ | |  |  /  \ |  |  |      |     ||   [_ l  :  !|   [_ |     T|     ||  |   |   [_ |    \ ")
  sleep(wait)
  print("|  |  | \    | \    | j  l  \    |  |  |      |     ||     T \   / |     T|     |l     !|  |   |     T|  .  Y")
  sleep(wait)
  print("l__j__j  \___j  \___j|____j  \___j  l__j      l_____jl_____j  \_/  l_____jl_____j \___/ l__j   l_____jl__j\_j")
  sleep(wait)
  print("                                                                                                             ")
  sleep(wait)
  print("  ____   ____     __  __  _      ____   ____     __  __ __   ____  ____   ___     _____  ___   ____  ")
  sleep(wait)
  print(" |    | /    T   /  ]|  l/ ]    |    \ l    j   /  ]|  T  T /    T|    \ |   \   / ___/ /   \ |    \ ")
  sleep(wait)
  print(" l__  |Y  o  |  /  / |  ' /     |  D  ) |  T   /  / |  l  |Y  o  ||  D  )|    \ (   \_ Y     Y|  _  Y")
  sleep(wait)
  print(" __j  ||     | /  /  |    \     |    /  |  |  /  /  |  _  ||     ||    / |  D  Y \__  T|  O  ||  |  |")
  sleep(wait)
  print("/  |  ||  _  |/   \_ |     Y    |    \  |  | /   \_ |  |  ||  _  ||    \ |     | /  \ ||     ||  |  |")
  sleep(wait)
  print("\  `  ||  |  |\     ||  .  |    |  .  Y j  l \     ||  |  ||  |  ||  .  Y|     | \    |l     !|  |  |")
  sleep(wait)
  print(" \____jl__j__j \____jl__j\_j    l__j\_j|____j \____jl__j__jl__j__jl__j\_jl_____j  \___j \___/ l__j__j")
  sleep(wait)
  print("                                                                                                     ")
  sleep(wait)
  print("\033[1;32;50m  ____  ____  ______  __ __  __ __  ____       ____     ___   _____   ___   ____  ____      __  __ __    ___  ____  ")
  sleep(wait)
  print(" /    Tl    j|      T|  T  T|  T  T|    \     |    \   /  _] / ___/  /  _] /    T|    \    /  ]|  T  T  /  _]|    \ ")
  sleep(wait)
  print("Y   __j |  T |      ||  l  ||  |  ||  o  )    |  D  ) /  [_ (   \_  /  [_ Y  o  ||  D  )  /  / |  l  | /  [_ |  D  )")
  sleep(wait)
  print("|  T  | |  | l_j  l_j|  _  ||  |  ||     T    |    / Y    _] \__  TY    _]|     ||    /  /  /  |  _  |Y    _]|    / ")
  sleep(wait)
  print("|  l_ | |  |   |  |  |  |  ||  :  ||  O  |    |    \ |   [_  /  \ ||   [_ |  _  ||    \ /   \_ |  |  ||   [_ |    \ ")
  sleep(wait)
  print("|     | j  l   |  |  |  |  |l     ||     |    |  .  Y|     T \    ||     T|  |  ||  .  Y\     ||  |  ||     T|  .  Y")
  sleep(wait)
  print("l___,_j|____j  l__j  l__j__j \__,_jl_____j    l__j\_jl_____j  \___jl_____jl__j__jl__j\_j \____jl__j__jl_____jl__j\_j")
  sleep(wait)
  print("                                                                                                                    ")
  sleep(wait)
  print("  ____   ___   ____    ____  __ __         __  ____    ____  __    __  _____   ___   ____   ___   ")
  sleep(wait)
  print(" |    | /   \ |    \  /    T|  T  T       /  ]|    \  /    T|  T__T  T|     | /   \ |    \ |   \  ")
  sleep(wait)
  print(" l__  |Y     Y|  _  YY  o  ||  l  |      /  / |  D  )Y  o  ||  |  |  ||   __jY     Y|  D  )|    \ ")
  sleep(wait)
  print(" __j  ||  O  ||  |  ||     ||  _  |     /  /  |    / |     ||  |  |  ||  l_  |  O  ||    / |  D  Y")
  sleep(wait)
  print("/  |  ||     ||  |  ||  _  ||  |  |    /   \_ |    \ |  _  |l  `  '  !|   _] |     ||    \ |     |")
  sleep(wait)
  print("\  `  |l     !|  |  ||  |  ||  |  |    \     ||  .  Y|  |  | \      / |  T   l     !|  .  Y|     |")
  sleep(wait)
  print(" \____j \___/ l__j__jl__j__jl__j__j     \____jl__j\_jl__j__j  \_/\_/  l__j    \___/ l__j\_jl_____j")
  sleep(wait)
  print("                                                                                                  ")
  sleep(wait)
  print("\033[1;36;50m  ____  ____  ______  __ __  __ __  ____          __   ___   _      _       ____  ____  ")
  sleep(wait)
  print(" /    Tl    j|      T|  T  T|  T  T|    \        /  ] /   \ | T    | T     /    T|    \ ")
  sleep(wait)
  print("Y   __j |  T |      ||  l  ||  |  ||  o  )      /  / Y     Y| |    | |    Y  o  ||  o  )")
  sleep(wait)
  print("|  T  | |  | l_j  l_j|  _  ||  |  ||     T     /  /  |  O  || l___ | l___ |     ||     T")
  sleep(wait)
  print("|  l_ | |  |   |  |  |  |  ||  :  ||  O  |    /   \_ |     ||     T|     T|  _  ||  O  |")
  sleep(wait)
  print("|     | j  l   |  |  |  |  |l     ||     |    \     |l     !|     ||     ||  |  ||     |")
  sleep(wait)
  print("l___,_j|____j  l__j  l__j__j \__,_jl_____j     \____j \___/ l_____jl_____jl__j__jl_____j")
  sleep(wait)
  print("                                                                                        ")
  sleep(wait)
  print(" ___      ___  ____     ___  ____   ___     ____  ____    ___   ______ ")
  sleep(wait)
  print("|   \    /  _]|    \   /  _]|    \ |   \   /    T|    \  /   \ |      T")
  sleep(wait)
  print("|    \  /  [_ |  o  ) /  [_ |  _  Y|    \ Y  o  ||  o  )Y     Y|      |")
  sleep(wait)
  print("|  D  YY    _]|   _/ Y    _]|  |  ||  D  Y|     ||     T|  O  |l_j  l_j")
  sleep(wait)
  print("|     ||   [_ |  |   |   [_ |  |  ||     ||  _  ||  O  ||     |  |  |  ")
  sleep(wait)
  print("|     ||     T|  |   |     T|  |  ||     ||  |  ||     |l     !  |  |  ")
  sleep(wait)
  print("l_____jl_____jl__j   l_____jl__j__jl_____jl__j__jl_____j \___/   l__j  ")
  sleep(wait)
  print("                                                                       ")
  sleep(wait)
  print("\033[1;35;50m ____    ____   _____   ___         __   ___   ___      ___ ")
  sleep(wait)
  print("|    \  /    T / ___/  /  _]       /  ] /   \ |   \    /  _]")
  sleep(wait)
  print("|  o  )Y  o  |(   \_  /  [_       /  / Y     Y|    \  /  [_ ")
  sleep(wait)
  print("|     T|     | \__  TY    _]     /  /  |  O  ||  D  YY    _]")
  sleep(wait)
  print("|  O  ||  _  | /  \ ||   [_     /   \_ |     ||     ||   [_ ")
  sleep(wait)
  print("|     ||  |  | \    ||     T    \     |l     !|     ||     T")
  sleep(wait)
  print("l_____jl__j__j  \___jl_____j     \____j \___/ l_____jl_____j")
  sleep(wait)
  print("                                                            ")
  sleep(wait)
  print("    __  ____    ____  ____   ____       _____  ____  ____    ____    ___  ____   ______ ")
  sleep(wait)
  print("   /  ]|    \  /    Tl    j /    T     / ___/ /    T|    \  /    T  /  _]|    \ |      T")
  sleep(wait)
  print("  /  / |  D  )Y  o  | |  T Y   __j    (   \_ Y  o  ||  D  )Y   __j /  [_ |  _  Y|      |")
  sleep(wait)
  print(" /  /  |    / |     | |  | |  T  |     \__  T|     ||    / |  T  |Y    _]|  |  |l_j  l_j")
  sleep(wait)
  print("/   \_ |    \ |  _  | |  | |  l_ |     /  \ ||  _  ||    \ |  l_ ||   [_ |  |  |  |  |  ")
  sleep(wait)
  print("\     ||  .  Y|  |  | j  l |     |     \    ||  |  ||  .  Y|     ||     T|  |  |  |  |  ")
  sleep(wait)
  print(" \____jl__j\_jl__j__j|____jl___,_j      \___jl__j__jl__j\_jl___,_jl_____jl__j__j  l__j  ")
  sleep(wait)
  print("                                                                                        ")
  sleep(wait)
  print(" ___     ____  __ __  ____  ___        __ __  ____  _      _      __ __   ____  ____   ___")   
  sleep(wait)
  print("|   \   /    T|  T  |l    j|   \      |  T  Tl    j| T    | T    |  T  T /    T|    \ |   \ ") 
  sleep(wait)
  print("|    \ Y  o  ||  |  | |  T |    \     |  l  | |  T | |    | |    |  |  |Y  o  ||  D  )|    \ ")
  sleep(wait)
  print("|  D  Y|     ||  |  | |  | |  D  Y    |  _  | |  | | l___ | l___ |  ~  ||     ||    / |  D  Y")
  sleep(wait)
  print("|     ||  _  |l  :  ! |  | |     |    |  |  | |  | |     T|     Tl___, ||  _  ||    \ |     |")
  sleep(wait)
  print("|     ||  |  | \   /  j  l |     |    |  |  | j  l |     ||     ||     !|  |  ||  .  Y|     |")
  sleep(wait)
  print("l_____jl__j__j  \_/  |____jl_____j    l__j__j|____jl_____jl_____jl____/ l__j__jl__j\_jl_____j")
  sleep(wait)
  print("\033[1;37;50m")
  sleep((wait * 10) ** (wait * 10))