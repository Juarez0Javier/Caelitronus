import random
import numpy
import pygame
import pygame_widgets as pwidgets
from pygame_widgets.button import Button

import Characters

pygame.init()


WIDTH, HEIGHT = 920, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font_Path = r"Assets\\Fonts\\Seagram_Tfb.ttf"

clock = pygame.time.Clock()
clock.tick(30)

class BinaryMenu:
    def __init__(self, screen):

        self._screen =  screen

        #Fonts
        self._BttnFont = pygame.font.Font(font_Path, 16)
        self._TitleFont = pygame.font.Font(font_Path, 20)

        #Elements Text
        self._titleTxt = "Title"
        self._leftTxt = "Left"
        self._rightTxt= "Right"

        #Separator
        self._sprt = 20

        #Elements Size
        self._bttnSize = (130,30)

        self._titleSize = self._TitleFont.size(self._titleTxt)

        self._menuSize = self.caclMenuSize()
        

        #Elements Positions
        self._menuCenter = (WIDTH/2, 570)

        self._leftBttnPos = (self._menuCenter[0] - self._bttnSize[0] - self._sprt/2,self._menuCenter[1])
        self._rightBttnPos = (self._menuCenter[0] + self._sprt/2,self._menuCenter[1])

        self._titlePos = (self._menuCenter[0] - self._titleSize[0]/2,self._menuCenter[1] - self._bttnSize[1] - self._sprt)

        self._menuPos = (numpy.subtract(self._menuCenter,numpy.divide(self._menuSize,2)))

        #Elements Colors (yay!)
        self._titleTxtCol = (0,0,0)
        self._btnnTxtCol = (0,0,0)
    
        self._menuCol = (226, 129, 99)
        self._BtnCol = (229,113,41)
        self._hoverBtnnCol = (229,127,56)
        self._pressedBtnnCol = (140,71,28)
        
         
        #Escape Clause
        self._ExitMode = False

        #Return Value
        self._ret = False
        

    def runMenu(self):

        #self._screen.fill((255,255,255))

        #Creting Menu Box
        pygame.draw.rect(self._screen, self._menuCol, pygame.Rect(*self._menuPos,*self._menuSize))

        #Creating Tittle
        title = self._TitleFont.render(self._titleTxt,True,self._titleTxtCol)
        self._screen.blit(title,self._titlePos)
        
        #Creating Buttons
        rightBtn = Button(
            self._screen, *self._rightBttnPos, *self._bttnSize, text=self._rightTxt,
            font=self._BttnFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            onClick = lambda: self.pressRight(),
            textColour = self._btnnTxtCol)

        leftBtn = Button(
            self._screen, *self._leftBttnPos, *self._bttnSize, text=self._leftTxt,
            font=self._BttnFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            onClick = lambda: self.pressLeft(),
            textColour = self._btnnTxtCol)

        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()

            if self._ExitMode == True:
                run = False

            pwidgets.update(events)
            pygame.display.update()

        return self._ret
    
    def pressLeft(self):
        #print("Left")

        self._ret = False
        self._ExitMode = True
    
    def pressRight(self):
        #print("Right")

        self._ret = False
        self._ExitMode = True

    def caclMenuSize(self):

        horBtnnSize = 2 * self._bttnSize[0] + 3 * self._sprt
        horTitleSize = self._titleSize[0] + 2 * self._sprt

        menuWidth = 0
        menuHeight = 2 * self._bttnSize[1] + self._titleSize[1] + 3 * self._sprt

        if horBtnnSize > horTitleSize:
            menuWidth = horBtnnSize
        else:
            menuWidth = horTitleSize
        
        return (menuWidth,menuHeight)

