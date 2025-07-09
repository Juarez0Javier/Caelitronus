import random
import numpy
import pygame
import pygame_widgets as pwidgets
from pygame_widgets.button import Button

import Characters

pygame.init()


WIDTH, HEIGHT = 920, 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
font_Path = r"Assets\\Fonts\\Seagram_Tfb.ttf"
BTNIMAGE = r"Assets\\BckGrnd\\paperallborder.png"
MENUIMAGE = r"Assets\\BckGrnd\\paperallborder.png"

clock = pygame.time.Clock()
clock.tick(30)

class BinaryMenu:
    def __init__(self, screen):

        self._screen =  screen

        #Fonts
        self._BttnFont = pygame.font.Font(r"Assets\\Fonts\\Seagram_Tfb.ttf",16)
        self._TitleFont = pygame.font.Font(r"Assets\\Fonts\\Seagram_Tfb.ttf", 20)

        #Elements Text
        self._titleTxt = "Title"
        self._leftTxt = "Left"
        self._rightTxt= "Right"

        #Separator
        self._sprt = 20

        #Elements Size
        self._bttnSize = (140,40)
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
    
        self._menuColor = (255,255,255,255)
        self._menuImage = pygame.image.load(r"Assets\\BckGrnd\\paperallborder.png")
        self._btnImage = pygame.image.load(r"Assets\\BckGrnd\\papersideborder.png")

        self._BtnCol = (0,0,0)
        self._hoverBtnnCol = (247,236,36)
        self._pressedBtnnCol = (247,236,36)

        #Buttons Enabling
        self._leftEn = True
        self._rightEn = True
         
        #Escape Clause
        self._ExitMode = False

        #Return Value
        self._ret = True
        

    def runMenu(self):

        #self._screen.fill((255,255,255))
        
        #Creting Menu Box
        menu = self._menuImage.fill(self._menuColor, None, pygame.BLEND_RGBA_MULT)
        menu = pygame.transform.scale(self._menuImage,self._menuSize)

        self._screen.blit(menu,self._menuPos)

        #pygame.draw.rect(self._screen, self._menuCol, pygame.Rect(*self._menuPos,*self._menuSize))

        #Creating Tittle
        title = self._TitleFont.render(self._titleTxt,True,self._titleTxtCol)
        self._screen.blit(title,self._titlePos)
        
        #Creating Buttons
        self._btnImage = pygame.transform.scale(self._btnImage, numpy.subtract(self._bttnSize,(10,10)))

        leftBtn = Button(
            self._screen, *self._leftBttnPos, *self._bttnSize, text=self._leftTxt,
            font=self._BttnFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol if self._leftEn == True else self._BtnCol,
            hoverColour = self._hoverBtnnCol if self._leftEn == True else self._BtnCol,
            image = self._btnImage,
            onClick = lambda: self.pressLeft() if self._leftEn == True else self.null(),
            textColour = self._btnnTxtCol)
        
        rightBtn = Button(
            self._screen, *self._rightBttnPos, *self._bttnSize, text=self._rightTxt,
            font=self._BttnFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol if self._rightEn == True else self._BtnCol,
            hoverColour = self._hoverBtnnCol if self._rightEn == True else self._BtnCol,
            image = self._btnImage,
            onClick = lambda: self.pressRight() if self._rightEn == True else self.null(),
            textColour = self._btnnTxtCol)

        run = True
        self._ExitMode = False
        self._ret = False

        while run:
            events = pygame.event.get()
            #print("Running Menu")
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
    
    def null(self):
        pass

    def caclMenuSize(self):

        horBtnnSize = 2 * self._bttnSize[0] + 3 * self._sprt
        horTitleSize = self._titleSize[0] + 2 * self._sprt

        menuWidth = 0
        menuHeight = 2 * self._bttnSize[1] + self._titleSize[1] + 4 * self._sprt

        if horBtnnSize > horTitleSize:
            menuWidth = horBtnnSize
        else:
            menuWidth = horTitleSize
        
        return (menuWidth,menuHeight)

