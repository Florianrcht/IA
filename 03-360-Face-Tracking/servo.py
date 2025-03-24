import RPi.GPIO as GPIO  #General Purpose Input/Output
from time import sleep  
GPIO.setmode(GPIO.BOARD) # Permet d'utiliser la numérotation physique des pins

GPIO.setup(11,GPIO.OUT)  # Setup le pin 11 (GPIO17) comme point sortie (OUT pour OUTPUT) 
                         # OUT permet la sortie d'information (ici la rotation demandée)
                         # IN permet l'entrée d'information (l'appuye sur un bouton)

p = GPIO.PWM(11, 50)     # Setup le pin 11 comme un signal PWM (Pulse Width Modulation / le cable de controle) avec une puissance de 50 Hz

p.start(0)               # Starts running PWM on the pin and sets it to 0

# Move the servo back and forth
p.ChangeDutyCycle(3)     # Changes the pulse width to 3 (so moves the servo)
sleep(1)                 # Wait 1 second
p.ChangeDutyCycle(15)    # Changes the pulse width to 12 (so moves the servo)
sleep(1)

# Clean up everything
p.stop()                 # At the end of the program, stop the PWM
GPIO.cleanup()   