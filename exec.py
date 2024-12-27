import random
import secrets
import json
import threading
import time

from main import TikTokApi

names = open("names.txt", "r", encoding="utf-8").read().splitlines()

api = TikTokApi('set proxy')

def __acc():
    email = f"{random.choice(names).split(' ')[0]}_{random.randint(10000, 99999)}@gmail.com"
    password = f"FL{random.randint(10000, 99999)}Test1*"
    dev = api.create_device()
    print(dev)
    if 'install_id' in str(dev):
        acc = api.create_account(email, password, dev)
        print(acc)
        if 'cookies' in str(acc):
            open("accounts.txt", "a+").write(json.dumps(acc) + "\n")
            open("devices.txt", "a+").write(json.dumps(dev) + "\n")
            time.sleep(3)
            print(__like(acc))

def __like(account: dict):
    return api.send_like('7442424948280315143', account)


for _ in range(20):
    threading.Thread(target=__acc).start()


