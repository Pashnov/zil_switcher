import os
import sys
from sys import platform
import requests
import time
from datetime import datetime
import subprocess
import psutil
import argparse

main_process = None
zil_process = None

startupinfo = None


class PropertyBox:

    def __init__(self):
        self.main_miner_filepath_to_bat = None
        self.zil_miner_filepath_to_bat = None
        self.test_run = False
        self.delay = 1

    def __str__(self):
        return f'\n main_miner_filepath_to_bat: {self.main_miner_filepath_to_bat}, ' \
               f'\n zil_miner_filepath_to_bat: {self.zil_miner_filepath_to_bat}, ' \
               f'\n test_run: {self.test_run}, '\
               f'\n delay: {self.delay} seconds'




def check_is_test_run(test_run):
    if test_run:
        print('TTTTTTTT  EEEEEEEE  SSSSSSSS  TTTTTTTT')
        print('   TT     EE        SS           TT   ')
        print('   TT     EEEEEEEE  SSSSSSSS     TT   ')
        print('   TT     EE              SS     TT   ')
        print('   TT     EEEEEEEE  SSSSSSSS     TT   ')


def parse_command_line_arguments(property_box: PropertyBox):
    global startupinfo
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '-main', '--main', help='filepath to main miner bat file', required=True)
    parser.add_argument('-z', '-zil', '--zil', help='filepath to zil miner bat file', required=True)
    parser.add_argument('-t', '-test', '-test_run', '--test_run', help='test run for debugging issues where number '
                                                                       'block it typed from cmd', action='store_true')
    parser.add_argument('-minimize', '--minimize', help='minimize command prompt windows', action='store_true')
    parser.add_argument('-delay', '--delay', help='delay before shutdown main miner and start zilliqa miner', default=1,
                        type=int)
    args = parser.parse_args()

    print(f'arguments: {args}')

    if args.main:
        if not os.path.exists(args.main):
            print(f'check that bat file exists for ZIL miner and filepath is correct. Filepath: {args.main}')
            sys.exit()
        property_box.main_miner_filepath_to_bat = args.main

    if args.zil:
        if not os.path.exists(args.zil):
            print(f'check that bat file exists for ZIL miner and filepath is correct. Filepath: {args.zil}')
            sys.exit()
        property_box.zil_miner_filepath_to_bat = args.zil

    property_box.test_run = args.test_run
    property_box.delay = args.delay

    if args.minimize:
        print("the windows is going to be minimized")
        SW_MINIMIZE = 6
        startupinfo = subprocess.STARTUPINFO()
        # startupinfo.dwFlags |= (subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW)
        startupinfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = SW_MINIMIZE


def get_count(last_2_digits, property_box: PropertyBox):
    if property_box.test_run:
        print("type 2 digits")
        count = input()
        return int(count)
    else:
        return int(last_2_digits)


def sleep(count):
    if 1 < count < 97:
        print('sleep for 60 seconds')
        time.sleep(60)
    elif 97 <= count < 98:
        print('sleep for 5 seconds')
        time.sleep(5)
    elif 98 <= count < 99:
        print('sleep for 1 seconds')
        time.sleep(1)
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


def start_main_miner(property_box: PropertyBox):
    global zil_process, main_process
    if zil_process is not None:
        kill(zil_process.pid)
        zil_process = None

    print('Starting main miner')
    main_bat = property_box.main_miner_filepath_to_bat

    cwd = os.path.dirname(main_bat)
    main_process = subprocess.Popen(main_bat, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=cwd,
                                    startupinfo=startupinfo)

    print(f"process: {main_process}")
    print(f"process.pid: {main_process.pid}")


def start_zil_miner(property_box: PropertyBox):
    print(f'\nDelay for {property_box.delay} seconds, went sleep\n')
    time.sleep(property_box.delay)
    global zil_process, main_process
    if main_process is not None:
        kill(main_process.pid)
        main_process = None

    print('Starting zil miner')
    zil_bat = property_box.zil_miner_filepath_to_bat

    cwd = os.path.dirname(zil_bat)
    zil_process = subprocess.Popen(zil_bat, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=cwd,
                                   startupinfo=startupinfo)

    print(f"process: {zil_process}")
    print(f"process.pid: {zil_process.pid}")

