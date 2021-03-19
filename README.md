# zil_switcher
The Python script that turns zil miner on and turns the main miner off when PoW (mining round) starts and vise versa.


# how to start
1st way:
You need to have python3 on your pc. Install pip.
Using pip run next command to load necessary libraries for script

`pip install requests`

`pip install psutil`

2nd way:
You need to activate virtual env (venv folder) that contains all dependencies.
Open cmd (command prompt) and go to the folder **zil_switcher** using **cd** command.
Inside zil_switcher folder run next command:

`venv\Scripts\activate.bat`

From here your environment is configured.
Open **m_switcher.py** in any text editor and change next variables:
`main_miner_filepath_to_bat`
`zil_miner_filepath_to_bat`

Write full path to your *.bat files.
Save file.

Back to cmd (command prompt) and run the zil_switcher:

`python m_switcher.py`