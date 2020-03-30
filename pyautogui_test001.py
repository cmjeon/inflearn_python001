import pyautogui
import time

pyautogui.moveTo(22, 102, 2)
pyautogui.click()
pyautogui.moveTo(22, 57, 1)
pyautogui.click(clicks=2, interval=2)

pyautogui.moveTo(1332, 228, 2)
pyautogui.doubleClick()
time.sleep(1)
pyautogui.typewrite('Hello')
pyautogui.typewrite(['enter'])
pyautogui.typewrite(['a','b','enter','^','d'])