class WScreen (BinaryMenu):
    def __init__(self, screen):
        super().__init__(screen)
        self._titleTxt = "Victoria"
        self._leftTxt = "Subir de Nivel"
        self._rightTxt= "Siguiente Batalla"

        self._titleSize = self._TitleFont.size(self._titleTxt)
        self._titlePos = (self._menuCenter[0] - self._titleSize[0]/2,self._menuCenter[1] - self._bttnSize[1] - self._sprt)

    def pressLeft(self):
        #print("We Level Up")
        self._ret = True
        self._ExitMode = True
        
class LScreen (BinaryMenu):
    def __init__(self, screen):
        super().__init__(screen)
        self._titleTxt = "Derrota"
        self._leftTxt = "Reintentar"
        self._rightTxt= "Seleccion de Nivel"

        self._titleSize = self._TitleFont.size(self._titleTxt)
        self._titlePos = (self._menuCenter[0] - self._titleSize[0]/2,self._menuCenter[1] - self._bttnSize[1] - self._sprt)

    def pressLeft(self):
        #We Try again
        self._ret = True
        self._ExitMode = True

class GWScreen (BinaryMenu):
    def __init__(self, screen):
        super().__init__(screen)

        self._TitleFont = pygame.font.Font(font_Path, 26)

        self._titleTxt = "GRAN VICTORIA"
        self._leftTxt = "Continuar a la Seleccion de los Niveles"
        self._rightTxt= "Subir de Nivel"

        self._bttnSize = (300,30)

        self._menuCenter = (WIDTH/2, 320)

        self._titleSize = self._TitleFont.size(self._titleTxt)
        self._menuSize = (WIDTH,2 * self._bttnSize[1] + self._titleSize[1] + 4 * self._sprt)

        self._leftBttnPos = (self._menuCenter[0] - self._bttnSize[0]/2,self._menuCenter[1])
        self._rightBttnPos = (self._menuCenter[0] - self._bttnSize[0]/2,self._menuCenter[1] + self._bttnSize[1] + self._sprt)
        self._titlePos = (self._menuCenter[0] - self._titleSize[0]/2,self._menuCenter[1] - self._bttnSize[1] - self._sprt)
        self._menuPos = (numpy.subtract(self._menuCenter,numpy.divide(self._menuSize,2)))

    def pressRight(self):
        #We Level Up
        self._ret = True
        self._ExitMode = True

