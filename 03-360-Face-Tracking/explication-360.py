import RPi.GPIO as GPIO  #General Purpose Input/Output
from time import sleep  
GPIO.setmode(GPIO.BOARD) # Permet d'utiliser la numérotation physique des pins

GPIO.setup(11,GPIO.OUT)  # Setup le pin 11 (GPIO17) comme point sortie (OUT pour OUTPUT) 
                         # OUT permet la sortie d'information (ici la rotation demandée)
                         # IN permet l'entrée d'information (l'appuye sur un bouton)

p = GPIO.PWM(11, 330)     # Setup le pin 11 comme un signal PWM (Pulse Width Modulation / le cable de controle) avec une puissance de 330 Hz

# Pour faire une rotation il y a deux choses importantes
# PWM (Pulse Width Modulation) et Duty Cycle
# Le PWM envoie un signal vers le moteur qui dure 20ms (50Hz) et ce signal est bas 
# Le servo va traduire le temps de signal haut (Duty Cycle) en position
# Donc avec un Duty Cycle à 3%, cela voudra dire que 3% du signal venant du PWM soit (0.6ms), est un signal HAUT donc le moteur va tourner vers sa position initiale.
# Au contraire, avec un Duty Cycle à 12%, le moteur fera une rotation de 180 degré 

print("Debut")
p.start(50)  # Démarrage à l'arrêt

print("Rotation horaire")
p.ChangeDutyCycle(45)  # Tourne dans un sens
sleep(2)

print("Arrêt")
p.ChangeDutyCycle(50)  # Arrêt
sleep(1)

print("Rotation antihoraire")
p.ChangeDutyCycle(55)  # Tourne dans l’autre sens
sleep(2)

print("Fin")
p.ChangeDutyCycle(50)  # Arrêt
sleep(1)

p.stop()                 # On coupe le signal PWM
GPIO.cleanup()           # On nettoie et libere la ressource du pin