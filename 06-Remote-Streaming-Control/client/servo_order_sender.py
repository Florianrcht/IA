import requests
import asyncio
import threading
import os
from dotenv import load_dotenv

load_dotenv()
host_ip = os.environ.get('RASPBERRY_IP')

# Variables de contrôle (à déplacer en paramétrage si besoin)
searchFace = True
already_move = None

def servo_order_sender():
    async def timer():
        await asyncio.sleep(3)
        print(f"En ligne sur {host_ip}")

    async def looper():
        global searchFace
        global already_move

        while searchFace:
            order = input("vitesse : ").strip().lower()

            if order == "a":
                print("<<< GAUCHE")
                already_move = "gauche"
                try:
                    response = requests.get(f'http://{host_ip}:5000/speed/6')
                    print(response.text)
                except Exception as e:
                    print(f"Erreur lors de la requête : {e}")

            elif order == "d":
                print(">>> DROITE")
                already_move = "droite"
                try:
                    response = requests.get(f'http://{host_ip}:5000/speed/8')
                    print(response.text)
                except Exception as e:
                    print(f"Erreur lors de la requête : {e}")

            elif order == "s":
                print(">>> STOP")
                try:
                    response = requests.get(f'http://{host_ip}:5000/speed/0')
                    print(response.text)
                except Exception as e:
                    print(f"Erreur lors de la requête : {e}")

            elif order == "k":
                print(">>> KILL")
                try:
                    response = requests.get(f'http://{host_ip}:5000/kill')
                    print(response.text)
                except Exception as e:
                    print(f"Erreur lors de la requête : {e}")


            else:
                print("Commande inconnue. Tape 'a' (gauche), 'd' (droite), ou 's' (stop).")

            await asyncio.sleep(0.1)

    def start_async_loop():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(asyncio.gather(
            timer(),
            looper()
        ))

    thread = threading.Thread(target=start_async_loop)
    thread.start()

# Exécution directe si fichier lancé seul
if __name__ == '__main__':
    servo_order_sender()
