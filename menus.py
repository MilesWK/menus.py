from time import sleep

import cursor
cursor.hide()

from readchar import key, readkey
from replit import clear
from termcolor import colored

bold = '\033[1m'
italic = '\x1B[3m'
print('Configuring')
def menu(menu_items,menu_type):
  selected_menu = 1
  answer = ""
  while answer != key.ENTER:
    clear()
    for x in range(0,len(menu_items)):
      if selected_menu == x+1:
        if str(menu_type)=="1":
          print(f"> {italic}{menu_items[x]} \n")
        elif str(menu_type)=="2":
          print(colored(f"{bold}{menu_items[x]} \n","black","on_white"))
        elif str(menu_type) == "3":
          print(colored(f"{menu_items[x]} \n","red"))
      else:
        print(menu_items[x] + "\n")
    sleep(0.1)
    answer = readkey()
    if answer == key.DOWN and selected_menu < len(menu_items):
      selected_menu += 1
    elif answer == key.UP and selected_menu > 1:
      selected_menu -= 1
  
  Selected = menu_items[selected_menu-1]
  return Selected
  clear()
  
  
