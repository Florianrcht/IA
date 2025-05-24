import requests
import asyncio
import threading


def servo_order_sender():

    async def timer():
        await asyncio.sleep(3)
        print("En ligne")

    async def looper():
        global searchFace
        global already_move
        while searchFace:
            order = print("<(a) | (d)>")
            # 10 - 45 => gauche 
            # 46 - 49 (0) => stop ?
            # 50 - 86 => droite
            if (order == "a"):
                print("<<< GAUCHE")
                already_move = "gauche"
                try:
                    response = requests.get('http://localhost:5000/speed/10')
                    print(response.text)
                except Exception as e:
                    print(f"Erreur lors de la requête : {e}")

            if (order == "d"):
                print(">>> DROITE")
                already_move = "droite"
                try:
                    response = requests.get('http://localhost:5000/speed/50')
                    print(response.text)
                except Exception as e:
                    print(f"Erreur lors de la requête : {e}")


    def start_async_loop():
        loop = asyncio.new_event_loop()
        time = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.set_event_loop(time)
        loop.run_until_complete(looper())
        time.run_until_complete(timer())


    if __name__ == '__main__':
        thread = threading.Thread(target=start_async_loop)
        thread.start()