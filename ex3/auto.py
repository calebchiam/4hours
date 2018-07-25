import pyautogui, time
# Intentionally written in the simplest way possible
# There are a lot of ways to do this

while True:
    pyautogui.click(751,44) # click on url
    pyautogui.typewrite('http://bit.ly/2JSVZZn')
    pyautogui.typewrite(['enter'])
    time.sleep(3) # wait for page to load
    pyautogui.click(441,597) # click on first input
    pyautogui.typewrite('Eren Yeager')
    pyautogui.typewrite(['tab'])
    pyautogui.typewrite('willkilltitans@gmail.com')
    pyautogui.typewrite(['tab'])
    pyautogui.typewrite('Within the walls')
    pyautogui.typewrite(['tab'])
    pyautogui.typewrite('94143889')
    pyautogui.typewrite(['tab'])
    pyautogui.typewrite('SASAGAEYO')
    pyautogui.typewrite(['tab', 'enter'])
    time.sleep(5)
