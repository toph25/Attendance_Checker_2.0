import pyautogui, time
# from AttendanceChecker import *

#print(pyautogui.position())

#click class 
pyautogui.moveTo(160, 220, duration=2)
pyautogui.click(160,220)

#click ViewClass button
pyautogui.moveTo(290, 81, duration=2)
pyautogui.click(290,81)

#click scrollbar
pyautogui.moveTo(500, 400, duration=2)
pyautogui.click(500,400)
# pyautogui.dragTo(x, y, duration=num_seconds)

#click a student
pyautogui.moveTo(200, 400, duration=2)
pyautogui.click(200,400)

#click Present button
pyautogui.moveTo(176, 659, duration=2)
pyautogui.click(176,659)

