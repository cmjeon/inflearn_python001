import pyautogui

# i = pyautogui.locateCenterOnScreen('7.png')
# print(i)
# pyautogui.click(i)

print(pyautogui.position())
pyautogui.screenshot('1.png', region=(1387, 608, 30, 30))

num1 = pyautogui.locateCenterOnScreen('1.png')
pyautogui.click(num1)