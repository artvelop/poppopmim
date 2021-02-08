import tkinter
from PIL import ImageTk, Image
import os
import time
import sounddevice as sd
import numpy as np
import threading

print (os.path.dirname(os.path.realpath(__file__)))

duration = 3 # seconds

def print_sound(indata, outdata, fames, time, status):
  root.volumne_norm = np.linalg.norm(indata) * 10


def execute():
  while True:
    with sd.Stream(callback=print_sound):
      sd.sleep(duration * 5000)

def onStartPopCat():
  root.voiceCheckThread.start()
  changePopCatMotion()

def changePopCatMotion():
  if int(root.volumne_norm) > 0:
    if root.popCatStatus == True:
      popCatLabel.configure(image=root.popCat1)
      root.popCatStatus = False
      time.sleep(0.05)
    else:
      popCatLabel.configure(image=root.popCat2)
      root.popCatStatus = True
      time.sleep(0.05)
  else:
    popCatLabel.configure(image=root.popCat2)
    root.popCatStatus = True

  root.after(10, changePopCatMotion)


def changePopCat(): 
  popCatLabel.configure(image=root.popCat1)

root = tkinter.Tk()
root.title('말하는 빱빱이')
root.geometry('560x420')
root.resizable(True, True)

root.popCatStatus = True
root.volumne_norm = 0

popCat1 = './resource/popcat1.gif'
popCat2 = './resource/popcat2.gif'
root.popCat1 = ImageTk.PhotoImage(Image.open(popCat1))
root.popCat2 = ImageTk.PhotoImage(Image.open(popCat2))

root.voiceCheckThread = threading.Thread(target=execute)

popCatLabel = tkinter.Label(root, image = root.popCat2)

startButton = tkinter.Button(root, text='start', command=onStartPopCat)

startButton.pack()
popCatLabel.pack()

root.mainloop()