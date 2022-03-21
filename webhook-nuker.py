from discord_webhook import DiscordWebhook
import itertools
import time
import os
from colorama import init, Fore

os.system('clear')
os.system('cls')

print(Fore.BLUE + """                __    __                __  
 _      _____  / /_  / /_  ____  ____  / /__
| | /| / / _ \/ __ \/ __ \/ __ \/ __ \/ //_/
| |/ |/ /  __/ /_/ / / / / /_/ / /_/ / ,<   
|__/|__/\___/_.___/_/ /_/\____/\____/_/|_|  
                                            
                __            
   ____  __  __/ /_____  _____
  / __ \/ / / / //_/ _ \/ ___/
 / / / / /_/ / ,< /  __/ /    
/_/ /_/\__,_/_/|_|\___/_/      """)
print()
print()
print(Fore.GREEN + "           Creado por Eltotiz")
print("       https://github.com/Eltotiz")
print()

URL = input("[+] Coloque la URL del webhook: ")
print()

num = int(input("[+] Coloque cantidad de mensajes: "))
print()

text = input(f"[+] Escriba el mensaje que se enviara {num} veces: ")

os.system('clear')
os.system('cls')

print("|------------------------------")
print("|")
print("| [!] Panel de Control [!]")
print("|")
print(f"| [+] Se mandaran {num} mensajes.")
print("|")
print("| [!] Iniciando ataque...")
print("|")
print("|==============================")
print()

time.sleep(2)
os.system('clear')
os.system('cls')

print("|------------------------------")
print("|")
print("| [!] Panel de Control [!]")
print("|")
print(f"| [+] Se mandaran {num} mensajes.")
print("|")
print("| [!] Ataque iniciado.")
print("|")
print("|==============================")
print()
print()

time.sleep(1)

for _ in itertools.repeat(None, num):
    time.sleep(1)
    webhook = DiscordWebhook(url=f'{URL}', content=f'{text}')
    response = webhook.execute()
    
    print("Ataque enviado.")

