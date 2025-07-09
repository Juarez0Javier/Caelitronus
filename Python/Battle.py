from time import sleep

import pygame
import random as rnd

from PIL.ImageChops import offset

##from pygame.examples.go_over_there import MIN_SPEED

import Characters

battle1_path = "../Sound/Music/Battle1.wav"

# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Prueba de Ticks")
fontPath = None
# clock = pygame.time.Clock()
font = pygame.font.Font(fontPath, 16)
fontStats = pygame.font.Font(fontPath, 30)
textos = []

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (127, 127, 127)
PURPLE = (127, 0, 127)
TOPY = 50

offset1 = 0
offset2 = 0

MIN_SPEED = 5


class Battle:
    def __init__(self, battler1: Characters, battler2: Characters, screen):

        #Recibe los combatientes
        self._battler1 = battler1
        self._battler2 = battler2

        self._screen = screen

        self._tiempoEvent1 = pygame.time.get_ticks()/1000
        self._tiempoEvent2 = pygame.time.get_ticks()/1000

        self._tiempoBuff1 = 0
        self._tiempoBuff2 = 0

        self._offset1 = 0
        self._offset2 = 0

        self._battleEnd = False

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

    def get_tiempoBuff1(self):
        return self._tiempoBuff1
    def get_tiempoBuff2(self):
        return self._tiempoBuff2

    def set_tiempoEvent1(self, tiempoEvent1):
        self._tiempoEvent1 = tiempoEvent1
    def set_tiempoEvent2(self, tiempoEvent2):
        self._tiempoEvent2 = tiempoEvent2

    def set_tiempoBuff1(self, tiempoBuff1):
        self._tiempoBuff1 = tiempoBuff1
    def set_tiempoBuff2(self, tiempoBuff2):
        self._tiempoBuff2 = tiempoBuff2

    def printStats(self, battler: Characters):
        stat = "ATQ: " + str(battler.get_atk()) + "  DAN:" + str(battler.get_atkDmg()) + "  VLC:" + str(battler.get_spd())
        stat += "\nDEF: " + str(battler.get_defn()) + "  ESQ:" + str(battler.get_evd()) + "  SRT:" + str(battler.get_luck())

        return stat

    def doBattle(self):


        actualTick = pygame.time.get_ticks() / 1000

        if not self._battleEnd:

            if actualTick >= self.get_tiempoEvent1() + (MIN_SPEED - (self.get_battler1().get_spd() * 0.5 * 0.1)):

                btlMsg1 = str(self.get_battler1().act())

                #self._offset2 = 30

                self.set_tiempoEvent1(pygame.time.get_ticks() / 1000)

                print("Ataque de PJ 1" + btlMsg1)

                # Prueba de checks

                print(str(actualTick) + " - " + str(self.get_tiempoEvent1()))

                textos.append(font.render(f"PJ 1: {btlMsg1}", True, BLACK, None, 256))

                if self.get_battler2().get_hp() <= 0:
                    expGainMsg = self.get_battler1().xpUp(5)
                    textos.append(font.render(f"PJ 1: {expGainMsg}", True, BLACK, None, 256))

                # textos.append(font.render("PJ 1 ataca", True, BLACK))

            if actualTick >= self.get_tiempoEvent2() + (MIN_SPEED - (self.get_battler2().get_spd() * 0.5 * 0.1)) and self.get_battler2().get_hp() > 0:

                btlMsg2 = str(self.get_battler2().act())

                self.set_tiempoEvent2(actualTick)

                print("Ataque de PJ 2" + btlMsg2)

                # textos.append(font.render(f"PJ 2 ataca con Daño {danioNuevo[0]} {danioNuevo[1]}", True, BLACK))

                textos.append(font.render(f"PJ 2: {btlMsg2}", True, BLACK, None, 256))

                # textos.append(font.render("PJ 2 ataca", True, BLACK))

            if self.get_battler1().get_actvBuff()[1] and self.get_tiempoBuff1() == 0:
                self.set_tiempoBuff1(actualTick)
                print("Ataque actual con buff: " + str(self.get_battler1().get_atk()) + "\n" + str(self.get_tiempoBuff1()) + " - " + str(self.get_tiempoBuff1() + self.get_battler1().get_actvBuff()[0]))

            if self.get_battler1().get_actvBuff()[1] and actualTick >= self.get_tiempoBuff1() + self.get_battler1().get_actvBuff()[0]:
                endBuffmsg = self.get_battler1().endBuff()
                textos.append(font.render(f"PJ 1: {endBuffmsg}", True, BLACK, None, 256))
                self.set_tiempoBuff1(0)
                print("Ataque actual sin buff: " + str(self.get_battler1().get_atk()))

            if self.get_battler2().get_actvBuff()[1] and self.get_tiempoBuff1() == 0:
                self.set_tiempoBuff2(actualTick)
                print("Ataque actual con buff: " + str(self.get_battler1().get_atk()) + "\n" + str(self.get_tiempoBuff2()) + " - " + str(self.get_tiempoBuff2() + self.get_battler2().get_actvBuff()[0]))

            if self.get_battler2().get_actvBuff()[1] and actualTick >= self.get_tiempoBuff1() + self.get_battler2().get_actvBuff()[0]:
                endBuffmsg = self.get_battler2().endBuff()
                textos.append(font.render(f"PJ 2: {endBuffmsg}", True, BLACK, None, 256))
                self.set_tiempoBuff2(0)
                print("Ataque actual sin buff: " + str(self.get_battler2().get_atk()))

        ##############

        #Calcular offset

        # if self._offset2 > 0:
        #     offset_x2 = rnd.randint(-10, 10)
        #     offset_y2 = rnd.randint(-10, 10)
        #     self._offset2 -= 1
        # else:
        #     offset_x2 = 0
        #     offset_y2 = 0


        ##############
        self.get_screen().fill(WHITE)

        pygame.draw.rect(self.get_screen(), RED, pygame.Rect(self.get_screen().get_width() - 300, TOPY + 25, self.get_battler2().get_maxHp(), 15))
        pygame.draw.rect(self.get_screen(), GREEN, pygame.Rect(self.get_screen().get_width() - 300, TOPY + 25, self.get_battler2().get_hp(), 15))

        pygame.draw.rect(self.get_screen(), RED, pygame.Rect(25, TOPY + 25, self.get_battler1().get_maxHp(), 15))
        pygame.draw.rect(self.get_screen(), GREEN, pygame.Rect(25, TOPY + 25, self.get_battler1().get_hp(), 15))

        ##############
        ############## Dibujar Stats

        HUD1 = fontStats.render(self.printStats(self.get_battler1()), True, BLACK)
        HUD2 = fontStats.render(self.printStats(self.get_battler2()), True, BLACK)

        LIFE1 = fontStats.render(str(self.get_battler1().get_hp()) + "/" + str(self.get_battler1().get_maxHp()), True, BLACK)
        LIFE2 = fontStats.render(str(self.get_battler2().get_hp()) + "/" + str(self.get_battler2().get_maxHp()), True, BLACK)

        self.get_screen().blit(LIFE1, (25, TOPY))
        self.get_screen().blit(LIFE2, (self.get_screen().get_width() - 300, TOPY))

        self.get_screen().blit(HUD1, (25, 600))
        self.get_screen().blit(HUD2, (self.get_screen().get_width() - 300, 600))

        ################

        ################
        while len(textos) > 7:
            textos.remove(textos[0])

        for i, texto in enumerate(textos):
            if texto.get_alpha() > 1:
                self.get_screen().blit(texto, (300, TOPY + i * 80))

        self.get_screen().blit(self.get_imagen1(), (0, TOPY + 75))
        self.get_screen().blit(pygame.transform.flip(self.get_imagen2(), True, False), (self.get_screen().get_width() - (self.get_imagen2().get_width() + 20), TOPY + 75))

        # self.get_screen().blit(self.get_imagen1(), (0, TOPY + 75))
        # self.get_screen().blit(pygame.transform.flip(self.get_imagen2(), True, False), (self.get_screen().get_width() - (self.get_imagen2().get_width() + 20 + offset_x2), TOPY + 75 + offset_y2))

        if self.get_battler1().get_hp() <= 0 or self.get_battler2().get_hp() <= 0 and not self._battleEnd:
            pygame.mixer.music.fadeout(1000)
            
            return False
            sleep(1)
            self._battleEnd = True

        '''    
        if self._battleEnd:
            boton_rect1 = pygame.Rect(300, 600, 120, 75)
            boton_rect2 = pygame.Rect(430, 600, 120, 75)
            fuenteBoton = pygame.font.SysFont(None, 16)
            textoBoton = fuenteBoton.render("SUBIR DE NIVEL", True, WHITE, None, 120)  # Texto blanco
            texto_rect = textoBoton.get_rect(center=boton_rect1.center)
            if self.get_battler1().checkXp():
                pygame.draw.rect(self.get_screen(), GREY, boton_rect1)
            self.get_screen().blit(textoBoton, texto_rect)
            textoBoton2 = fuenteBoton.render("SIGUIENTE BATALLA", True, WHITE, None, 120)  # Texto blanco
            texto_rect2 = textoBoton2.get_rect(center=boton_rect2.center)
            pygame.draw.rect(self.get_screen(), GREY, boton_rect2)
            self.get_screen().blit(textoBoton2, texto_rect2)

            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.get_battler1().checkXp():
                        if boton_rect1.collidepoint(evento.pos):
                            print("¡Botón Subir de Nivel!")
                    if boton_rect2.collidepoint(evento.pos):
                        print("¡Botón Continuar!")
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.flip()
        return True

