import RPi.GPIO as GPIO  
import asyncio
import threading
from flask import Flask

def servo_function():
    app = Flask(__name__)

    GPIO.setmode(GPIO.BOARD)  
    GPIO.setup(11, GPIO.OUT)  

    p = GPIO.PWM(11, 330)  
    p.start(50)

    state = {
        "servoControl": True,
        "servoVitesse": 0
    }

    async def looper():
        while state["servoControl"]:
            p.ChangeDutyCycle(state["servoVitesse"])
            print("Vitesse:", state["servoVitesse"])
            state["servoVitesse"] = int(46)
            await asyncio.sleep(1)


        p.stop()                 
        GPIO.cleanup()
        print("Servo arrêté et GPIO nettoyé")

    def start_async_loop():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(looper())

    @app.route('/stop')
    def stop():
        state["servoControl"] = False
        print("Commande reçue : STOP")
        return "Servo arrêté"

    @app.route('/speed/<servoVitesseRequest>')
    def speed(servoVitesseRequest):
        try:
            state["servoVitesse"] = int(servoVitesseRequest)
            print("Commande reçue : vitesse =", state["servoVitesse"])
            return f"Vitesse mise à jour : {state['servoVitesse']}"
        except ValueError:
            return "Erreur : la vitesse doit être un entier."

    # Lancer la boucle asynchrone dans un thread
    thread = threading.Thread(target=start_async_loop)
    thread.start()

    # Lancer le serveur Flask
    app.run(host="0.0.0.0", port=5000)
