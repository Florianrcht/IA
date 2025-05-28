import requests

try:
    print("vitesse en int")
    # 10 - 45 => gauche 
    # 46 - 49 (0) => stop ?
    # 50 - 86 => droite
    
    x = input()
    response = requests.get('http://localhost:5000/speed/'+x)
    print(response.text)
except Exception as e:
    print(f"Erreur lors de la requête : {e}")
