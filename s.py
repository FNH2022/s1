import time
import os
import board
import digitalio

x = 0

btn1 = digitalio.DigitalInOut(board.D23)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

while True:
   if  button1.value:
      x = x+1
    else
      time.sleep(.25)
   print(x)
