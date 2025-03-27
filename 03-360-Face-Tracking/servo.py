from pynput import keyboard

def on_press(key):
    try:
        if key.char == 'z':
            print("Vitesse augmentée")
        elif key.char == 's':
            print("Vitesse réduite")
        elif key.char == 'q':
            print("Quitter")
            return False
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

while listener.running:
    pass
