from function import *

zil_api_url = 'https://api.zilliqa.com/'
r_data = {
    "id": "1",
    "jsonrpc": "2.0",
    "method": "GetNumTxBlocks",
    "params": [""]
}

is_main_miner = True

property_box = PropertyBox()
parse_command_line_arguments(property_box)
print(f'Next arguments will be applied: '
      f'\n=============================================='
      f'\n{property_box}\n'
      f'\n==============================================')
check_is_test_run(property_box.test_run)

start_main_miner(property_box)

while True:
    try:
        response = requests.post(zil_api_url, json=r_data)
        print(f'res: {response}')
        print(f'status: {response.status_code}')
        print(f"json: {response.json()}")

        result = response.json()['result']
        last_2_digits = result[-2:]

        print(f"last 2 digits of block are {last_2_digits}, time is {datetime.now().time()}")

        count = get_count(last_2_digits, property_box)
        if count >= 99 or count < 1:
            if is_main_miner:
                is_main_miner = False
                start_zil_miner(property_box)
            print("zil miner works")
            sleep(count)
        else:
            if not is_main_miner:
                is_main_miner = True
                start_main_miner(property_box)
            print("main miner works")
            sleep(count)
    except KeyError as ke:
        print(f"ke: {ke}")
    except Exception as ex:
        print(f"ex: {ex}")

