import RPi.GPIO as GPIO  
import asyncio

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.OUT)  

p = GPIO.PWM(11, 330)  
p.start(50)  # 50% = STOP

servoVitesse = 51  # Départ en arrêt (50%)

async def looper():
    while True:
        p.ChangeDutyCycle(servoVitesse)

async def main():
    await asyncio.sleep(5)
    print("main")
    future = asyncio.ensure_future(looper())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())