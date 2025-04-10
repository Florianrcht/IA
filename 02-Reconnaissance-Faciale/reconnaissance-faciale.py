import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur : Impossible de lire une frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    cv2.line(frame, (1000, 1100), (1000, 0), (0, 255, 0), 3)
    cv2.line(frame, (0, 550), (2000, 550), (0, 255, 0), 3)
#   cv2.line(frame, 1er(Horizontal, Verticale), 2eme(Horizontal, Verticale), (0, 255, 0), 3)

    for (x, y, w, h) in faces:
        face_center_x = x + w // 2
        face_center_y = y + h // 2

        print("face_center_x :", face_center_x) # horizontale
        print("face_center_y :", face_center_y) # verticale
        if (600 < face_center_x < 700) and (200 < face_center_y < 300):
            print("au centre")
            break 

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    print('Détection de visage', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
