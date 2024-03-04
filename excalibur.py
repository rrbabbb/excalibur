import os
import subprocess
import sys

# checks whether the platform used is windows, for using applicable shell command to activate venv
is_windows = sys.platform.startswith('win')

if is_windows:
    subprocess.call("launch.bat", shell=True)
else:
    subprocess.call("bash launch.sh", shell=True)


import pyautogui

pyautogui.displayMousePosition()


