import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servo_pin = 1  # Choisir la broche GPIO (ici GPIO 17)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz pour le signal PWM
pwm.start(0)

# Déplacer le servo
try:
    while True:
        # Tourner à 0° (basse vitesse)
        pwm.ChangeDutyCycle(2.5)
        time.sleep(1)
        # Tourner à 90° (milieu)
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)
        # Tourner à 180° (haute vitesse)
        pwm.ChangeDutyCycle(12.5)
        time.sleep(1)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
