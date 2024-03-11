# creates venv and activates it
python3 -m venv venv
venv/bin/activate

# installs required dependencies
pip install -r requirements.txt

# makes executable
pyinstaller excalibur.py

deactivate