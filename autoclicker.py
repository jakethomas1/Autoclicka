import tkinter as tk
from pynput.mouse import Button, Controller
import time
#Imports***
  #tkinter is gui, 
  #pynput controller mouse allows for clicker() function, 
  #time is used in clicker function as end condition

#Global variables, including starting values for clicks and seconds
root = tk.Tk()
root.geometry("240x120")
root.title("Auto Clicker")

mouse = Controller()
cps = [5] 
sec = [2]
 
def clicker():  #Function called by Start button, clicks for selected amount in selected time frame
  time.sleep(2)
  start = time.time()
  while (time.time()-start) < sec[0]: 
    for i in range(cps[0]): 
      mouse.press(Button.left)
      mouse.release(Button.left) 
      time.sleep(1/cps[0])

def incsec(): #Helper function to increment variable then render change to GUI
  if sec[0] < 20:   #**********This is cap on time************
    sec[0] += 1
    l2["text"] = "{} s".format(sec[0])
    root.update()

def decsec(): #Helper function to decrement variable then render change to GUI
  if sec[0] > 0:
    sec[0] -= 1
    l2["text"] = "{} s".format(sec[0])

def incclicks(): #Helper function to increment variable then render change to GUI
  if cps[0] < 50:   #*********This is cap on click speed********
    cps[0] += 1 
    l["text"] = "{} /s".format(cps[0])
    root.update()

def decclicks(): #Helper function to decrement variable then render change to GUI
  if cps[0] > 0:
    cps[0] -= 1
    l["text"] = "{} /s".format(cps[0])
    root.update()

while True: #Event Loop, refresh called at end

  #Labels

    #Label containing numclicks
  l = tk.Label(root, text="{} /s".format(cps[0]))   
  l.pack()
  l.place(x=170, y=30)

    #Label containing seconds 
  l2 = tk.Label(root, text="{} s".format(sec[0]))
  l2.pack()
  l2.place(x=50, y=30)
  #Labels
  
  #Buttons
  startbutton = tk.Button(text="Start", command=(lambda:(clicker())))
  startbutton.pack()
  startbutton.place(x=90,y=10)

  addclick= tk.Button(text="+", command=(lambda:(incsec())))
  addclick.pack()
  addclick.place(x=40,y=50)
  
  subclick = tk.Button(text=" - ", command=(lambda:(decsec())))
  subclick.pack()
  subclick = subclick.place(x=40,y=80)
  
  addsec = tk.Button(text="+", command=(lambda:(incclicks())))
  addsec.pack()
  addsec.place(x=160,y=50)
  
  subsec = tk.Button(text=" - ", command=(lambda:(decclicks())))
  subsec.pack()
  subsec.place(x=160,y=80)
  #/Buttons
 
  root.mainloop()
