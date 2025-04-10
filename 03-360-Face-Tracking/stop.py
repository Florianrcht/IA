# stop.py

import requests

try:
    response = requests.get('http://localhost:5000/stop')
    print(response.text)
except Exception as e:
    print(f"Erreur lors de la requête : {e}")
