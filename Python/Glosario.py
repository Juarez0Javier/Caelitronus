import pygame

import Button
from pygame import Rect, mouse

pygame.init()
WIDTH, HEIGHT = 920, 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
clock.tick(30)

class Glosario:
    def __init__(self, screen):

        self.screen = screen
        self._ExitMode = False

    def runGlosario(self):

        screen = self.screen
        fondo = pygame.image.load("./Assets/BckGrnd/Nivel.png").convert()
        fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))
        fondo_rect = fondo.get_rect()
        font = pygame.font.Font("./Assets/Fonts/Seagram_tfb.ttf", 35)
        text_titulo = font.render("\nGLOSARIO",True,'#000000')
        titulo_rect = text_titulo.get_rect(centerx = fondo_rect.centerx,top = fondo_rect.top)
        but_back = Button.Button('Atras',100,50,(25,25))

        flechaizq = pygame.image.load("./Assets/Icons/izq.png")
        flechaizq_rect = pygame.Rect(0,345,50,60)
        flechader = pygame.image.load("./Assets/Icons/der.png")
        flechader_rect = pygame.Rect(870,345,50,60)

        #Botones con imagenes de la seccion 1 (PERSONAJES)
        caelius = pygame.image.load("./Assets/ChArt/caelius de ira.png")
        but_caelius = Button.GlosarioButton(caelius,'Caelius',170,260,(55,150))  
        monja = pygame.image.load("./Assets/ChArt/la monja.png")
        but_monja = Button.GlosarioButton(monja,'Monja Roja',170,260,(265,150))
        monaquillo = pygame.image.load("./Assets/ChArt/los monaquillo.png")
        but_monaquillo = Button.GlosarioButton(monaquillo,'Monaquillo',170,260,(475,150))        
        espina = pygame.image.load("./Assets/ChArt/padre espina.png")
        but_espina = Button.GlosarioButton(espina,'Padre Espina',170,260,(685,150))        
        serpico = pygame.image.load("./Assets/ChArt/Obispo Serpico.png")
        but_serpico = Button.GlosarioButton(serpico,'Obispo Serpico',170,260,(55,450))        
        corvus = pygame.image.load("./Assets/ChArt/Fray Corvus.png")
        but_corvus = Button.GlosarioButton(corvus,'Fray Corvus',170,260,(265,450))        
        galaad = pygame.image.load("./Assets/ChArt/galaad.png")
        but_galaad = Button.GlosarioButton(galaad,'Galaad',170,260,(475,450))        
        kapparah = pygame.image.load("./Assets/ChArt/Kapparah.png")
        but_kapparah = Button.GlosarioButton(kapparah,'Kapparah',170,260,(685,450))
        #Botones de la seccion 2 (LUGARES)
        #Botones de la seccion 3 (CONCEPTOS)

        run = True
        seccion = 1
        mouse_pos = pygame.mouse.get_pos()

        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if(but_back.get_clicked() == True):
                        self._ExitMode = True
                    if flechaizq_rect.collidepoint(mouse_pos) and seccion > 1:
                        seccion = seccion - 1
                    if flechader_rect.collidepoint(mouse_pos) and seccion < 3:
                        seccion = seccion + 1
                    if(but_caelius.get_clicked() == True):
                        return but_caelius
                    if(but_monja.get_clicked() == True):
                        return but_monja
                    if(but_monaquillo.get_clicked() == True):
                        return but_monaquillo
                    if(but_espina.get_clicked() == True):
                        return but_espina
                    if(but_serpico.get_clicked() == True):
                        return but_serpico
                    if(but_corvus.get_clicked() == True):
                        return but_corvus
                    if(but_galaad.get_clicked() == True):
                        return but_galaad
                    if(but_kapparah.get_clicked() == True):
                        return but_kapparah
                if event.type == pygame.QUIT:
                    pygame.quit()

                screen.blit(fondo,(0,0))
                but_back.draw(screen,True,False)
                screen.blit(text_titulo,titulo_rect)
                
                mouse_pos = pygame.mouse.get_pos()
                if flechaizq_rect.collidepoint(mouse_pos) and seccion > 1:
                    flechaizq = pygame.transform.scale(flechaizq, (55, 70))
                else:
                    flechaizq = pygame.transform.scale(flechaizq, (50, 60))
                if flechader_rect.collidepoint(mouse_pos) and seccion < 3:
                    flechader = pygame.transform.scale(flechader, (55, 70))
                else:
                    flechader = pygame.transform.scale(flechader, (50, 60))
                screen.blit(flechader,flechader_rect)
                screen.blit(flechaizq,flechaizq_rect)

                font = pygame.font.Font("./Assets/Fonts/Seagram_tfb.ttf", 25)
                if seccion == 1:
                    text_subtitulo = font.render("\n\n\nPERSONAJES",True,'#000000')
                    but_caelius.draw(screen)
                    but_monja.draw(screen)
                    but_monaquillo.draw(screen)
                    but_espina.draw(screen)
                    but_serpico.draw(screen)
                    but_corvus.draw(screen)
                    but_galaad.draw(screen)
                    but_kapparah.draw(screen)
                elif seccion == 2:
                    text_subtitulo = font.render("\n\n\nLUGARES",True,'#000000')
                elif seccion == 3:
                    text_subtitulo = font.render("\n\n\nCONCEPTOS",True,'#000000')

                subtitulo_rect = text_subtitulo.get_rect(centerx = fondo_rect.centerx,top = fondo_rect.top)
                screen.blit(text_subtitulo,subtitulo_rect)

                if self._ExitMode == True:
                    run = False

                pygame.display.update()
                clock.tick(30)
        
        return False

