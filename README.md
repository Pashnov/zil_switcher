# zil switcher zil_switcher zilliqa switcher
The Python script that turns zil miner on and turns the main miner off when PoW (mining round) starts and vise versa.


# how to start
1st way:
You need to have python3 on your pc. Install pip.
Using pip run next command to load necessary libraries for script

`pip install requests` </br>
`pip install psutil` </br>

2nd way:
You need to activate virtual environment (venv folder) that contains all dependencies.
Open cmd (command prompt) and go to the folder **zil_switcher** using **cd** command.
Inside zil_switcher folder run next command:

`venv\Scripts\activate.bat`

From here your environment is configured. 
Open **start_switcher.bat** in any text editor and change next variables:
`main_miner_filepath_to_bat` </br>
`zil_miner_filepath_to_bat` </br>

Write full path to your *.bat files.
Save file.

Back to cmd (command prompt) and run the zil_switcher:

`python zil_switcher.py`

#ps
video instructions - https://youtu.be/uiq7VIG-l3g

Ref link to ezil - https://ezil.me/?p=2969 (it will be huge thanks me)

If you want to support the project or me don't hesitate to donate.

**BTC** - `12tpyDdZHS41KPct3xB1gDZVkZaEZwQfjG` </br>
**ETH** - `0xdb87b6375a9889c28c650146aadfa57b2438bdac` </br>
**ZIL** - `zil13pj9nawd3hh4f4uk5j6xm0px95v7mg5pd8tj66` </br>
**ETC** - `0xdb87b6375a9889c28c650146aadfa57b2438bdac` </br>
**RVN** - `RUtagtDUsi2RwozadMznEzrVV2T7pGWYm4` </br>
**DOGE** - `DH2gjXCi6SPaFAt6V5UK31w2t8G6wsegQU` </br>

