rem creates venv and activates it
python -m venv venv
call venv\Scripts\activate

rem installs required dependencies
pip install -r requirements.txt

rem makes executable
pyinstaller excalibur.py

deactivate