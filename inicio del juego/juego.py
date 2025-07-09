import pygame
import sys
import json
import os
import time

pygame.init()

#Configuración Global del Juego
WIDTH, HEIGHT = 920, 750  #Tamaño de la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Caeltronos - El Juego") 
clock = pygame.time.Clock()  

#Colores utilizados
TEXT_COLOR = (200, 190, 175) 
BLACK = (0, 0, 0) 

#Fuentes del juego
font_mono_36 = pygame.font.Font("matrix mono.ttf", 36) 
font_mono_24 = pygame.font.Font("matrix mono.ttf", 24)  

#Función para cargar configuración de audio
def cargar_config():
    """Carga la configuración de audio desde config.json."""
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            return json.load(f)
    else:
        #Si no existe el archivo, usar valores por defecto
        return {"musica": 0.5, "efectos": 0.5}

#Función para hacer un fade-in desde negro
def fade_in(duration=500):
    """Realiza un efecto de desvanecimiento desde negro."""
    start_time = pygame.time.get_ticks()  #Tiempo de inicio
    while True:
        elapsed_time = pygame.time.get_ticks() - start_time  #Tiempo transcurrido
        alpha = int(255 * (1 - (elapsed_time / duration)))  #Opacidad de 255 a 0
        if alpha <= 0:
            break  

        #Dibujar contenido del primer frame
        screen.fill(BLACK)  #Fondo negro
        game_text = font_mono_36.render("¡BIENVENIDO AL JUEGO!", True, TEXT_COLOR)
        game_rect = game_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(game_text, game_rect)

        instructions_text = font_mono_24.render("Presiona ESC para volver al menu principal", True, TEXT_COLOR)
        instructions_rect = instructions_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(instructions_text, instructions_rect)

        #Capa negra con transparencia para efecto de fade
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill(BLACK)
        fade_surface.set_alpha(max(0, alpha))  #Asegura opacidad no negativa
        screen.blit(fade_surface, (0, 0))

        pygame.display.flip()
        clock.tick(60)

#Cargar y aplicar configuración de audio
game_config = cargar_config()  #Cargar volúmenes desde config.json
pygame.mixer.music.set_volume(game_config["musica"])  #Aplicar volumen de música

#Si hay efectos de sonido, se cargarían y ajustarían aquí 
#sound_effect.set_volume(game_config["efectos"])

#Reproducir música de fondo del juego si fuera diferente
#pygame.mixer.music.load("musica_juego.mp3")
#pygame.mixer.music.play(-1)

fade_in()

#Bucle Principal del Juego
def game_loop():
    running = True  #Controla si el juego sigue en ejecución
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  

        screen.fill(BLACK)  #Limpia la pantalla en negro

        #Dibujar texto principal del juego
        game_text = font_mono_36.render("¡BIENVENIDO AL JUEGO!", True, TEXT_COLOR)
        game_rect = game_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(game_text, game_rect)

        #Dibujar instrucciones
        instructions_text = font_mono_24.render("Presiona ESC para volver al menú principal", True, TEXT_COLOR)
        instructions_rect = instructions_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(instructions_text, instructions_rect)

        pygame.display.flip()  #Actualiza la pantalla
        clock.tick(60)  

    pygame.quit()  
    sys.exit()  

#Ejecuta el bucle del juego si este archivo se ejecuta directamente
if __name__ == "__main__":
    game_loop()
