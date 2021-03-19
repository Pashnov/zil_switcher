import os
from sys import platform
import requests
import time
from datetime import datetime
import subprocess
import psutil


# change variables for main and zil miners filepath to bat.
# for example:
# main_miner_filepath_to_bat = r'D:\Install\mining\t-rex-0.19.12-win-cuda11.1\trex_ETH-v_binance.bat'

main_miner_filepath_to_bat = r'D:\CHANGE_IT.bat'
zil_miner_filepath_to_bat = r'D:\CHANGE_ID.bat'

test_run = False

is_main_miner = True
main_process = None
zil_process = None

if test_run:
    print('TTTTTTTT  EEEEEEEE  SSSSSSSS  TTTTTTTT')
    print('   TT     EE        SS           TT   ')
    print('   TT     EEEEEEEE  SSSSSSSS     TT   ')
    print('   TT     EE              SS     TT   ')
    print('   TT     EEEEEEEE  SSSSSSSS     TT   ')

zil_api_url = 'https://api.zilliqa.com/'
r_data = {
    "id": "1",
    "jsonrpc": "2.0",
    # "method": "GetCurrentMiniEpoch",
    "method": "GetNumTxBlocks",
    "params": [""]
}


def get_count(last_2_digit):
    if test_run:
        print("type 2 digits")
        count = input()
        return int(count)
    else:
        return int(last_2_digits)


def sleep(count):
    if 1 < count < 97:
        print('sleep for 60 seconds')
        time.sleep(60)
    elif 97 <= count < 99:
        print('sleep for 5 seconds')
        time.sleep(5)
    else:
        print('sleep for 10 seconds')
        time.sleep(10)


def kill(proc_pid):
    try:
        process = psutil.Process(proc_pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()
    except Exception:
        pass


def start_main_miner():
    global zil_process, main_process
    if zil_process is not None:
        kill(zil_process.pid)
        zil_process = None
    print('Starting main miner')
    cwd = os.path.dirname(main_miner_filepath_to_bat)
    main_process = subprocess.Popen(main_miner_filepath_to_bat, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=cwd)
    print(f"process: {main_process}")
    print(f"process.pid: {main_process.pid}")


def start_zil_miner():
    global zil_process, main_process
    if main_process is not None:
        kill(main_process.pid)
        main_process = None
    print('Starting zil miner')
    cwd = os.path.dirname(zil_miner_filepath_to_bat)
    zil_process = subprocess.Popen(zil_miner_filepath_to_bat, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=cwd)
    print(f"process: {main_process}")
    print(f"process.pid: {main_process.pid}")


start_main_miner()
while True:
    try:
        response = requests.post(zil_api_url, json=r_data)
        print(f'res: {response}')
        print(f'status: {response.status_code}')
        print(f"json: {response.json()}")
        result = response.json()['result']
        last_2_digits = result[-2:]
        print(f"last_2_digits is {last_2_digits}, time is {datetime.now().time()}")
        count = get_count(last_2_digits)
        if count >= 99 or count < 1:
            if is_main_miner:
                is_main_miner = False
                start_zil_miner()
            print("zil miner works")
            sleep(count)
        else:
            if not is_main_miner:
                is_main_miner = True
                start_main_miner()
            print("main miner works")
            sleep(count)


    # except JSONDecodeError as js:
    #     print(f'js: {js}')
    except KeyError as ke:
        print(f"ke: {ke}")
    except Exception as ex:
        print(f"ex: {ex}")





# if platform == "linux" or platform == "linux2":
#     # linux
# elif platform == "darwin":
#     # OS X
# elif platform == "win32" or platform == "cygwin":
#     os.system(f"run-client.bat param1 param2")
#
# import subprocess
#
# filepath = r'C:\Users\MattR\Desktop\testing.bat' # raw string
#
# rc = subprocess.call([filepath, 'arg1'])
#
# rc1 = subprocess.Popen([filepath, 'arg1'], shell=True)
#
# rc1.getPid.terminate()
#
# var1 = "Hello, world!"
# os.putenv("VAR1", var1)
#
# os.system("C:\Windows\System32\cmd.exe /c z:\Scripts\myscript.bat")
#
# os.system("taskkill /f /im wordpad.exe")
# os.system("taskkill /f /im [executable name].exe")
#
# # linux, mac
# os.kill(pid, signal.SIGKILL)
# killedpid, stat = os.waitpid(pid, os.WNOHANG)
# if killedpid == 0:
# print >> sys.stderr, "ACK! PROCESS NOT KILLED?"
#
# # windows
# handle = subprocess.Popen("someprocess here", shell=False)
# subprocess.Popen("taskkill /F /T /PID %i"%handle.pid , shell=True)
