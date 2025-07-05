import pygame 
import sys
import json
import os
import time
import subprocess
from moviepy.editor import VideoFileClip

pygame.init()

#Configuración Global
WIDTH, HEIGHT = 1020, 750  #Tamaño de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Caeltronos")  
clock = pygame.time.Clock() 

#Colores usados en la interfaz
COLOR_NORMAL = (200, 190, 175)
COLOR_SELECCIONADO = (160, 150, 135)
SLIDER_COLOR = (180, 180, 180)
HANDLE_COLOR = (255, 255, 255)
TEXT_COLOR = COLOR_NORMAL
COLOR_FONDO_POPUP = (50, 50, 50)
BLACK = (0, 0, 0)

#Fuentes utilizadas
font_mono_30 = pygame.font.Font("matrix mono.ttf", 30)
font_mono_24 = pygame.font.Font("matrix mono.ttf", 24)
font_mono_20 = pygame.font.Font("matrix mono.ttf", 20)
font_mono_36 = pygame.font.Font("matrix mono.ttf", 36)

#Carga fondo y música
try:
    background_image = pygame.image.load("font.png").convert()
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    pygame.mixer.music.load("violin.mp3")
except pygame.error as e:
    print(f"Error cargando recursos: {e}")
    sys.exit()

#Función para cargar configuración guardada (volumen)
def cargar_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            return json.load(f)
    return {"musica": 0.5, "efectos": 0.5}

def guardar_config(musica, efectos):
    with open("config.json", "w") as f:
        json.dump({"musica": round(musica, 2), "efectos": round(efectos, 2)}, f)

#Cargar configuración actual y aplicar volumen a la música
config = cargar_config()
pygame.mixer.music.set_volume(config["musica"])
pygame.mixer.music.play(-1)  #Reproducir música en bucle

#Clase para fuente animada que cambia tamaño al pasar el mouse
class MatrixFont:
    def __init__(self, font_path, base_size, hover_size):
        self.font_path = font_path
        self.base_size = base_size
        self.hover_size = hover_size

    def render(self, text, selected):
        size = self.hover_size if selected else self.base_size
        font = pygame.font.Font(self.font_path, size)
        color = COLOR_SELECCIONADO if selected else COLOR_NORMAL
        return font.render(text, True, color)

#Instancia para renderizar fuente animada del menú
font_renderer_menu = MatrixFont("matrix mono.ttf", 30, 24)

