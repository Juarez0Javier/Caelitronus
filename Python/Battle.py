from time import sleep

import pygame
import random as rnd

##from pygame.examples.go_over_there import MIN_SPEED

import Characters

battle1_path = "../Sound/Music/Battle1.wav"

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Prueba de Ticks")

# clock = pygame.time.Clock()
font = pygame.font.Font(None, 16)
fontStats = pygame.font.Font(None, 30)
textos = []

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

MIN_SPEED = 5


class Battle:
    def __init__(self, battler1: Characters, battler2: Characters, screen):

        #Recibe los combatientes
        self._battler1 = battler1
        self._battler2 = battler2

        self._screen = screen

        self._tiempoEvent1 = pygame.time.get_ticks()/1000
        self._tiempoEvent2 = pygame.time.get_ticks()/1000

        #Se obtiene la imagen original del battler
        self._img1_imp = pygame.image.load(battler1.get_sprite())
        self._img2_imp = pygame.image.load(battler2.get_sprite())

        #Se resizea para que tenga el tamaño correcto
        self._imagen1 = pygame.transform.scale(self._img1_imp, (self._img1_imp.get_width() / 2, self._img1_imp.get_height() / 2))
        self._imagen2 = pygame.transform.scale(self._img2_imp, (self._img2_imp.get_width() / 2, self._img2_imp.get_height() / 2))

    def get_battler1(self):
        return self._battler1
    def get_battler2(self):
        return self._battler2
    
    def get_tiempoEvent1(self):
        return self._tiempoEvent1
    def get_tiempoEvent2(self):
        return self._tiempoEvent2
    
    def get_imagen1(self):
        return self._imagen1
    def get_imagen2(self):
        return self._imagen2
    
    def get_screen(self):
        return self._screen

    def set_tiempoEvent1(self, tiempoEvent1):
        self._tiempoEvent1 = tiempoEvent1
    def set_tiempoEvent2(self, tiempoEvent2):
        self._tiempoEvent2 = tiempoEvent2

    def printStats(self, battler: Characters):
        stat = "ATQ: " + str(battler.get_atk()) + "  DAN:" + str(battler.get_atkDmg()) + "  VLC:" + str(battler.get_spd())
        stat += "\nDEF: " + str(battler.get_defn()) + "  ESQ:" + str(battler.get_evd()) + "  SRT:" + str(battler.get_luck())

        return stat

    def doBattle(self):

        if pygame.time.get_ticks() / 1000 >= self.get_tiempoEvent1() + (MIN_SPEED - (self.get_battler1().get_spd() * 0.5 * 0.1)):

            btlMsg1 = str(self.get_battler1().act())

            self.set_tiempoEvent1(pygame.time.get_ticks() / 1000)

            print("Ataque de PJ 1" + btlMsg1)

            # Prueba de checks

            print(str(pygame.time.get_ticks() / 1000) + " - " + str(self.get_tiempoEvent1()))

            # textos.append(font.render(f"PJ 1 ataca con Daño {danioNuevo[0]} {danioNuevo[1]}", True, BLACK))

            textos.append(font.render(f"PJ 1: {btlMsg1}", True, BLACK, None, 256))

            # textos.append(font.render("PJ 1 ataca", True, BLACK))

        if pygame.time.get_ticks() / 1000 >= self.get_tiempoEvent2() + (MIN_SPEED - (self.get_battler2().get_spd() * 0.5 * 0.1)):
            
            btlMsg2 = str(self.get_battler2().act())

            self.set_tiempoEvent2(pygame.time.get_ticks() / 1000)

            print("Ataque de PJ 2" + btlMsg2)

            # textos.append(font.render(f"PJ 2 ataca con Daño {danioNuevo[0]} {danioNuevo[1]}", True, BLACK))
           
            textos.append(font.render(f"PJ 2: {btlMsg2}", True, BLACK, None, 256))
            
            # textos.append(font.render("PJ 2 ataca", True, BLACK))

        ##############

        self.get_screen().fill(WHITE)

        pygame.draw.rect(self.get_screen(), RED, pygame.Rect(self.get_screen().get_width() - 250, 100, self.get_battler2().get_maxHp(), 15))
        pygame.draw.rect(self.get_screen(), GREEN, pygame.Rect(self.get_screen().get_width() - 250, 100, self.get_battler2().get_hp(), 15))

        pygame.draw.rect(self.get_screen(), RED, pygame.Rect(50, 100, self.get_battler1().get_maxHp(), 15))
        pygame.draw.rect(self.get_screen(), GREEN, pygame.Rect(50, 100, self.get_battler1().get_hp(), 15))

        ##############
        ############## Dibujar Stats

        HUD1 = fontStats.render(self.printStats(self.get_battler1()), True, BLACK)
        HUD2 = fontStats.render(self.printStats(self.get_battler2()), True, BLACK)

        self.get_screen().blit(HUD1, (50, 600))
        self.get_screen().blit(HUD2, (670, 600))

        ################
        if len(textos) > 7:
            textos.remove(textos[0])

        for i, texto in enumerate(textos):
            if texto.get_alpha() > 1:
                self.get_screen().blit(texto, (300, 50 + i * 80))

        self.get_screen().blit(self.get_imagen1(), (0, 200))
        self.get_screen().blit(pygame.transform.flip(self.get_imagen2(), True, False), (self.get_screen().get_width() - (self.get_imagen2().get_width() + 20), 200))

        # screen.blit(img2, (screen.get_width() - (img1.get_width() + 20), 200))

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False

        # pygame.display.flip()
        # clock.tick(30)
        pygame.display.flip()
        if self.get_battler1().get_hp() <= 0 or self.get_battler2().get_hp() <= 0:
            pygame.mixer.music.fadeout(1000)
            sleep(3)
            return False

        return True

