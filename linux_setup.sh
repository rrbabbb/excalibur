# creates a virtualenvironment
python -m venv venv

# activates the virtualenvironment
source venv/Scripts/activate

# installs the required libraries within virtualenvironment
pip install -r requirements.txt

# exits virtualenvironment
deactivate
