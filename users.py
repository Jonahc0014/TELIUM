from replit import db
import os
import text_check
from time import sleep

null = ""

def clear():
  command = "clear"
  if os.name in ("nt", "dos"):
    command = "cls"
  os.system(command)
  return null

logged = False

def get_name():
  name = os.environ["REPL_OWNER"]
  if name not in db["users"]:
    db["users"].update({name : 1})
  else:
    times = db["users"][name]
    db["users"].pop(name)
    db["users"].update({name : int(times + 1)})
  return db["users"]

#db["passwords"] = {
#  "JonahCrawford" : "1a2b3c4d5e"
#}

db["user stats"] = {
  "JonahCrawford" : {
      "Games Played": 0,
      "Games Won": 0,
      "Games Lost": 0,
      "Percentage Won": "0%",
      "Percentage Lost": "0%",
      "Destroyed Workers": 0,
      "Favorite Module": "none",
      "Current Coins": 100,
      "Total Coins": 0,
      "Coins Spent": 0,
      "Upgrades": []
    }
  }


#change = [+1 if end of game, +1 if win, +1 if loss, +1 if worker, ±x coins, +x total coins, + spent coins, new upgrade dictonary]
#[played, win, lose, worker, coins, total coins, spent coins, upgrades]
def update_stats(shop_buys, username, change):
  try:
    if change[0] != 0:
      db["user stats"][username]["Games Played"] += change[0]
    if change[1] != 0:
      db["user stats"][username]["Games Won"] += change[1]
    if change[2] != 0:
      db["user stats"][username]["Games Lost"] += change[2]
    if change[3] != 0:
      db["user stats"][username]["Destroyed Workers"] += change[3]
    if change[4] != 0:
      db["user stats"][username]["Current Coins"] += change[4]
    if change[5] != 0:
      db["user stats"][username]["Total Coins"] += change[5]
    if change[6] != 0:
      db["user stats"][username]["Coins Spent"] += change[6]
    if change[7] != 0:
      db["user stats"][username]["Upgrades"] = change[7]
  finally:  
    print(db["user stats"])
    return shop_buys

username = ""
password = ""

def output():
  global username
  global password
  global logged
  return (username, password, logged)

def login():
  global logged
  global username
  global password
  name = str(os.environ["REPL_OWNER"])
  while 1 == 1:
    if logged:
      print("You are already logged in as", username)
    else:
      print("You are not logged in")
    print("Will you sign in or create a new account?")
    if logged:
      print("Or do you want to sign out?")
    method = input("> ")
    if method in ("Sign in", "sign in", "Sign In", "sign In", "SIGN IN", "SIGN", "Si", "SI", "si", "sI"):
      if logged:
        print("You are already logged in to", name + "!")
        print("You may not sign in unless you log off your current account!")
        sleep(3)
        return null
      clear()
      while 1 == 1:
        print("Please enter your username")
        username = input("> ")
        if username not in db["passwords"]:
          print("That username is not in use, please try again")
          continue
        else:
          break
      while 1 == 1:
        print("Please enter your password")
        password_new = input("> ")
        if db["passwords"][username] == password_new:
          print("You are now logged in as", username)
          logged = True
          break
        else:
          print("That is not the correct password for that username, please try again")
          continue
      sleep(3)
      #password = pasword_new
      name = username
      return null
    elif method in ("Sign out", "Sign Out", "sign out", "SIGN OUT", "sign Out", "so", "So", "sO", "SO") and logged:
      clear()
      while 1 == 1:
        print("Are you sure you want to log out?")
        sure = input("> ")
        if sure in ("yes", "Yes", "YES", "Y", "y"):
          logged = False
          username = ""
          password = ""
          print("You are now logged out of your account")
          break
        else:
          continue
      sleep(3)
      #password = pasword_new
      name = username
      return null
    elif method in ("Create a new account", "CREATE A NEW ACCOUNT", "Create A New Account", "Create a New Account", "CREATE", "create", "Create", "New Account", "new account", "New account", "NEW ACCOUNT", "NEW", "New", "new"):
      if logged:
        print("You are already logged in to", name + "!")
        print("You may not sign in unless you log off your current account!")
        sleep(3)
        return null
      clear()
      print("Your username has been automaticly set to", name + ",", "is this ok?")
      sure = input("> ")
      if sure  in ("no", "No", "NO", "n", "N"):
        print("No Problem, what do you want your username to be?")
        while 1 == 1:
          new_name = input("> ")
          if not text_check.check(new_name):
            print("That name is not allowed, please pick another")
            continue
          else:
            break
      else:
        new_name = name
      print("Now for a password")
      print("Your password must contain more then 8 characters and must include a special symbol (like @ or £)")
      print("Remember! You can' change this password once it has been set!")
      while 1 == 1:
        special = 0
        new_password = input()
        if len(new_password) >= 8:
          for i in new_password:
            if not i.isalpha() and i not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
              special += 1
          if special > 0 and special < len(new_password):
            print("That is a strong password!")
            break
          else:
            print("Sorry, that password doesnt fit our requirements")
            continue
        else:
          print("Sorry, that password doesnt fit our requirements")
          continue
      print("Your new account has been created!")
      logged = True
      db["passwords"].update({new_name : new_password})
      sleep(3)
      #password = pasword_new
      name = username
      db["user stats"].update({new_name : {
      "Games Played": 0,
      "Games Won": 0,
      "Games Lost": 0,
      "Percentage Won": "0%",
      "Percentage Lost": "0%",
      "Destroyed Workers": 0,
      "Favorite Module": "none",
      "Current Coins": 0,
      "Total Coins": 0,
      "Coins Spent": 0,
      "Upgrades": []
    }})
      return null
    else:
      return null