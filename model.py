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
  volumne_norm = np.linalg.norm(indata) * 10
  print(volumne_norm)


def execute():
  while True:
    with sd.Stream(callback=print_sound):
      sd.sleep(duration * 5000)

execute()