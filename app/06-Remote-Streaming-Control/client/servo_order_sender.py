import requests
import asyncio
import threading
import os
from dotenv import load_dotenv
from pynput import keyboard

load_dotenv()
host_ip = os.environ.get('RASPBERRY_IP')

# Variables de contrôle
searchFace = True
already_move = None

command_queue = []

def on_press(key):
    try:
        k = key.char.lower()  
        if k in ['a', 'd', 's', 'k']:
            command_queue.append(k)
    except AttributeError:
        pass

def servo_order_sender():
    async def timer():
        await asyncio.sleep(3)
        print(f"En ligne sur {host_ip}")

    async def looper():
        global searchFace
        global already_move

        while searchFace:
            if command_queue:
                order = command_queue.pop(0)

                if order == 'a':
                    print("<<< GAUCHE")
                    already_move = "gauche"
                    try:
                        response = requests.get(f'http://{host_ip}:5000/speed/6')
                        print(response.text)
                    except Exception as e:
                        print(f"Erreur lors de la requête : {e}")

                elif order == 'd':
                    print(">>> DROITE")
                    already_move = "droite"
                    try:
                        response = requests.get(f'http://{host_ip}:5000/speed/8')
                        print(response.text)
                    except Exception as e:
                        print(f"Erreur lors de la requête : {e}")

                elif order == 's':
                    print(">>> STOP")
                    try:
                        response = requests.get(f'http://{host_ip}:5000/speed/0')
                        print(response.text)
                    except Exception as e:
                        print(f"Erreur lors de la requête : {e}")

                elif order == 'k':
                    print(">>> KILL")
                    try:
                        response = requests.get(f'http://{host_ip}:5000/kill')
                        print(response.text)
                        searchFace = False  # Arrête la boucle
                    except Exception as e:
                        print(f"Erreur lors de la requête : {e}")

            await asyncio.sleep(0.1)

    def start_async_loop():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(asyncio.gather(
            timer(),
            looper()
        ))

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    thread = threading.Thread(target=start_async_loop)
    thread.start()

if __name__ == '__main__':
    print("Contrôle du servo : appuie sur 'a', 'd', 's', ou 'k'")
    servo_order_sender()
