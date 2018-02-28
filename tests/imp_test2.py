import pyautogui, time
import os

string1 = '28/02/2018'
string2 = '05/20/2018'
#print(pyautogui.position())

pyautogui.moveTo(200, 210, duration=2)
pyautogui.click(200,210)

pyautogui.typewrite(string1, interval=0.25)

pyautogui.moveTo(420, 210, duration=2)
pyautogui.click(420,210)

pyautogui.moveTo(830, 440, duration=2)
pyautogui.click(830,440)

pyautogui.press(['backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'])
pyautogui.typewrite(string2, interval=0.25)

pyautogui.moveTo(420, 210, duration=2)
pyautogui.click(420,210)

pyautogui.moveTo(830, 440, duration=2)
pyautogui.click(830,440)

pyautogui.moveTo(515, 105, duration=2)
pyautogui.click(515,105)

pyautogui.moveTo(385, 15, duration=2)
pyautogui.click(385,15)

pyautogui.moveTo(680, 440, duration=2)
pyautogui.click(680,440)


path = os.path.dirname(__file__)
path2 = str(os.path.dirname(path))
with open(path2+'\\savefile.txt') as f:
    lines = f.readlines()
string = str(lines[70])
string = string.split()
#print string[-1]
if string2 == string[-1]:
	print "SUCCESS"
else:
	print "FAIL"
	print string1, string[-1]

