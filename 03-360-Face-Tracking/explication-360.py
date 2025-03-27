from pynput import keyboard
import RPi.GPIO as GPIO
from time import sleep

# Configuration GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 330)  # Servo à 330 Hz
p.start(50)  # Démarrage en position neutre

vitesse = 50  # Valeur initiale du Duty Cycle

def on_press(key):
    global vitesse
    try:
        if key.char == 'z':  # Augmente la vitesse
            vitesse = min(100, vitesse + 1)
        elif key.char == 's':  # Réduit la vitesse
            vitesse = max(0, vitesse - 1)
        elif key.char == 'q':  # Quitte le programme
            print("\nArrêt du programme.")
            p.stop()
            GPIO.cleanup()
            return False  # Arrête l'écouteur

        print(f"Nouvelle vitesse : {vitesse}%")
        p.ChangeDutyCycle(vitesse)

    except AttributeError:
        pass  # Ignore d'autres touches

print("Utilise 'Z' pour augmenter la vitesse et 'S' pour la réduire. Appuie sur 'Q' pour quitter.")

# Démarrage de l'écoute du clavier
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # Bloque le programme ici et écoute le clavier