r'''
class StageSelector:
    
    def __init__(self, screen):

        self._screen =  screen

        #Fonts
        self._stageFont = pygame.font.Font("Assets\\Fonts\\Seagram_Tfb.ttf", 15)
        self._TitleFont = pygame.font.Font("Assets\\Fonts\\Seagram_Tfb.ttf", 50)

        #Separator
        self._sprt = 50

        #Elements Size
        self._bttnSize = (170,70)
        self._titleSize = self._TitleFont.size("ELIGE TU DESTINO")
        

        #Elements Positions
        self._menuCenter = (WIDTH/2, 320)

        self._bttmLeftBttnPos = (self._menuCenter[0] - self._bttnSize[0] * (1/2 + 1) - self._sprt, self._menuCenter[1] - self._bttnSize[1]/2 + self._titleSize[1]/2 + self._sprt)
        self._bttmMiddleBtnnPos = (self._menuCenter[0] - self._bttnSize[0]/2, self._menuCenter[1] - self._bttnSize[1]/2 + self._titleSize[1]/2 + self._sprt)
        self._bttmRightBtnnPos = (self._menuCenter[0] - self._bttnSize[0] * (1/2 - 1) + self._sprt, self._menuCenter[1] - self._bttnSize[1]/2 + self._titleSize[1]/2 + self._sprt)

        self._centMiddleBtnnPos = (self._menuCenter[0] - self._bttnSize[0]/2,self._menuCenter[1] - self._bttnSize[1] * (1/2 + 1) + self._titleSize[1]/2)

        self._uppMiddleBtnnPos = (self._menuCenter[0] - self._bttnSize[0]/2,self._menuCenter[1] - self._bttnSize[1] * (1/2 + 1) + self._titleSize[1]/2)

        self._titlePos = (self._menuCenter[0] - self._titleSize[0]/2 , self._menuCenter[1] - self._bttnSize[1]/2 + 2 * self._titleSize[1]/2 + 4 * self._sprt)

        #Elements Colors (yay!)
        self._titleTxtCol = (0,0,0)
        self._btnnTxtCol = (0,0,0)
    
        self._menuCol = (226, 129, 99)
        self._BtnCol = (229,113,41)
        self._hoverBtnnCol = (229,127,56)
        self._pressedBtnnCol = (140,71,28)

        #Returns
        self.ret = ""
        self._ExitMode = False

    def runMenu(self):

        self._screen.fill((137,137,137))

        #Creating Tittle
        title = self._TitleFont.render("ELIGE TU DESTINO",True,self._titleTxtCol)
        self._screen.blit(title,self._titlePos)

        bttmLeftBtn = Button(
            self._screen, *self._bttmLeftBttnPos, *self._bttnSize,  text="PADRE ESPINA",
            font=self._stageFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            onClick = lambda: self.pressStage("Spn"),
            textColour = self._btnnTxtCol)
        
        bttmMiddleBtn = Button(
            self._screen, *self._bttmMiddleBtnnPos, *self._bttnSize,  text="OBISPO SERPICO",
            font=self._stageFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            onClick = lambda: self.pressStage("Fn"),
            textColour = self._btnnTxtCol)
        
        bttmRightBtn = Button(
            self._screen, *self._bttmRightBtnnPos, *self._bttnSize,  text="FRAY CORVUS",
            font=self._stageFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            onClick = lambda: self.pressStage("Pss"),
            textColour = self._btnnTxtCol)
        
        centMiddleBtn = Button(
            self._screen, *self._centMiddleBtnnPos, *self._bttnSize, text="GALAAD",
            font=self._stageFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            onClick = lambda: self.pressStage("Fnl"),
            textColour = self._btnnTxtCol)
        
        spnBtn = Button(
            self._screen, *self._uppMiddleBtnnPos, *self._bttnSize, text="???",
            font=self._stageFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            onClick = lambda: self.pressStage(""),
            textColour = self._btnnTxtCol)

        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()

            if self._ExitMode == True:
                run = False

            pwidgets.update(events)
            pygame.display.update()

        return self._ret
    
    def pressStage(self,stage):
        self._ExitMode == True
        self.ret = stage
'''

