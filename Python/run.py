import pygame
import os

pygame.init()
clock = pygame.time.Clock()
clock.tick(30)

import Characters
import Levels
import LvlSelect


# Seteo valores de la screen

battle1_path = r"Assets\Music\Testy1.wav"

WIDTH, HEIGHT = 920, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prueba de Batalla")
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


## Corroboracion del Directorio Activio (Esto es importante por otra razón)
print (os.getcwd())

M1 = Characters.AtkDmnManifest(1)

pygame.mixer.music.load(battle1_path)
pygame.mixer.music.play()

#Definimos un Nuevo Nivel

LVS = [Levels.Level(M1,0,"Spn"), Levels.Level(M1,0,"Fn"), Levels.Level(M1,0,"Pss"), Levels.Level(M1,0,"Spn")]

run = True

while run:

    #Run Opening Cinematic

    #Run Main Menu

    #Run Character Select

    #While Run Stage Select

    LVS[0].runLvSq()
        
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()