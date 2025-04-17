import cv2
import requests

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
searchFace = True 
last_direction = None 

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra.")
    exit()

def send_request(direction, speed):
    global last_direction
    if last_direction != direction:
        print(f"Direction changée : {direction}")
        last_direction = direction
        try:
            response = requests.get(f'http://localhost:5000/speed/{speed}')
            print(response.text)
        except Exception as e:
            print(f"Erreur lors de la requête : {e}")

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
        centre_tete_x = x + w // 2
        centre_tete_y = y + h // 2
        delta_x = centre_tete_x - centre_ecran_x
        delta_y = centre_tete_y - centre_ecran_y

        if -100 < delta_x < 100 and -100 < delta_y < 100:
            print(">>> CENTRE")
            send_request("center", 0)

        elif delta_x > 100:
            print("<<< GAUCHE")
            send_request("left", 10)

        elif delta_x < -100:
            print(">>> DROITE")
            send_request("right", 50)

        if delta_y < -100:
            print("^^^ HAUT")

        elif delta_y > 100:
            print("vvv BAS")

cap.release()
cv2.destroyAllWindows()