class LvUpScreen:
    def __init__(self,screen,M1):

        self._screen =  screen
        self._M1 = M1

        #Textos
        self._titleTxt = "Caelus sube de Nivel"
        self._untitleTxt = "Estadisticas Aumentadas"
        self._statTxt = self.gnrtStatTxt()

        #Fonts
        self._stageFont = pygame.font.Font(font_Path, 15)
        self._TitleFont = pygame.font.Font(font_Path, 50)

        #Separator
        self._sprt = 50

        #Elements Size
        self._bttnSize = (170,70)
        self._titleSize = self._TitleFont.size("Caelus sube de Nivel")
        

        #Elements Positions
        self._menuCenter = (WIDTH/2, 320)

        self._bttmLeftBttnPos = (self._menuCenter[0] - self._bttnSize[0] * (1/2 + 1) - self._sprt, self._menuCenter[1] - self._bttnSize[1]/2 + self._titleSize[1]/2 + self._sprt)
        self._bttmMiddleBtnnPos = (self._menuCenter[0] - self._bttnSize[0]/2, self._menuCenter[1] - self._bttnSize[1]/2 + self._titleSize[1]/2 + self._sprt)
        self._bttmRightBtnnPos = (self._menuCenter[0] - self._bttnSize[0] * (1/2 - 1) + self._sprt, self._menuCenter[1] - self._bttnSize[1]/2 + self._titleSize[1]/2 + self._sprt)

        self._titlePos = (self._menuCenter[0] - self._titleSize[0]/2 , self._menuCenter[1] + - self._titleSize[1]/2 - 4 * self._sprt)

        #Elements Colors (yay!)
        self._titleTxtCol = (0,0,0)
        self._btnnTxtCol = (0,0,0)
    
        self._menuCol = (226, 129, 99)
        self._BtnCol = (229,113,41)
        self._hoverBtnnCol = (229,127,56)
        self._pressedBtnnCol = (140,71,28)

        #Returns
        self._ExitMode = False

        pass

    def runMenu(self):
        self._screen.fill((137,137,137))

        #Creating Tittle
        title = self._TitleFont.render("Caelus sube de Nivel",True,self._titleTxtCol)
        self._screen.blit(title,self._titlePos)

        #Creating Stat Subtsection
        title = self._TitleFont.render("Caelus sube de Nivel",True,self._titleTxtCol)
        self._screen.blit(title,self._titlePos)

        #Creating Mejora Subsection

        #Generating Ranodm Stat Picks
        statList =[self.gnrtRndStatUp(),self.gnrtRndStatUp(),self.gnrtRndStatUp()]

        #Generating Buttons 
        bttomLeftTxt = "+" + str(statList[0][0][1])  + " " + str(statList[0][0][0]) + "   " + "+" + str(statList[0][1][1])  + " " + str(statList[0][1][0])
        bttomMiddleTxt = "+" + str(statList[1][0][1])  + " " + str(statList[1][0][0]) + "   " + "+" + str(statList[1][1][1])  + " " + str(statList[1][1][0])
        bttomRightTxt = "+" + str(statList[2][0][1])  + " " + str(statList[2][0][0]) + "   " + "+" + str(statList[2][1][1])  + " " + str(statList[2][1][0])
       
        bttmLeftBtn = Button(
            self._screen, *self._bttmLeftBttnPos, *self._bttnSize, text=bttomLeftTxt,
            font=self._stageFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            onClick = lambda: self.btnnStatUp(statList[0]),
            textColour = self._btnnTxtCol)
        
        bttmMiddleBtn = Button(
            self._screen, *self._bttmMiddleBtnnPos, *self._bttnSize,  text=bttomMiddleTxt,
            font=self._stageFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            onClick = lambda: self.btnnStatUp(statList[1]),
            textColour = self._btnnTxtCol)
        
        bttmRightBtn = Button(
            self._screen, *self._bttmRightBtnnPos, *self._bttnSize,  text=bttomRightTxt,
            font=self._stageFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            onClick = lambda: self.btnnStatUp(statList[2]),
            textColour = self._btnnTxtCol)

        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()

            if self._ExitMode == True:
                run = False

            pwidgets.update(events)
            pygame.display.update()
    
    def gnrtStatTxt(self):
        Txt = ""

        M1Bp = self._M1.get_lvBp()
        M1Lv = self._M1.get_lv()

        lvOffset = M1Lv - M1Bp[0]['StartLv']  + 1

        for Stat in Characters.STATLIST:
            Txt += Stat + ": " + str(M1Bp[M1Lv][Stat]) + " → " + str(M1Bp[lvOffset][Stat] + M1Bp[lvOffset+1][Stat]) + " "
        return Txt
    
    def gnrtRndStatUp(self):
        pickList = []

        for i in range(0,2):
            statList = [[Characters.STATLIST[0],25],
                        [Characters.STATLIST[1],5],
                        [Characters.STATLIST[2],5],
                        [Characters.STATLIST[3],5],
                        [Characters.STATLIST[4],5],
                        [Characters.STATLIST[5],5],
                        [Characters.STATLIST[6],5]]
            random.shuffle(statList)
            pickList.append(statList[0])
        return pickList

    def btnnStatUp(self,stats):
        M1 = self._M1

        for stat in stats:
            IncrValue = M1.get_bsStatByKey(stat[0]) + stat[1]
            M1.set_bsStatByKey(stat[0],IncrValue)

        M1.lvUp()

        self._ExitMode = True


#WinScreen = WScreen(screen)
#print(WinScreen.runMenu())
