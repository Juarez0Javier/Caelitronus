#
#   Esto lo dejo por ahora por si rompo algo así tengo la versión funcional, pero va a quedar fuera
#
#   El nuevo Battle es la clase Battle.py
#
#   En run .py hay un ejemplo de como se lanza una batalla
#

from asyncio import wait_for
from time import sleep

import pygame
import random as rnd

from pygame.examples.go_over_there import MIN_SPEED

import Characters



pygame.init()

battle1_path = "../Sound/Music/Battle1.wav"

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prueba de Ticks")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 16)
textos = []

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

MIN_SPEED = 5

tiempoEvent1 = 0
tiempoEvent2 = 0

vida1 = 100
vida2 = 100
velocidad1 = 2.5
velocidad2 = 3

# def calcularCritico(danio):
#     if (rnd.randint(0, 5) == 5):
#         danioNuevo = [danio * 2, "CRITICO"]
#     else:
#         danioNuevo = [danio, ""]
#     return danioNuevo

#####################################

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
    "Name": "Espina",
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

M1.set_opp(M2)
M2.set_opp(M1)

i = 0
while M1.get_hp() > 0 and M2.get_hp() > 0:
    print("##################################")
    print(M1.act())
    print("----------------------------------")
    print(M2.act())
    print("----------------------------------")
    print(M1.get_name() + " le queda " + str(M1.get_hp()) + " de vida.")
    print(M2.get_name() + " le queda " + str(M2.get_hp()) + " de vida.")
    i+=1
print("Turnos Totales: " + str(i))
#####################################
M1.set_hp(M1.get_maxHp())
M2.set_hp(M2.get_maxHp())

img1_imp = pygame.image.load(M1.get_sprite())
img2_imp = pygame.image.load(M2.get_sprite())

pygame.mixer.music.load(battle1_path)
pygame.mixer.music.play()
#####################################

img1 = pygame.transform.scale(img1_imp, (img1_imp.get_width() / 4, img1_imp.get_height() / 4))
img2 = pygame.transform.scale(img2_imp, (img2_imp.get_width() / 4, img2_imp.get_height() / 4))


run = True
while run:

    # screen.fill(WHITE)
    #
    # pygame.draw.rect(screen, RED, pygame.Rect(WIDTH - 250, 100, M1.get_maxHp() * 3, 15))
    # pygame.draw.rect(screen, GREEN, pygame.Rect(WIDTH - 250, 100, M1.get_hp() * 3, 15))
    #
    # pygame.draw.rect(screen, RED, pygame.Rect(50, 100, M2.get_maxHp() * 3, 15))
    # pygame.draw.rect(screen, GREEN, pygame.Rect(50, 100, M2.get_hp() * 3, 15))

    # vida1 = max(0, vida1 - 0.3)
    # vida2 = max(0, vida2 - 0.2)

    # print(vida1)
    # print(vida2)

    # print(pygame.time.get_ticks()/1000)

    if pygame.time.get_ticks()/1000 >= tiempoEvent1 + (MIN_SPEED - (M1.get_spd() * 0.5)):
        btlMsg1 = str(M1.act())
        tiempoEvent1 = pygame.time.get_ticks()/1000
        print("Ataque de PJ 1")
        #textos.append(font.render(f"PJ 1 ataca con Daño {danioNuevo[0]} {danioNuevo[1]}", True, BLACK))
        textos.append(font.render(f"PJ 1: {btlMsg1}", True, BLACK))
        #textos.append(font.render("PJ 1 ataca", True, BLACK))

    if pygame.time.get_ticks()/1000 >= tiempoEvent2 + (MIN_SPEED - (M2.get_spd() * 0.5)):
        btlMsg2 = str(M2.act())
        tiempoEvent2 = pygame.time.get_ticks()/1000
        print("Ataque de PJ 2")
        #textos.append(font.render(f"PJ 2 ataca con Daño {danioNuevo[0]} {danioNuevo[1]}", True, BLACK))
        textos.append(font.render(f"PJ 2: {btlMsg2}", True, BLACK))
        #textos.append(font.render("PJ 2 ataca", True, BLACK))

##############

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, pygame.Rect(WIDTH - 250, 100, M1.get_maxHp() * 3, 15))
    pygame.draw.rect(screen, GREEN, pygame.Rect(WIDTH - 250, 100, M1.get_hp() * 3, 15))

    pygame.draw.rect(screen, RED, pygame.Rect(50, 100, M2.get_maxHp() * 3, 15))
    pygame.draw.rect(screen, GREEN, pygame.Rect(50, 100, M2.get_hp() * 3, 15))

##############

    if len(textos) > 6:
        textos.remove(textos[0])

    for i, texto in enumerate(textos):
        if texto.get_alpha() > 1:
            screen.blit(texto, (260, 50 + i * 80))


    screen.blit(img1, (20, 200))
    screen.blit(pygame.transform.flip(img2, True, False), (screen.get_width() - (img1.get_width() + 20), 200))
    #screen.blit(img2, (screen.get_width() - (img1.get_width() + 20), 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(30)

    if M1.get_hp() <= 0 or M2.get_hp() <= 0:
        run = False

    if run == False:
        pygame.mixer.music.fadeout(1000)
        sleep(3)

pygame.quit()