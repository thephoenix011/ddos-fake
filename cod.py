import os,sys
from colorama import Fore
def start():
    negocios="[ZOMBIE] DDOS IN"
    ip=input(f"{Fore.GREEN}-> Digite seu ip para dar um ddos fake!")
    for i in range(10000):
        print(f"{negocios} {ip}")
start()
