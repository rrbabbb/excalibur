rem creates a virtualenvironment
python -m venv venv

rem activates virtualenvironment
call venv\Scripts\activate

rem installs the required libraries within virtualenvironment
pip install -r requirements.txt

rem exits virtualenvironment
deactivate