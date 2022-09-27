import pyautogui as nitesh

import time
time.sleep (10)

txt = open("BoysName.txt", "r")

a = "Hello"

for i in txt:
    nitesh.write (a+' '+i)
    nitesh.press('Enter')