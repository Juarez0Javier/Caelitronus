
import pygame

#clock = pygame.time.Clock()
#clock.tick(30)

pygame.init()

import random

import Characters as Ch
import Battle as Btl
import Menus as Mns

WIDTH, HEIGHT = 920, 750

#Angel Randomizer Chances

ANGRND = [["HealManifest",4],["DrainManifest",3], ["LazManifest",1]]


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
            
            M2 = getattr(Ch,Enemy[0])(Enemy[1])
            self._M1.set_opp(M2)
            M2.set_opp(self._M1)

            # Creamos una nueva batalla
            battleScreen = Btl.Battle(self._M1, M2, screen)

            run = True

            while run:
                run = battleScreen.doBattle()
                #pygame.display.flip()

            if self._M1.get_hp() == 0:
                #Pantalla de Perdida
                LostMenu = Mns.LScreen(screen)
                return LostMenu.runMenu()
            else:
                #Pantalla de Siguiente o Subida de Nivel
                WinMenu = Mns.WScreen(screen)
                run = WinMenu.runMenu()
                while run:
                    LvUpMenu = Mns.LvUpScreen(screen,self._M1)
                    LvUpMenu.runMenu()
                    run = WinMenu.runMenu()

            self._M1.set_hp(self._M1.get_maxHp())
        
        #Cutscene de Final de Seccion

        run = FinalMenu = Mns.GWScreen(screen)
        #while run


        return True
        
    def AngeRand(self):

        AngL = []

        for Ang in ANGRND:
            for i in range(Ang[1]):
                AngL.append(Ang[0])

        random.shuffle(AngL)

        return AngL[0]
    

##Prueba de Niveles##

MainC = Ch.AtkDmnManifest(1)

LV1 = Level(MainC,0,"Spn")

run =  True

while run:
    run = LV1.runLvSq()