import time

import pyautogui


countpos = int(input("количество позиций: "))
count = 0
while True:
    time.sleep(5)
    count += 1
    print(pyautogui.position())
    if count == countpos:
        break

