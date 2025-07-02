from asyncio import wait_for
from time import sleep
import pygame

pygame.init()
clock = pygame.time.Clock()
clock.tick(30)
import random as rnd
import Characters
import Battle


# Seteo valores de la screen

battle1_path = "../Sound/Music/Battle1.wav"

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prueba de Batalla")
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Seteamos Stats de los personajes y los asignamos

'''
M1Dicc = {
    "Name": "Angel Bueno",
    "Sprite": "../diseños/enemigos/monaquillos/alma normal/mininormal.png",
    "Level": 1,
    "Exp": 0,
    "Health": 20,
    "Defense": 0,
    "Evade": 0,
    "Attack": 4,
    "Damage": 2,
    "Speed": 1,
    "Luck": 5,
    "Opponent": None
}

M2Dicc = {
    "Name": "PEPE",
    "Sprite": "../diseños/enemigos/monaquillos/alma oscuro/minicorupto.png",
    "Level": 1,
    "Exp": 0,
    "Health": 30,
    "Defense": 0,
    "Evade": 0,
    "Attack": 1,
    "Damage": 3,
    "Speed": 6,
    "Luck": 2,
    "Opponent": None
}

M1 = Characters.HealManifest(*list(M1Dicc.values()))
M2 = Characters.SpnBossManifest(*list(M2Dicc.values()))
'''

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