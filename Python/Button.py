from asyncio.windows_events import NULL
import pygame, sys

from pygame import mouse

class Button:
    def __init__(self,text,width,height,pos):

        #Para pasar a otra pantalla
        self.clicked = False

        #Rect principal (borde)
        self.border_rect = pygame.Rect(pos,(width,height))
        self.border_color = '#000000'

        #Imagen dentro del Rect anterior
        self.background_img = pygame.image.load("./Assets/BckGrnd/paperallborder.png").convert()
        self.background_img = pygame.transform.scale(self.background_img, (width - 10 , height - 10))
        self.background_rect = self.background_img.get_rect(center = self.border_rect.center)
        
        #Texto por encima (centrado) del Rect anterior
        self.font = pygame.font.Font("./Assets/Fonts/Seagram_tfb.ttf", 25)
        self.text_text = self.font.render(text,True,'#000000')
        self.text_rect = self.text_text.get_rect(center = self.background_rect.center)
        
    #Para que haga algo en donde llames la clase
    def get_clicked(self):
        return self.clicked

    def popup(self,screen,text,rect):

        background_img = pygame.image.load("./Assets/BckGrnd/paperallborder.png").convert()
        background_img = pygame.transform.scale(background_img, (rect.width - 2 , rect.height - 2))           
        background_rect = background_img.get_rect(center = rect.center) 
        font = pygame.font.Font("./Assets/Fonts/Seagram_tfb.ttf", 20)
        mensaje_text = font.render(text,True,'#000000')
        mensaje_text_rect = mensaje_text.get_rect(center = rect.center)
        pygame.draw.rect(screen,'#000000',rect,1)
        screen.blit(background_img,background_rect)
        screen.blit(mensaje_text,mensaje_text_rect)

    #Dibuja los Rect anteriores y llama funcion mouse_check
    def draw(self,screen,enabled,flag):
        pygame.draw.rect(screen,self.border_color,self.border_rect,5)
        screen.blit(self.background_img,self.background_rect)
        screen.blit(self.text_text,self.text_rect)
        self.mouse_check(screen,enabled,flag)

    #Cambia los bordes de color y el valor self.clicked si se presiona el botton. enabled (se puede clickear) y flag (borde color rojo en los jefes ya derrotados) son bool.
    def mouse_check(self,screen,enabled,flag):
        mouse_pos = pygame.mouse.get_pos()
        if self.border_rect.collidepoint(mouse_pos):
            if(enabled == True):
                if(flag == False):
                    self.border_color = (247,236,36)
                else:
                    self.border_color = (255,0,0)
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
            else:
                #Muestra mensaje si el jefe no esta desbloqueado
                mensaje_rect = pygame.Rect(mouse_pos[0] - 350, mouse_pos[1] - 50, 350, 50)
                self.popup(screen,"Derrota a todos los Jefes anteriores",mensaje_rect)
        else:
            self.border_color = '#000000'