#Función para desenfocar una imagen superficial
def get_blurred_surface(surface, blur_amount=5):
    if blur_amount <= 1:
        return surface
    small = pygame.transform.scale(surface, (surface.get_width() // blur_amount, surface.get_height() // blur_amount))
    return pygame.transform.scale(small, surface.get_size())

#Función para dividir y renderizar texto largo en varias líneas
def render_multiline_text(text, font, color, max_width):
    words = text.split(' ')
    lines, current = [], ""
    for word in words:
        test_line = current + (" " if current else "") + word
        if font.render(test_line, True, color).get_width() <= max_width:
            current = test_line
        else:
            if current: lines.append(current)
            current = word
    if current: lines.append(current)
    return [font.render(line, True, color) for line in lines]

#Reproduce video introductorio y luego ejecuta el juego principal
def reproducir_cinematica_y_ejecutar_juego():
    pygame.mixer.music.stop()  #Detiene la música

    try:
        clip = VideoFileClip("prologo.mp4").resize((WIDTH, HEIGHT))
        fps = clip.fps
        duration = clip.duration

        start_time = time.time()
        for frame in clip.iter_frames(fps=fps, dtype="uint8"):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "QUIT"
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "MENU"

            surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            screen.blit(surface, (0, 0))
            pygame.display.flip()
            clock.tick(fps)

        clip.close()

        screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.time.wait(2000)

        subprocess.run([sys.executable, "juego.py"], check=True) #Remplasar juego.py por el archivo que siga

    except Exception as e:
        print(f"Error al reproducir video: {e}")
        return "MENU"

    return "MENU"

#Pantalla principal del menú
def menu_screen():
    opciones = ["COMENZAR PARTIDA", "AJUSTES", "CREDITOS", "SALIR"]
    selected = -1

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return "QUIT"
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: return "QUIT"
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 and selected != -1:
                return ["CINEMATICA_VIDEO", "AJUSTES", "CREDITOS", "CONFIRM_QUIT"][selected]

        selected = -1
        for i, op in enumerate(opciones):
            if font_renderer_menu.render(op, False).get_rect(center=(WIDTH//2, HEIGHT//2 + i*60)).collidepoint(mouse_pos):
                selected = i

        screen.blit(background_image, (0, 0))
        for i, op in enumerate(opciones):
            surface = font_renderer_menu.render(op, selected == i)
            rect = surface.get_rect(center=(WIDTH//2, HEIGHT//2 + i*60))
            screen.blit(surface, rect)
        pygame.display.flip()
        clock.tick(60)

#Pantalla de configuración de volumen
def ajustes_screen():
    global config
    sliders = {
        "Música": {"x": 300, "y": 300, "value": config["musica"]},
        "Efectos": {"x": 300, "y": 400, "value": config["efectos"]}
    }
    arrastrando = None

    def draw_back_arrow():
        #Flecha para volver
        mouse_pos = pygame.mouse.get_pos()
        x, y, base, hover = 40, 40, 30, 40
        size, color = (hover if pygame.Rect(x-hover//2, y-hover//2, hover, hover).collidepoint(mouse_pos) else base), COLOR_NORMAL
        if size == hover: color = COLOR_SELECCIONADO
        points = [(x + size//2, y - size//2), (x - size//2, y), (x + size//2, y + size//2)]
        pygame.draw.polygon(screen, color, points)
        return pygame.Rect(x-hover//2, y-hover//2, hover, hover)

    def detectar_slider(mx, my):
        #Detecta si se está clickeando un slider
        for nombre, data in sliders.items():
            if pygame.Rect(data['x'], data['y'] - 10, 300, 30).collidepoint(mx, my):
                return nombre
        return None

    def draw_slider(nombre, data):
        #Dibuja un slider
        text = font_mono_30.render(f"{nombre}: {int(data['value']*100)}%", True, TEXT_COLOR)
        screen.blit(text, (data['x'], data['y'] - 40))
        pygame.draw.rect(screen, SLIDER_COLOR, (data['x'], data['y'], 300, 10))
        pygame.draw.circle(screen, HANDLE_COLOR, (int(data['x'] + data['value']*300), data['y'] + 5), 10)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        volver_rect = draw_back_arrow()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return "QUIT"
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                guardar_config(sliders["Música"]["value"], sliders["Efectos"]["value"])
                config = cargar_config()
                return "MENU"
            if e.type == pygame.MOUSEBUTTONDOWN:
                if volver_rect.collidepoint(e.pos):
                    guardar_config(sliders["Música"]["value"], sliders["Efectos"]["value"])
                    config = cargar_config()
                    return "MENU"
                arrastrando = detectar_slider(*e.pos)
            if e.type == pygame.MOUSEBUTTONUP:
                arrastrando = None
            if e.type == pygame.MOUSEMOTION and arrastrando:
                rel_x = max(0, min(300, e.pos[0] - sliders[arrastrando]["x"]))
                sliders[arrastrando]["value"] = rel_x / 300
                pygame.mixer.music.set_volume(sliders["Música"]["value"])

        screen.blit(background_image, (0, 0))
        for nombre, data in sliders.items():
            draw_slider(nombre, data)
        draw_back_arrow()
        pygame.display.flip()
        clock.tick(60)

#Pantalla para confirmar si el jugador quiere salir
def confirm_quit_screen(previous_surface):
    msg = "Estas seguro?"
    options = ["Si", "NO"]
    selected = -1
    final_msg = None
    start_time = None
    fondo = get_blurred_surface(previous_surface, 10)
    popup = pygame.Rect(140, 150, 640, 400)

    while True:
        mouse = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return "QUIT"
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return "MENU" if not final_msg else "QUIT"
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 and selected != -1 and not final_msg:
                final_msg = ("Esta bien, ¡COBARDE! Si no te da para luchar en el conclave..." if options[selected]=="Si"
                             else "¡Eso! Pelea en el conclave por el trono.")
                start_time = pygame.time.get_ticks()

        screen.blit(fondo, (0, 0))
        pygame.draw.rect(screen, COLOR_FONDO_POPUP, popup, border_radius=15)
        pygame.draw.rect(screen, TEXT_COLOR, popup, 3, border_radius=15)

        if not final_msg:
            screen.blit(font_mono_24.render(msg, True, TEXT_COLOR), (popup.centerx - 80, popup.top + 60))
            selected = -1
            for i, text in enumerate(options):
                surf = font_mono_30.render(text, True, COLOR_SELECCIONADO if
                                           pygame.Rect(popup.centerx + (i-0.5)*180, popup.bottom-90, 100, 40).collidepoint(mouse)
                                           else TEXT_COLOR)
                screen.blit(surf, surf.get_rect(center=(popup.centerx + (i-0.5)*180, popup.bottom-90)))
                if surf.get_rect(center=(popup.centerx + (i-0.5)*180, popup.bottom-90)).collidepoint(mouse):
                    selected = i
        else:
            lines = render_multiline_text(final_msg, font_mono_20, TEXT_COLOR, popup.width - 40)
            for i, l in enumerate(lines):
                screen.blit(l, l.get_rect(center=(popup.centerx, popup.top + 80 + i * 28)))
            elapsed = (pygame.time.get_ticks() - start_time) / 1000
            if "COBARDE" in final_msg:
                countdown = max(0, 10 - int(elapsed))
                cd_surface = font_mono_20.render(f"Cerrando en {countdown} segundos...", True, TEXT_COLOR)
                screen.blit(cd_surface, cd_surface.get_rect(center=(popup.centerx, popup.bottom - 60)))
                if elapsed >= 10: return "QUIT"
            else:
                if elapsed >= 3: return "MENU"

        pygame.display.flip()
        clock.tick(60)

#Loop principal del juego
current_screen = "MENU"
last_screen_surface = None

while True:
    if current_screen == "MENU":
        last_screen_surface = screen.copy()
        next_screen = menu_screen()
    elif current_screen == "AJUSTES":
        last_screen_surface = screen.copy()
        next_screen = ajustes_screen()
    elif current_screen == "CREDITOS":
        print("Mostrando créditos..."); time.sleep(2); next_screen = "MENU"
    elif current_screen == "CINEMATICA_VIDEO":
        next_screen = reproducir_cinematica_y_ejecutar_juego()
    elif current_screen == "CONFIRM_QUIT":
        next_screen = confirm_quit_screen(last_screen_surface)
    elif current_screen == "QUIT":
        break
    current_screen = next_screen

pygame.quit()
sys.exit()
