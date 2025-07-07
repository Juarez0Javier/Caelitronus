
import pygame

clock = pygame.time.Clock()
clock.tick(30)

pygame.init()

import random

import Characters
import Battle

WIDTH, HEIGHT = 920, 750

#Angel Randomizer Chances

ANGRND = [["HealManifest",3], ["DrainManifest",3], ["LazManifest",1]]


class Level:

    def __init__(self, M1, diff, stage):

        self._M1 = M1
        self.diff = diff
        self.stage = stage
    
        pass

    def runLvSq (self):

        #Cutscene de Inicio de Seccion

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Caelitronus")

        LvSq = [[self.AngeRand(), 1 + self.diff],[self.AngeRand(), 1 + self.diff], [self.stage + "BossManifest", 3 + self.diff]]

        for Enemy in LvSq:
            M2 = getattr(Characters,Enemy[0])(Enemy[1])


            self._M1.set_opp(M2)
            M2.set_opp(self._M1)

            battleScreen = Battle.Battle(self._M1, M2, screen)

            run = True

            while run:
                run = battleScreen.doBattle()
                pygame.display.flip()

            if self._M1.get_hp() == 0:
                #Pantalla de Perdida
                return False
                break
            else:
                run = True
                #Pantalla de Siguiente o Subida de Nivel
                self._M1.set_hp(self._M1.get_maxHp())
        
        #Cutscene de Final de Seccion
        
    def AngeRand(self):

        AngL = []

        for Ang in ANGRND:
            for i in range(Ang[1]):
                AngL.append(Ang[0])

        random.shuffle(AngL)

        return AngL[0]

MainC = Characters.AtkDmnManifest(1)

LV1 = Level(MainC,0,"Spn")

LV1.runLvSq()