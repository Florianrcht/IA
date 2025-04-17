import cv2
import requests

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
searchFace = True 

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra.")
    exit()

while searchFace:
    print("en cours")
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

        
        if (-100 < centre_tete_ecran_x < 100) and (-100 < centre_tete_ecran_y <100):
            print("au centre")

        if (centre_tete_ecran_y < -100):
            print("^^^ HAUT")

        if (centre_tete_ecran_y > 100):
            print("vvv BAS")

        if (centre_tete_ecran_x > 100):
            print("<<< GAUCHE")
            try:
                # 10 - 45 => gauche 
                # 46 - 49 (0) => stop ?
                # 50 - 86 => droite
                
                response = requests.get('http://localhost:5000/speed/'+10)
                print(response.text)
            except Exception as e:
                print(f"Erreur lors de la requête : {e}")

        if (centre_tete_ecran_x < -100):
            print(">>> DROITE")
            try:
                # 10 - 45 => gauche 
                # 46 - 49 (0) => stop ?
                # 50 - 86 => droite
                
                response = requests.get('http://localhost:5000/speed/'+50)
                print(response.text)
            except Exception as e:
                print(f"Erreur lors de la requête : {e}")


cap.release()
cv2.destroyAllWindows()
