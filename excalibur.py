import os
import subprocess
import sys

print(sys.executable)

# checks whether the platform used is windows, for using applicable shell command to activate venv
is_windows = sys.platform.startswith('win')

if is_windows:
    subprocess.call(os.path.join("venv","Scripts","activate"), shell=True)#os.path.join("venv", "Scripts", "activate"), shell=True)
else:
    subprocess.call(os.path.join("venv", "bin", "activate"), shell=True)


import pyautogui

pyautogui.displayMousePosition()


# import pyautogui

# pyautogui.dragTo(100,120)