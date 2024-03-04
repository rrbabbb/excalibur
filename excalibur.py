import os
import subprocess
import sys


# checking whether the platform used is windows, for using applicable shell command to activate venv
is_windows = sys.platform.startswith('win')

if is_windows:
    venv_path = "venv\Scripts\activate"
    subprocess.call(f"call {venv_path}", shell=True)
else:
    venv_path = "venv/bin/activate"
    subprocess.call(f"source {venv_path}", shell=True)


import pyautogui

pyautogui.dragTo(100,120)