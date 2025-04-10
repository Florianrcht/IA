import RPi.GPIO as GPIO  
import time  
import keyboard  # Permet de détecter les touches du clavier

# Configuration GPIO
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.OUT)  

# Configuration du signal PWM
p = GPIO.PWM(11, 330)  # Fréquence 330 Hz pour un servo à rotation continue
p.start(50)  # 50% = STOP

servoVitesse = 51  # Départ en arrêt (50%)

try:
    while True:
        print("depart : 50")
        p.ChangeDutyCycle(servoVitesse)


finally:
    p.stop()
    GPIO.cleanup()
