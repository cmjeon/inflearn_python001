import pyautogui

print(pyautogui.position())
pyautogui.moveTo(1400, 822, 1)
pyautogui.click()
for i in range(100):
    pyautogui.scroll(-100)