import time
from colorama import Fore
servers = 8
clockspeed = 5.5
cores = 16
serverspresent = [True,True,True,True,True,True,True,True]
currentlymining = False
upgrades = 8
miningstarttime = 0
miningstoptime = 0
bitcoinspersecond = 0.28
bitcoinsavailable = 0
exchangerate = 1.25
money = 0
bitcoinssold = False
osOpen = True
def os():
  global servers,clockspeed,cores,serverspresent, osOpen
  if osOpen == True:
    print(Fore.LIGHTBLUE_EX + "[server OS]")
    boot = input("_")
    if boot == "boot":
      procedures = [">>loading...",">>found OS version",">>finished loading OS",">>booted OS.bit.4.2.7","----------------------------------------"]
      boottimes = [1,.25,1,0,0]
      for osinstall in range (5):
        print(procedures[osinstall])
        time.sleep(boottimes[osinstall])
      bitcoin()
    elif boot == "settings":
      servers = int(input(Fore.LIGHTMAGENTA_EX + "#servers: " + Fore.RESET))
      clockspeed = float(input(Fore.LIGHTMAGENTA_EX + "server clock speed: " + Fore.RESET))
      cores = input(Fore.LIGHTMAGENTA_EX + "#cores per server" + Fore.RESET)
    elif boot == "servers eject":
      if servers == 0:
        print(Fore.LIGHTYELLOW_EX + ">>no valid servers")
      else:
        ejection = input(">>enter which server to be ejected" + Fore.LIGHTCYAN_EX)
        if ejection == "back":
          pass
        else:
          servers -= 1
          clockspeed -= clockspeed / 8
          print(">>server " , ejection , ": ejected successfully")
          serverspresent[int(ejection) - 1] = False
    elif boot == "help":
      print(">>commands:\nboot, settings, servers eject, help, servers, vector install_servers")
    elif boot == "servers":
      print(Fore.LIGHTCYAN_EX + "\nSERVER 1: ", serverspresent[0],"\nSERVER 2: ", serverspresent[1],"\nSERVER 3: ", serverspresent[2],"\nSERVER 4: ", serverspresent[3],"\nSERVER 5: ", serverspresent[4],"\nSERVER 6: ", serverspresent[5],"\nSERVER 7: ", serverspresent[6],"\nSERVER 8: ", serverspresent[7])
    elif boot == "vector install_servers":
      print("which server is to be installed")
      serverinstaller = input("_" + Fore.LIGHTCYAN_EX)
      if serverinstaller.isalpha() == False:
        if int(serverinstaller) <= len(serverspresent):
          if serverspresent[int(serverinstaller) - 1] == False:
            serverspresent[int(serverinstaller) - 1] = True
            print(">>server " + serverinstaller + " installed successfully")
          else:
            print(Fore.LIGHTYELLOW_EX + ">>server " + serverinstaller + " already exists")
        else:
          print(Fore.LIGHTYELLOW_EX + ">>server identifier too great")
      else:
        print(Fore.LIGHTYELLOW_EX + ">>invalid")
    elif boot == "shutdown":
      print(">>shutting down")
      time.sleep(2)
      osOpen = False
    else:
      print(Fore.LIGHTYELLOW_EX + ">>unknown command")
    os()
def bitcoin():
  global currentlymining, miningstarttime, miningstoptime, money, bitcoinssold, clockspeed, bitcoinspersecond, upgrades
  if osOpen == True:
    command = input(Fore.RESET + "~")
    if command == "mining start":
      if currentlymining == False:
        print("~|mining started")
        miningstarttime = time.time()
        currentlymining = True
        bitcoinssold = False
      else:
        print(Fore.LIGHTYELLOW_EX + "~|already mining")
    elif command == "mining stop":
      if currentlymining == True:
        print("~|mining stopped")
        miningstoptime = time.time()
        miningtimedif = miningstoptime - miningstarttime
        currentlymining = False
      else:
        print(Fore.LIGHTYELLOW_EX + "~|not currently mining")
    elif command == "info":
      print(Fore.LIGHTRED_EX + "------------------INFO------------------\n~|servers detected: " , servers , "\n~|single server clock speed: " , round(clockspeed, 3) , "GHz\n~|# cores per server: " , cores , "\n~|type: bitminer rack\n~|upgrades: " , upgrades , "\n----------------------------------------")
    elif command == "bitcoin info":
      if currentlymining == True:
        midminingtime = time.time()
        miningtimedif = midminingtime - miningstarttime
      else:
        miningtimedif = miningstoptime - miningstarttime
      bitcoinsavailable = miningtimedif * bitcoinspersecond
      print(Fore.CYAN + "~|bitcoins: " , round(bitcoinsavailable,3))
      print("~|bitcoins value: £" , round(bitcoinsavailable * 1.25,3))
    elif command == "bitcoin sell":
      if currentlymining == True:
        midminingtime = time.time()
        miningtimedif = midminingtime - miningstarttime
      else:
        if bitcoinssold == False:
          miningtimedif = miningstoptime - miningstarttime
          bitcoinssold = True
        else:
          miningtimedif = 0
      bitcoinsavailable = miningtimedif * bitcoinspersecond
      money += bitcoinsavailable * 1.25
      miningstarttime = time.time()
      print(Fore.LIGHTRED_EX + "-----------------RECEIPT----------------\n~|# bitcoins: " , bitcoinsavailable , "\n~|converted bitcoins to: £" , bitcoinsavailable * 1.25 , "\n~|money transferred to bank account\n----------------------------------------")
    elif command == "upgrade":
      print("~|upgrade 1: + 256MHz\n~|cost: £200")
    elif command == "upgrade 1":
      if upgrades != 8:
        if money > 499:
          money -= 500
          clockspeed += .256
          bitcoinspersecond += .02
          upgrades += 1
          print("~|upgrade installed")
        else:
          print(Fore.LIGHTYELLOW_EX + "~|insufficient funds")
      else:
        print("~|maximum # of upgrades installed")
    elif command == "exit":
      print("~|closing bitminer2.5")
      time.sleep(1)
      print("~|exited")
      os()
    else:
      print(Fore.LIGHTYELLOW_EX + "invalid")
    bitcoin()
os()