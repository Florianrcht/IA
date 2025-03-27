from pynput import keyboard

# Cette fonction sera appelée quand une touche est pressée
def on_press(key):
    try:
        if key.char == 'z':  # Si la touche 'z' est pressée, augmente la vitesse
            print("Vitesse augmentée")
        elif key.char == 's':  # Si la touche 's' est pressée, réduit la vitesse
            print("Vitesse réduite")
        elif key.char == 'q':  # Si la touche 'q' est pressée, quitte le programme
            print("Quitter")
            return False  # Cela arrête l'écoute du clavier
    except AttributeError:
        # Ignore les touches spéciales (comme les touches SHIFT, CTRL, etc.)
        pass

# Crée une instance de listener pour écouter les touches du clavier
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # Attends que l'utilisateur appuie sur une touche
