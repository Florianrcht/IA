import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
searchFace = True 

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra.")
    exit()

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

    cv2.line(frame, (centre_ecran_x, 0), (centre_ecran_x, height), (0, 255, 0), 3) 
    cv2.putText(frame, 'Y', (centre_ecran_x - 70, 80), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4, cv2.LINE_AA)

    cv2.line(frame, (0, centre_ecran_y), (width, centre_ecran_y), (0, 255, 0), 3)   
    cv2.putText(frame, 'X', (width - 150, centre_ecran_y - 20), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4, cv2.LINE_AA)

    cv2.circle(frame, (centre_ecran_x, centre_ecran_y), 3, (255, 0, 0), 5)

    for (x, y, w, h) in faces:
        centre_tete_w = w // 2
        centre_tete_h = h // 2
        centre_tete_x = x + centre_tete_w
        centre_tete_y = y + centre_tete_h
        centre_tete_ecran_x = centre_tete_x - centre_ecran_x
        centre_tete_ecran_y = centre_tete_y - centre_ecran_y
        print("x :", centre_tete_ecran_x)
        print("y :", centre_tete_ecran_y)

        
        if (-100 < centre_tete_ecran_x < 100) and (-100 < centre_tete_ecran_y <100):
            print("au centre")

        if (centre_tete_ecran_y < -100):
            print("^^^ HAUT")
        
        if (centre_tete_ecran_y > 100):
            print("vvv BAS")

        if (centre_tete_ecran_x > 100):
            print(">>> DROITE")

        if (centre_tete_ecran_x < -100):
            print("<<< GAUCHE")

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.circle(frame, (centre_tete_x, centre_tete_y), 3, (0, 0, 255), 5)

    cv2.imshow('Détection de visage', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
