import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 920, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego Activo")

font = pygame.font.Font("matrix mono.ttf", 40)
texto = font.render("¡Juego Iniciado!", True, (200, 190, 175))

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 20))
    screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