class WScreen (BinaryMenu):
    def __init__(self,screen,M1):
        super().__init__(screen)
        self._titleTxt = "Victoria"
        self._leftTxt = "Subir de Nivel"
        self._rightTxt= "Siguiente Batalla"

        self._titleSize = self._TitleFont.size(self._titleTxt)
        self._titlePos = (self._menuCenter[0] - self._titleSize[0]/2,self._menuCenter[1] - self._bttnSize[1] - self._sprt)

        self._M1 = M1

        self._leftEn = self._leftEn if self._M1.checkXp() == True else False

    def pressLeft(self):
        #print("We Level Up")
        if self._M1.checkXp() == True:
            self._ret = True
            self._ExitMode = True

            #print(self._ret)
        
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

class GWScreen (WScreen):
    def __init__(self,screen,M1):
        super().__init__(screen,M1)

        self._TitleFont = pygame.font.Font(font_Path, 26)

        self._titleTxt = "GRAN VICTORIA"
        self._leftTxt = "Subir de Nivel"
        self._rightTxt = "Continuar a la Seleccion de los Niveles"

        self._bttnSize = (300,55)

        self._titleSize = self._TitleFont.size(self._titleTxt)
        self._menuSize = (WIDTH,self.caclMenuSize()[1] + self._sprt)

        self._menuCenter = (WIDTH/2, 320)

        self._leftBttnPos = (self._menuCenter[0] - self._bttnSize[0]/2,self._menuCenter[1])
        self._rightBttnPos = (self._menuCenter[0] - self._bttnSize[0]/2,self._menuCenter[1] + self._bttnSize[1] + self._sprt)
        self._titlePos = (self._menuCenter[0] - self._titleSize[0]/2,self._menuCenter[1] - self._bttnSize[1] - self._sprt)
        self._menuPos = (self._menuCenter[0] - self._menuSize[0]/2,self._menuCenter[1] - 100)
        
        self._menuColor = (249,218,94,0)
        self._menuImage = pygame.image.load(r"Assets\\BckGrnd\\paper.png")
        
