import requests

def go_left():
    try:
        response = requests.get('http://localhost:5000/left')
        print(response.text)
    except Exception as e:
        print(f"Erreur lors de la requête : {e}")

def go_right():
    try:
        response = requests.get('http://localhost:5000/right')
        print(response.text)
    except Exception as e:
        print(f"Erreur lors de la requête : {e}")