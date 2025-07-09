import pygame
import sys
import Button

#Configuración Global del Juego
pygame.init()
WIDTH, HEIGHT = 920, 750  #Tamaño de la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Caeltronus - El Juego") 
clock = pygame.time.Clock()

#Prueba. True si los jefes han sido derrotados (no me hago cargo si no respetan el orden de pelea)
flag_serpico = False
flag_espina = False
flag_corvus = False
flag_galaad = False
flag_misionero = False
jefesderrotados = 0

#Trae y muestra los iconos de los jefes
fondo = pygame.image.load("./Assets/BckGrnd/Nivel.png").convert()
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))
icon_back_color = '#000000'
if(flag_serpico == False):
    icon_serpico = pygame.image.load("./Assets/Icons/Serpico.png")
else:
    icon_serpico = pygame.image.load("./Assets/Icons/SerpicoDerrotado.png")
    jefesderrotados+=1
icon_serpico = pygame.transform.scale(icon_serpico, (50, 50))
posicion = pygame.Rect(155,550,50,50)
icon_serpico_rect = icon_serpico.get_rect(center = posicion.center)
if(flag_espina == False):
    icon_espina = pygame.image.load("./Assets/Icons/Espina.png")
else:
    icon_espina = pygame.image.load("./Assets/Icons/EspinaDerrotado.png")
    jefesderrotados+=1
icon_espina = pygame.transform.scale(icon_espina, (50, 50))
posicion = pygame.Rect(435,550,50,50)
icon_espina_rect = icon_espina.get_rect(center = posicion.center)
if(flag_corvus == False):
    icon_corvus = pygame.image.load("./Assets/Icons/Corvus.png")
else:
    icon_corvus = pygame.image.load("./Assets/Icons/CorvusDerrotado.png")
    jefesderrotados+=1
icon_corvus = pygame.transform.scale(icon_corvus, (50, 50))
posicion = pygame.Rect(715,550,50,50)
icon_corvus_rect = icon_corvus.get_rect(center = posicion.center)
if(flag_galaad == False):
    icon_galaad = pygame.image.load("./Assets/Icons/Galaad.png")
else:
    icon_galaad = pygame.image.load("./Assets/Icons/GalaadDerrotado.png")
    jefesderrotados+=1
icon_galaad = pygame.transform.scale(icon_galaad, (50, 50))
posicion = pygame.Rect(435,275,50,50)
icon_galaad_rect = icon_galaad.get_rect(center = posicion.center)
icon_misionero = pygame.image.load("./Assets/Icons/Misionero.png")
icon_misionero = pygame.transform.scale(icon_misionero, (50, 50))
posicion = pygame.Rect(435,50,50,50)
icon_misionero_rect = icon_misionero.get_rect(center = posicion.center)

#Botones de Seleccion de nivel (clase Button)
but_serpico = Button.Button('Obispo Serpico',200,100,(80,600))
but_espina = Button.Button('Padre Espina',200,100,(360,600))
but_corvus = Button.Button('Fray Corvus',200,100,(640,600))
but_galaad = Button.Button('Galaad',200,100,(360,325))
but_misionero = Button.Button('El Misionero',200,100,(360,100))
but_menu = Button.Button('Salir al Menu Principal',280,50,(595,25))

#Prueba. Sale si se presiona el boton de Salir al Menu Principal (falta integrar).
while True:
    for event in pygame.event.get():
        if but_menu.get_clicked() == True:
            pygame.quit()
            sys.exit()

    #Rect.Rect.Rect.Rect.Rect.Rect.Rect.Rect.Rect.Rect.Rect.Rect.Rect.Rect.Rect...
    #Dibuja las lineas entre los niveles, y sus variantes, segun cual y cuantos jefes se han derrotado
    screen.blit(fondo,(0,0))
    pygame.draw.rect(screen,'#000000',pygame.Rect(450,200,20,400))
    pygame.draw.rect(screen,'#000000',pygame.Rect(170,485,20,50))
    pygame.draw.rect(screen,'#000000',pygame.Rect(730,485,20,50))
    pygame.draw.rect(screen,'#000000',pygame.Rect(170,485,560,20))
    pygame.draw.rect(screen,'#000000',pygame.Rect(140,535,80,65))
    if(flag_serpico == True):
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(145,540,70,65),5)
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(175,535,10,5))
    else:
         pygame.draw.rect(screen,(247,236,36),pygame.Rect(145,540,70,65),5)
    pygame.draw.rect(screen,icon_back_color,icon_serpico_rect)
    screen.blit(icon_serpico,icon_serpico_rect)
    pygame.draw.rect(screen,'#000000',pygame.Rect(420,535,80,65))
    if(flag_espina == True):
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(425,540,70,65),5)
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(455,535,10,5))
    else:
        pygame.draw.rect(screen,(247,236,36),pygame.Rect(425,540,70,65),5)
    pygame.draw.rect(screen,icon_back_color,icon_espina_rect)
    screen.blit(icon_espina,icon_espina_rect)
    pygame.draw.rect(screen,'#000000',pygame.Rect(700,535,80,65))
    if(flag_corvus == True):
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(705,540,70,65),5)
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(735,535,10,5))
    else:
        pygame.draw.rect(screen,(247,236,36),pygame.Rect(705,540,70,65),5)
    pygame.draw.rect(screen,icon_back_color,icon_corvus_rect)
    screen.blit(icon_corvus,icon_corvus_rect)
    pygame.draw.rect(screen,'#000000',pygame.Rect(420,260,80,65))
    if(flag_galaad == True):
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(425,265,70,65),5)
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(455,200,10,65))
    else:
        pygame.draw.rect(screen,(247,236,36),pygame.Rect(425,265,70,65),5)
    pygame.draw.rect(screen,icon_back_color,icon_galaad_rect)
    screen.blit(icon_galaad,icon_galaad_rect)
    pygame.draw.rect(screen,'#000000',pygame.Rect(420,35,80,65))
    pygame.draw.rect(screen,(247,236,36),pygame.Rect(425,40,70,65),5)
    pygame.draw.rect(screen,icon_back_color,icon_misionero_rect)
    screen.blit(icon_misionero,icon_misionero_rect)
    
    if jefesderrotados == 1:
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(175,497,10,38))
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(735,497,10,38))
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(455,497,10,38))
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(175,497,560,3))
    elif jefesderrotados >= 2:
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(175,490,10,45))
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(735,490,10,45))
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(455,480,10,55))
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(175,490,560,10))
        if (jefesderrotados >= 3):
            pygame.draw.rect(screen,(255,0,0),pygame.Rect(455,425,10,55))

    #Llamadas a la funcion draw de la clase Button
    but_serpico.draw(screen,True,flag_serpico)
    but_espina.draw(screen,True,flag_espina)
    but_corvus.draw(screen,True,flag_corvus)
    if(jefesderrotados >= 3):
        but_galaad.draw(screen,True,flag_galaad)
    else:
        but_galaad.draw(screen,False,flag_galaad)
    if(jefesderrotados >= 4):
        but_misionero.draw(screen,True,flag_misionero)
    else:
        but_misionero.draw(screen,False,flag_misionero)
    but_menu.draw(screen,True,False)

    pygame.display.update()
    clock.tick(60)