class LvUpScreen:
    def __init__(self,screen,M1):

        self._screen =  screen
        self._M1 = M1

        #Textos
        self._titleTxt = "Caelus sube de Nivel"
        self._untitleTxt = "Estadisticas Aumentadas"
        self._statTxt = self.gnrtStatTxt()
        self._bttnOverTxt = "Elige una mejora"

        #Fonts
        self._stageFont = pygame.font.Font(r"Assets\\Fonts\\Seagram_Tfb.ttf", 15)

        self._TitleFont = pygame.font.Font(r"Assets\\Fonts\\Seagram_Tfb.ttf", 50)

        self._subTitleFont = pygame.font.Font(r"Assets\\Fonts\\Seagram_Tfb.ttf", 25)

        self._statFont = pygame.font.Font(r"Assets\\Fonts\\Seagram_Tfb.ttf", 18)

        #Separator
        self._sprt = 50

        #Elements Size
        self._bttnSize = (180,80)
        self._titleSize = self._TitleFont.size("Caelus sube de Nivel")
        

        #Elements Positions
        self._menuCenter = (int(WIDTH/2), 320)

        self._bttmLeftBttnPos = (self._menuCenter[0] - self._bttnSize[0] * (1/2 + 1) - self._sprt, self._menuCenter[1] - self._bttnSize[1]/2 + self._titleSize[1]/2 + 5 * self._sprt)
        self._bttmMiddleBtnnPos = (self._menuCenter[0] - self._bttnSize[0]/2, self._menuCenter[1] - self._bttnSize[1]/2 + self._titleSize[1]/2 + 5 * self._sprt)
        self._bttmRightBtnnPos = (self._menuCenter[0] - self._bttnSize[0] * (1/2 - 1) + self._sprt, self._menuCenter[1] - self._bttnSize[1]/2 + self._titleSize[1]/2 + 5 * self._sprt)

        self._titlePos = (self._menuCenter[0] - self._titleSize[0]/2 , self._menuCenter[1] + - self._titleSize[1]/2 - 4 * self._sprt)

        #Elements Colors (yay!)
        self._titleTxtCol = (0,0,0)
        self._btnnTxtCol = (0,0,0)
    
        self._backCol = (226, 129, 99)
        self._backImage = pygame.image.load(r"Assets\\BckGrnd\\paper.png")
        self._btnImage = pygame.image.load(r"Assets\\BckGrnd\\papersideborder.png")

        self._BtnCol = (0,0,0)
        self._hoverBtnnCol = (247,236,36)
        self._pressedBtnnCol = (247,236,36)

        #Returns
        self._ExitMode = False

        pass

    def runMenu(self):
        self._screen.fill((137,137,137))

        #Creating Background
        back = self._backImage.fill((226, 114, 86), None, pygame.BLEND_RGBA_MULT)
        back = pygame.transform.scale(self._backImage,(WIDTH,HEIGHT))

        self._screen.blit(back,(0,0))
        
        #Creating Tittle
        title = self._TitleFont.render(self._titleTxt,True,self._titleTxtCol)
        self._screen.blit(title,self._titlePos)

        #Creating Stat Subtsection

        title = self._subTitleFont.render(self._untitleTxt,True,self._titleTxtCol)
        title_size = self._subTitleFont.size(self._untitleTxt)
        self._screen.blit(title,(self._menuCenter[0] - title_size[0]/2,self._titlePos[1] + self._titleSize[1] + self._sprt))

        i = 0
        for txt in self._statTxt:
            title = self._statFont.render(txt,True,self._titleTxtCol)
            title_size = self._statFont.size(txt)
            self._screen.blit(title,(self._menuCenter[0] - title_size[0]/2, self._titlePos[1] + self._titleSize[1] * (2/3) + (2 + i) * self._sprt + title_size[1]))
            i+=1


        #Generating Buttons 

        title = self._TitleFont.render(self._bttnOverTxt,True,self._titleTxtCol)
        title_size = self._TitleFont.size(self._bttnOverTxt)
        self._screen.blit(title,(self._menuCenter[0] - title_size[0]/2,self._bttmMiddleBtnnPos[1] - self._bttnSize[1] - self._sprt))

        statList =[self.gnrtRndStatUp(),self.gnrtRndStatUp(),self.gnrtRndStatUp()]

        self._btnImage = pygame.transform.scale(self._btnImage, numpy.subtract(self._bttnSize,(10,10)))

        bttomLeftTxt = "+" + str(statList[0][0][1])  + " " + str(statList[0][0][0]) + "\n" + "+" + str(statList[0][1][1])  + " " + str(statList[0][1][0])
        bttomMiddleTxt = "+" + str(statList[1][0][1])  + " " + str(statList[1][0][0]) + "\n" + "+" + str(statList[1][1][1])  + " " + str(statList[1][1][0])
        bttomRightTxt = "+" + str(statList[2][0][1])  + " " + str(statList[2][0][0]) + "\n" + "+" + str(statList[2][1][1])  + " " + str(statList[2][1][0])
       
        
        bttmLeftBtn = Button(
            self._screen, *self._bttmLeftBttnPos, *self._bttnSize, text=bttomLeftTxt,
            font=self._stageFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            image = self._btnImage,
            onClick = lambda: self.btnnStatUp(statList[0]),
            textColour = self._btnnTxtCol)
        
        bttmMiddleBtn = Button(
            self._screen, *self._bttmMiddleBtnnPos, *self._bttnSize,  text=bttomMiddleTxt,
            font=self._stageFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            image = self._btnImage,
            onClick = lambda: self.btnnStatUp(statList[1]),
            textColour = self._btnnTxtCol)
        
        bttmRightBtn = Button(
            self._screen, *self._bttmRightBtnnPos, *self._bttnSize,  text=bttomRightTxt,
            font=self._stageFont, margin=20,
            inactiveColour = self._BtnCol,
            pressedColour = self._pressedBtnnCol,
            hoverColour = self._hoverBtnnCol,
            image = self._btnImage,
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
        TxtList = []
        M1Bp = self._M1.get_lvBp()
        M1Lv = self._M1.get_lv()

        lvOffset = M1Lv - M1Bp[0]['StartLv']  + 1

        i = 0
        Txt = ""
        for Stat in Characters.STATLIST:

            Txt += Stat + ": " + str(M1Bp[M1Lv][Stat]) + " => " + str(M1Bp[lvOffset][Stat] + M1Bp[lvOffset+1][Stat])
            
            if i == 0 or i == 3 or i == 6:
                TxtList.append(Txt)
                Txt = ""
            else:
               Txt += "    " 
            i+=1
        return TxtList
    
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

'''
import Characters

M1 = Characters.AtkDmnManifest(1)

WinScreen = WScreen(SCREEN,M1)

print(WinScreen.runMenu())
'''
