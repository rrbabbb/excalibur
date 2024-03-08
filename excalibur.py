import os
import subprocess
import sys

# checks whether the platform used is windows, for using applicable shell command to activate venv
is_windows = sys.platform.startswith('win')

if is_windows:
    subprocess.Popen(os.path.join("venv", "Scripts", "activate"), shell=True)
else:
    subprocess.Popen(os.path.join("venv", "bin", "activate"), shell=True)


import pyautogui

print(pyautogui.displayMousePosition())


