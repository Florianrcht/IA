# servo_server.py

import RPi.GPIO as GPIO  
import asyncio
import threading
from flask import Flask

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.OUT)  

p = GPIO.PWM(11, 330)  
p.start(50)  # 50% = STOP

servoControl = True
servoVitesse = 50  # Départ en arrêt (50%)

# Cette boucle tourne tant que servoControl est True
async def looper():
    global servoControl

    while servoControl:
        p.ChangeDutyCycle(servoVitesse)
        print(servoVitesse)
        await asyncio.sleep(0.1)

    print("Arreté")
    p.ChangeDutyCycle(50)  

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

@app.route('/speedUp')
def speed_up():
    servoVitesse = servoVitesse + 1
    print("vitesse +")
    return "vitesse +"

if __name__ == '__main__':
    thread = threading.Thread(target=start_async_loop)
    thread.start()

    app.run(host="0.0.0.0", port=5000)
