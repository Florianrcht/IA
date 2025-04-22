import cv2
import requests
import asyncio
import threading

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)
searchFace = True 
already_move = ""

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra.")
    exit()

async def timer():
    await asyncio.sleep(3)
    print("En ligne")

async def looper():
    global searchFace
    global already_move
    while searchFace:

        ret, frame = cap.read()
        if not ret:
            print("Erreur : Impossible de lire une frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        height, width, _ = frame.shape
        centre_ecran_x = width // 2
        centre_ecran_y = height // 2

        for (x, y, w, h) in faces:
            centre_tete_w = w // 2
            centre_tete_h = h // 2
            centre_tete_x = x + centre_tete_w
            centre_tete_y = y + centre_tete_h
            centre_tete_ecran_x = centre_tete_x - centre_ecran_x
            centre_tete_ecran_y = centre_tete_y - centre_ecran_y

            
            if (-100 < centre_tete_ecran_x < 100) and (-100 < centre_tete_ecran_y <100) and (already_move != "centre"):
                print("au centre")
                already_move = "centre"
                try:
                    response = requests.get('http://localhost:5000/speed/0')
                    print(response.text)
                except Exception as e:
                    print(f"Erreur lors de la requête : {e}")

            if (centre_tete_ecran_y < -100 and (already_move != "haut")):
                print("^^^ HAUT")
                already_move = "haut"

            if (centre_tete_ecran_y > 100 and (already_move != "bas")):
                print("vvv BAS")
                already_move = "bas"

            if (centre_tete_ecran_x > 100 and (already_move != "gauche")):
                print("<<< GAUCHE")
                already_move = "gauche"
                try:
                    response = requests.get('http://localhost:5000/speed/10')
                    print(response.text)
                except Exception as e:
                    print(f"Erreur lors de la requête : {e}")

            if (centre_tete_ecran_x < -100 and (already_move != "droite")):
                print(">>> DROITE")
                already_move = "droite"
                try:
                    # 10 - 45 => gauche 
                    # 46 - 49 (0) => stop ?
                    # 50 - 86 => droite
                    
                    response = requests.get('http://localhost:5000/speed/50')
                    print(response.text)
                except Exception as e:
                    print(f"Erreur lors de la requête : {e}")
    cap.release()
    cv2.destroyAllWindows()


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