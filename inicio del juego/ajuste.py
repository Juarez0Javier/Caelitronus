import pygame
import sys
import subprocess
import json
import os

pygame.init()

def cargar_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            return json.load(f)
    else:
        return {"musica": 0.5, "efectos": 0.5}

def guardar_config(musica, efectos):
    with open("config.json", "w") as f:
        json.dump({
            "musica": round(musica, 2),
            "efectos": round(efectos, 2)
        }, f)

config = cargar_config()

WIDTH, HEIGHT = 920, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ajustes de Audio")

SLIDER_COLOR = (180, 180, 180)
HANDLE_COLOR = (255, 255, 255)
TEXT_COLOR = (200, 190, 175)

background = pygame.image.load("font.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background.set_alpha(100)

font = pygame.font.Font("matrix mono.ttf", 30)

sliders = {
    "Música": {"x": 300, "y": 300, "value": config["musica"]},
    "Efectos": {"x": 300, "y": 400, "value": config["efectos"]}
}

def draw_slider(nombre, data):
    text = font.render(f"{nombre}: {int(data['value'] * 100)}%", True, TEXT_COLOR)
    screen.blit(text, (data['x'], data['y'] - 40))
    pygame.draw.rect(screen, SLIDER_COLOR, (data['x'], data['y'], 300, 10))
    handle_x = int(data['x'] + data['value'] * 300)
    pygame.draw.circle(screen, HANDLE_COLOR, (handle_x, data['y'] + 5), 10)

def detectar_slider(mouse_x, mouse_y):
    for nombre, data in sliders.items():
        rect = pygame.Rect(data['x'], data['y'] - 10, 300, 30)
        if rect.collidepoint(mouse_x, mouse_y):
            return nombre
    return None

def draw_volver():
    volver_text = font.render("← VOLVER", True, TEXT_COLOR)
    rect = volver_text.get_rect(topleft=(20, 20))
    screen.blit(volver_text, rect)
    return rect

clock = pygame.time.Clock()
arrastrando = None
running = True
musica_reproduciendo = False

while running:
    screen.blit(background, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    volver_rect = draw_volver()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if volver_rect.collidepoint(event.pos):
                    guardar_config(sliders["Música"]["value"], sliders["Efectos"]["value"])
                    pygame.quit()
                    subprocess.run(["python", "main.py"])
                    sys.exit()
                arrastrando = detectar_slider(*event.pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            arrastrando = None
            pygame.mixer.music.stop()
            musica_reproduciendo = False

        elif event.type == pygame.MOUSEMOTION and arrastrando:
            x = sliders[arrastrando]["x"]
            rel_x = max(0, min(300, event.pos[0] - x))
            sliders[arrastrando]["value"] = rel_x / 300

            if arrastrando == "Música":
                if not musica_reproduciendo:
                    try:
                        pygame.mixer.music.load("violin.mp3")
                        pygame.mixer.music.play(-1)
                        musica_reproduciendo = True
                    except:
                        pass
                pygame.mixer.music.set_volume(sliders["Música"]["value"])

    for nombre, data in sliders.items():
        draw_slider(nombre, data)

    pygame.display.flip()
    clock.tick(60)

guardar_config(sliders["Música"]["value"], sliders["Efectos"]["value"])
pygame.quit()
sys.exit()