class Detalle:
    def __init__(self, screen):

        self.screen = screen
        self._ExitMode = False

    def cargaDetalle(self,screen,titulo,img,texto):

        fondo_rect = pygame.Rect(0,0,screen.width,screen.height)
        font = pygame.font.Font("./Assets/Fonts/Seagram_tfb.ttf", 25)
        text_titulo = font.render("\n" + titulo, True,'#000000')
        titulo_rect = text_titulo.get_rect(centerx = fondo_rect.centerx,top = fondo_rect.top)

        #Bloque superior (Imagen, Botones opcionales)
        background = pygame.image.load("./Assets/BckGrnd/paperallborder.png").convert()
        border_color = '#000000'
        border_rect = pygame.Rect(352,75,215,291)
        background = pygame.transform.scale(background, (border_rect.width - 10 , border_rect.height - 10))
        background_rect = background.get_rect(center = border_rect.center)
        img = pygame.transform.scale(img, (background_rect.width - 5, background_rect.height - 9))
        img_rect = img.get_rect(centerx = background_rect.centerx,top = background_rect.top + 4)

        #Bloque inferior (Texto)
        texto_border_rect = pygame.Rect(60,375,800,350)
        texto_background = pygame.image.load("./Assets/BckGrnd/paper.png")
        texto_background = pygame.transform.scale(texto_background, (texto_border_rect.width - 10 , texto_border_rect.height - 10))
        texto_background_rect = texto_background.get_rect(center = texto_border_rect.center)
        font = pygame.font.Font("./Assets/Fonts/Seagram_tfb.ttf", 20)
        text = font.render(texto, True,'#000000',None,texto_background_rect.width-10)
        text_rect = text.get_rect(center = texto_background_rect.center)
       
        
        screen.blit(text_titulo,titulo_rect)

        pygame.draw.rect(screen,border_color,border_rect,5)        
        screen.blit(background,background_rect)
        screen.blit(img,img_rect)

        pygame.draw.rect(screen,border_color,texto_border_rect,5)
        screen.blit(texto_background,texto_background_rect)
        screen.blit(text,text_rect)

    def runDetalle(self,boton):

        screen = self.screen
        fondo = pygame.image.load("./Assets/BckGrnd/Nivel.png").convert()
        fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))
        fondo_rect = fondo.get_rect()
        but_back = Button.Button('Atras',100,50,(25,25))

        flechaizq = pygame.image.load("./Assets/Icons/izq.png")
        flechaizq_rect = pygame.Rect(312,195,40,50)
        flechader = pygame.image.load("./Assets/Icons/der.png")
        flechader_rect = pygame.Rect(567,195,40,50)

        #Reemplazr prueba de texto con lo que quieras escribir sobre el sujeto
        texto = ""
        if (boton.text == 'Caelius'):
            textoIra = "Prueba de texto de Caelius Ira"
            imgego = pygame.image.load("./Assets/ChArt/caelius de ego.png")
            textoEgo = "Prueba de texto de Caelius Ego"
            imgpena = pygame.image.load("./Assets/ChArt/caelius de pena.png")
            textoPena = "Prueba de texto de Caelius Pena"
        elif (boton.text == 'Monja Roja'):
            texto = "Prueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja Roja"\
                "Prueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja Roja"\
                "Prueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja Roja"\
                "Prueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja RojaPrueba de texto de Monja Roja"
        elif (boton.text == 'Monaquillo'):
            texto = "Prueba de texto de Monaquillo"
        elif (boton.text == 'Padre Espina'):
            texto = "Prueba de texto de Padre Espina"
        elif (boton.text == 'Obispo Serpico'):
            texto = "Prueba de texto de Obispo Serpico"
        elif (boton.text == 'Fray Corvus'):
            texto = "Prueba de texto de Fray Corvus"
        elif (boton.text == 'Galaad'):
            texto = "Prueba de texto de Galaad"
        elif (boton.text == 'Kapparah'):
            texto = "Prueba de texto de Kapparah"
        
        run = True
        opc = 1
        mouse_pos = pygame.mouse.get_pos()

        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if(but_back.get_clicked() == True):
                        self._ExitMode = True
                    if flechaizq_rect.collidepoint(mouse_pos) and opc > 1:
                        opc = opc - 1
                    if flechader_rect.collidepoint(mouse_pos) and opc < 3:
                        opc = opc + 1
                if event.type == pygame.QUIT:
                    pygame.quit()

            screen.blit(fondo,(0,0))
            but_back.draw(screen,True,False)

            mouse_pos = pygame.mouse.get_pos()

            if(texto == ""):
                if flechaizq_rect.collidepoint(mouse_pos) and opc > 1:
                    flechaizq = pygame.transform.scale(flechaizq, (45, 60))
                else:
                    flechaizq = pygame.transform.scale(flechaizq, (40, 50))
                if flechader_rect.collidepoint(mouse_pos) and opc < 3:
                    flechader = pygame.transform.scale(flechader, (45, 60))
                else:
                    flechader = pygame.transform.scale(flechader, (40, 50))
                screen.blit(flechader,flechader_rect)
                screen.blit(flechaizq,flechaizq_rect)

                if (opc == 1):
                    self.cargaDetalle(screen,boton.text,boton.img,textoIra)
                elif (opc == 2):
                    self.cargaDetalle(screen,boton.text,imgego,textoEgo)
                elif (opc == 3):
                    self.cargaDetalle(screen,boton.text,imgpena,textoPena)
            else:
                self.cargaDetalle(screen,boton.text,boton.img,texto)

            if self._ExitMode == True:
                    run = False

            pygame.display.update()
            clock.tick(30)