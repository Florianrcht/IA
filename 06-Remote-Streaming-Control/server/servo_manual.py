import RPi.GPIO as GPIO  
from flask import Flask
import time

def servo_manual_function():
    app = Flask(__name__)

    GPIO.setmode(GPIO.BOARD)  
    GPIO.setup(11, GPIO.OUT)  

    p = GPIO.PWM(11, 50)  
    p.start(0)

    state = {
        "servoControl": True,
        "servoVitesse": 0
    }

    @app.route('/kill')
    def kill():
        state["servoControl"] = False
        print("Commande reçue : FIN")
        p.stop()                 
        GPIO.cleanup()
        print("Servo arrêté et GPIO nettoyé")
        return "Servo arrêté"

    @app.route('/speed/<servoVitesseRequest>')
    def speed(servoVitesseRequest):
        try:
            state["servoVitesse"] = int(servoVitesseRequest)
            print("Commande reçue : vitesse =", state["servoVitesse"])
            p.ChangeDutyCycle(state["servoVitesse"])
            time.sleep(1)
            p.ChangeDutyCycle(0)
            return f"Vitesse mise à jour : {state['servoVitesse']}"
        except ValueError:
            return "Erreur : la vitesse doit être un entier."

    # Lancer le serveur Flask
    app.run(host="0.0.0.0", port=5000)
