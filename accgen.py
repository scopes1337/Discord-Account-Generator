import requests
import json
import requests
import random
import os
import sys
from colorama import Fore
import string
import threading
from capmonster_python import HCaptchaTask
import time
import proxygen
from itertools import cycle

letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
def create(username,invite):





    capmonster = HCaptchaTask("Buy ur own api key at capmonster")
    task_id = capmonster.create_task("https://discord.com/register", "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34")
    resultcap = capmonster.join_task_result(task_id)
    fingerprintx = requests.get('https://discord.com/api/v9/experiments')
    fingerprintreceived = fingerprintx.json()['fingerprint']

    url = "https://discord.com/api/v9/auth/register"
    payload = json.dumps({
    "fingerprint": fingerprintreceived,
    "email": f"{random_char(17)}@protonmail.com",
    "username": username,
    "password": "Sutminpiku002112",
    "invite": invite,
    "consent": True,
    "date_of_birth": "2000-04-01",
    "gift_code_sku_id": None,
    "captcha_key": resultcap.get("gRecaptchaResponse"),
    "promotional_email_opt_in": True
    })
    headers = {
    'authority': 'discord.com',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'x-fingerprint': fingerprintreceived,
    'x-debug-options': 'bugReporterEnabled',
    'accept-language': 'en-US',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'content-type': 'application/json',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'origin': 'https://discord.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://discord.com/register'
    }
    while True:
            proxies = proxygen.get_proxies()
            proxy_pool = cycle(proxies)
            proxy = next(proxy_pool)
            response = requests.request("POST", url, headers=headers, data=payload)#,proxies={'https':"http://"+proxy})
            time.sleep(2)
            if response.status_code == 201:
                token = response.json()['token']
                print(token)
            if response.status_code == 429:
                return print(f"{Fore.YELLOW}(RATE-LIMITED){Fore.RESET}" + response.text)
    else:
            return print("Something bad happend")






def fastreq(username,invite):
    threads = []
    for i in range(50):
        t = threading.Thread(target=create(username,invite))
        t.daemon = True
        threads.append(t)
    for i in range(50):
        threads[i].start()
    for i in range(50):
        threads[i].join()

if __name__ == "__main__":
    os.system("cls")
    userename = input("Username: ")
    invitecode = input("Invite: ")
    fastreq(userename,invitecode)
