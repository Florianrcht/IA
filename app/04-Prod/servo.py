import RPi.GPIO as GPIO  
import asyncio
import threading
from flask import Flask

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.OUT)  

p = GPIO.PWM(11, 330)  
p.start(50) 

servoControl = True
servoVitesse = 0  

async def looper():
    global servoControl
    global servoVitesse

    while servoControl:
        p.ChangeDutyCycle(servoVitesse)
        print(servoVitesse)
        await asyncio.sleep(1)

    p.stop()                 
    GPIO.cleanup()
    print("Arreté")

def start_async_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(looper())

@app.route('/stop')
def stop():
    global servoControl
    servoControl = False
    print("Servo arrêté.")
    return "Servo arrêté"

@app.route('/speed/<servoVitesseRequest>')
def speed(servoVitesseRequest):
    global servoVitesse
    try:
        servoVitesse = int(servoVitesseRequest)
        print("Requête /speed reçue. Nouvelle vitesse :", servoVitesse)
        return f"Vitesse mise à jour : {servoVitesse}"
    except ValueError:
        return "Erreur : la vitesse doit être un entier."

if __name__ == '__main__':
    thread = threading.Thread(target=start_async_loop)
    thread.start()

    app.run(host="0.0.0.0", port=5000)
