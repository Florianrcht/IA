import RPi.GPIO as GPIO  
import time  
import keyboard  # Permet de détecter les touches du clavier

# Configuration GPIO
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.OUT)  

# Configuration du signal PWM
p = GPIO.PWM(11, 330)  # Fréquence 330 Hz pour un servo à rotation continue
p.start(50)  # 50% = STOP

servoVitesse = 50  # Départ en arrêt (50%)
print("Utilise 'Z' pour augmenter la vitesse et 'S' pour la réduire. Appuie sur 'Q' pour quitter.")

try:
    while True:
        # Vérifie si une touche est pressée
        if keyboard.is_pressed('z'):  # Augmente la vitesse
            if servoVitesse < 60:  # Limite maximale
                servoVitesse += 1
                print(f"Vitesse augmentée : {servoVitesse}%")
                p.ChangeDutyCycle(servoVitesse)
            time.sleep(0.1)  # Petit délai pour éviter d'aller trop vite

        elif keyboard.is_pressed('s'):  # Diminue la vitesse
            if servoVitesse > 40:  # Limite minimale
                servoVitesse -= 1
                print(f"Vitesse réduite : {servoVitesse}%")
                p.ChangeDutyCycle(servoVitesse)
            time.sleep(0.1)  

        elif keyboard.is_pressed('q'):  # Quitte proprement avec 'Q'
            print("Arrêt du programme.")
            break

finally:
    p.stop()
    GPIO.cleanup()
