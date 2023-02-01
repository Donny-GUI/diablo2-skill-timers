import pyautogui
from string import ascii_lowercase


Debug                       = True
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
BAR_WIDTH                   = 100
SKILL_HEIGHT                = 73



DIGITS                      = [str(x) for x in range(1, 10)]
LETTERS                     = [x for x in ascii_lowercase]
FNS                         = [f'F{x}' for x in range(1, 13)]
__other                     = ['space', 'tab', 'enter', 'shift', '`', 'left click', 'right click', 'up click', 'down click', 'scroll up', 'scroll down']
BINDS                       = DIGITS + LETTERS + FNS + __other



