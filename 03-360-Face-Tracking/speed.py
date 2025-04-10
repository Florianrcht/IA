import requests

try:
    x = input()
    response = requests.get('http://localhost:5000/speed/'+x)
    print(response.text)
except Exception as e:
    print(f"Erreur lors de la requête : {e}")
