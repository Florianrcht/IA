import requests
import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))

try:
    done = False
    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("pressed w")
                if event.key == pygame.K_s:
                    print("pressed s")
                    
    response = requests.get('http://localhost:5000/speed')
    print(response.text)
except Exception as e:
    print(f"Erreur lors de la requête : {e}")
