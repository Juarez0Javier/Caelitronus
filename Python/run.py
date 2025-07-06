from asyncio import wait_for
from time import sleep
import pygame
import os

pygame.init()
clock = pygame.time.Clock()
clock.tick(30)
import random as rnd
import Characters
import Battle


# Seteo valores de la screen

battle1_path = r"Assets\Music\Testy1.wav"

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prueba de Batalla")
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


## Corroboracion del Directorio Activio (Esto es importante por otra razón)
print (os.getcwd())

M1 = Characters.AtkDmnManifest(1)
M2 = Characters.HealManifest(1)

M1.set_opp(M2)
M2.set_opp(M1)

# Creamos una nueva batalla

battleScreen = Battle.Battle(M1, M2, screen)

pygame.mixer.music.load(battle1_path)
pygame.mixer.music.play()

run = True

while run:
    run = battleScreen.doBattle()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()