import pygame
import sys
import json
import os
import time
import subprocess
from moviepy.editor import VideoFileClip

class Game:
    def __init__(self):
        pygame.init()

        # Configuración Global
        self.WIDTH, self.HEIGHT = 1020, 750  # Tamaño de la ventana
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Caeltronos")
        self.clock = pygame.time.Clock()

        # Colores usados en la interfaz
        self.COLOR_NORMAL = (200, 190, 175)
        self.COLOR_SELECCIONADO = (160, 150, 135)
        self.SLIDER_COLOR = (180, 180, 180)
        self.HANDLE_COLOR = (255, 255, 255)
        self.TEXT_COLOR = self.COLOR_NORMAL
        self.COLOR_FONDO_POPUP = (50, 50, 50)
        self.BLACK = (0, 0, 0)

        # Fuentes utilizadas
        self.font_mono_30 = pygame.font.Font("matrix mono.ttf", 30)
        self.font_mono_24 = pygame.font.Font("matrix mono.ttf", 24)
        self.font_mono_20 = pygame.font.Font("matrix mono.ttf", 20)
        self.font_mono_36 = pygame.font.Font("matrix mono.ttf", 36)

        # Carga fondo y música
        try:
            self.background_image = pygame.image.load("font.png").convert()
            self.background_image = pygame.transform.scale(self.background_image, (self.WIDTH, self.HEIGHT))
            pygame.mixer.music.load("violin.mp3")
        except pygame.error as e:
            print(f"Error cargando recursos: {e}")
            sys.exit()

        # Cargar configuración actual y aplicar volumen a la música
        self.config = self._cargar_config()
        pygame.mixer.music.set_volume(self.config["musica"])
        pygame.mixer.music.play(-1)  # Reproducir música en bucle

        # Instancia para renderizar fuente animada del menú
        self.font_renderer_menu = self.MatrixFont("matrix mono.ttf", 30, 24)

        # Estado del juego
        self.current_screen_name = "MENU"
        self.current_screen = self.MenuScreen(self.screen, self.clock, self.background_image, self.font_renderer_menu, self)
        self.last_screen_surface = None # Para la pantalla de confirmación de salida

    # --- Métodos de Utilidad ---
    def _cargar_config(self):
        if os.path.exists("config.json"):
            with open("config.json", "r") as f:
                return json.load(f)
        return {"musica": 0.5, "efectos": 0.5}

    def _guardar_config(self, musica, efectos):
        with open("config.json", "w") as f:
            json.dump({"musica": round(musica, 2), "efectos": round(efectos, 2)}, f)

    def _get_blurred_surface(self, surface, blur_amount=5):
        if blur_amount <= 1:
            return surface
        small = pygame.transform.scale(surface, (surface.get_width() // blur_amount, surface.get_height() // blur_amount))
        return pygame.transform.scale(small, surface.get_size())

    def _render_multiline_text(self, text, font, color, max_width):
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

    def _reproducir_cinematica_y_ejecutar_juego(self):
        pygame.mixer.music.stop()  # Detiene la música

        try:
            clip = VideoFileClip("prologo.mp4").resize((self.WIDTH, self.HEIGHT))
            fps = clip.fps
            # duration = clip.duration # No se usa

            # start_time = time.time() # No se usa
            for frame in clip.iter_frames(fps=fps, dtype="uint8"):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return "QUIT"
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return "MENU"

                surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
                self.screen.blit(surface, (0, 0))
                pygame.display.flip()
                self.clock.tick(fps)

            clip.close()

            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            pygame.time.wait(2000)

            subprocess.run([sys.executable, "juego.py"], check=True) # Reemplazar juego.py por el archivo que siga

        except Exception as e:
            print(f"Error al reproducir video: {e}")
            return "MENU"

        return "MENU"

    # --- Clases Anidadas (para mantener la encapsulación) ---
    class MatrixFont:
        def __init__(self, font_path, base_size, hover_size):
            self.font_path = font_path
            self.base_size = base_size
            self.hover_size = hover_size

        def render(self, text, selected):
            size = self.hover_size if selected else self.base_size
            font = pygame.font.Font(self.font_path, size)
            color = (160, 150, 135) if selected else (200, 190, 175) # Usar colores directamente o pasar desde Game
            return font.render(text, True, color)

    class MenuItem:
        def __init__(self, text, action, y_offset, font_renderer, game_instance):
            self.text = text
            self.action = action
            self.y_offset = y_offset
            self.font_renderer = font_renderer
            self.rect = None
            self.game = game_instance # Referencia a la instancia de Game

        def draw(self, surface, mouse_pos):
            selected = self.is_hovered(mouse_pos)
            rendered_text = self.font_renderer.render(self.text, selected)
            self.rect = rendered_text.get_rect(center=(self.game.WIDTH // 2, self.game.HEIGHT // 2 + self.y_offset))
            surface.blit(rendered_text, self.rect)

        def is_hovered(self, mouse_pos):
            if self.rect:
                return self.rect.collidepoint(mouse_pos)
            return False

    class GameScreen:
        def __init__(self, screen, clock, background_image, game_instance):
            self.screen = screen
            self.clock = clock
            self.background_image = background_image
            self.next_screen = None
            self.game = game_instance # Referencia a la instancia de Game

        def handle_event(self, event):
            pass

        def update(self):
            pass

        def draw(self):
            self.screen.blit(self.background_image, (0, 0))

    class MenuScreen(GameScreen):
        def __init__(self, screen, clock, background_image, font_renderer_menu, game_instance):
            super().__init__(screen, clock, background_image, game_instance)
            self.font_renderer_menu = font_renderer_menu
            menu_items_data = [
                ("COMENZAR PARTIDA", "CINEMATICA_VIDEO", 0),
                ("AJUSTES", "AJUSTES", 60),
                ("CREDITOS", "CREDITOS", 120),
                ("SALIR", "CONFIRM_QUIT", 180)
            ]
            self.menu_items = []
            for text, action, y_offset in menu_items_data:
                self.menu_items.append(self.game.MenuItem(text, action, y_offset, self.font_renderer_menu, self.game))

        def handle_event(self, event):
            if event.type == pygame.QUIT:
                self.next_screen = "QUIT"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.next_screen = "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for item in self.menu_items:
                    if item.is_hovered(mouse_pos):
                        self.next_screen = item.action

        def draw(self):
            super().draw()
            mouse_pos = pygame.mouse.get_pos()
            for item in self.menu_items:
                item.draw(self.screen, mouse_pos)
            pygame.display.flip()

    class AjustesScreen(GameScreen):
        def __init__(self, screen, clock, background_image, current_config, game_instance):
            super().__init__(screen, clock, background_image, game_instance)
            self.config = current_config
            self.sliders = {
                "Música": {"x": 300, "y": 300, "value": self.config["musica"]},
                "Efectos": {"x": 300, "y": 400, "value": self.config["efectos"]}
            }
            self.arrastrando = None
            self.volver_rect = None

        def _draw_back_arrow(self):
            mouse_pos = pygame.mouse.get_pos()
            x, y, base, hover = 40, 40, 30, 40
            size, color = (hover if pygame.Rect(x-hover//2, y-hover//2, hover, hover).collidepoint(mouse_pos) else base), self.game.COLOR_NORMAL
            if size == hover: color = self.game.COLOR_SELECCIONADO
            points = [(x + size//2, y - size//2), (x - size//2, y), (x + size//2, y + size//2)]
            pygame.draw.polygon(self.screen, color, points)
            return pygame.Rect(x-hover//2, y-hover//2, hover, hover)

        def _detectar_slider(self, mx, my):
            for nombre, data in self.sliders.items():
                if pygame.Rect(data['x'], data['y'] - 10, 300, 30).collidepoint(mx, my):
                    return nombre
            return None

        def _draw_slider(self, nombre, data):
            text = self.game.font_mono_30.render(f"{nombre}: {int(data['value']*100)}%", True, self.game.TEXT_COLOR)
            self.screen.blit(text, (data['x'], data['y'] - 40))
            pygame.draw.rect(self.screen, self.game.SLIDER_COLOR, (data['x'], data['y'], 300, 10))
            pygame.draw.circle(self.screen, self.game.HANDLE_COLOR, (int(data['x'] + data['value']*300), data['y'] + 5), 10)

        def handle_event(self, event):
            if event.type == pygame.QUIT:
                self.next_screen = "QUIT"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game._guardar_config(self.sliders["Música"]["value"], self.sliders["Efectos"]["value"])
                self.game.config = self.game._cargar_config() # Recargar la configuración global
                self.next_screen = "MENU"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.volver_rect and self.volver_rect.collidepoint(event.pos):
                    self.game._guardar_config(self.sliders["Música"]["value"], self.sliders["Efectos"]["value"])
                    self.game.config = self.game._cargar_config() # Recargar la configuración global
                    self.next_screen = "MENU"
                self.arrastrando = self._detectar_slider(*event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.arrastrando = None
            elif event.type == pygame.MOUSEMOTION and self.arrastrando:
                rel_x = max(0, min(300, event.pos[0] - self.sliders[self.arrastrando]["x"]))
                self.sliders[self.arrastrando]["value"] = rel_x / 300
                if self.arrastrando == "Música":
                    pygame.mixer.music.set_volume(self.sliders["Música"]["value"])

        def draw(self):
            super().draw()
            for nombre, data in self.sliders.items():
                self._draw_slider(nombre, data)
            self.volver_rect = self._draw_back_arrow()
            pygame.display.flip()

    class ConfirmQuitScreen(GameScreen):
        def __init__(self, screen, clock, previous_surface, game_instance):
            super().__init__(screen, clock, None, game_instance) # No usa background_image directamente
            self.msg = "Estas seguro?"
            self.options = ["Si", "NO"]
            self.selected = -1
            self.final_msg = None
            self.start_time = None
            self.fondo = self.game._get_blurred_surface(previous_surface, 10)
            self.popup = pygame.Rect(140, 150, 640, 400)

        def handle_event(self, event):
            if event.type == pygame.QUIT:
                self.next_screen = "QUIT"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.next_screen = "MENU" if not self.final_msg else "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.selected != -1 and not self.final_msg:
                self.final_msg = ("Esta bien, ¡COBARDE! Si no te da para luchar en el conclave..." if self.options[self.selected]=="Si"
                                   else "¡Eso! Pelea en el conclave por el trono.")
                self.start_time = pygame.time.get_ticks()

        def update(self):
            if self.final_msg:
                elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
                if "COBARDE" in self.final_msg:
                    if elapsed >= 10:
                        self.next_screen = "QUIT"
                else:
                    if elapsed >= 3:
                        self.next_screen = "MENU"

        def draw(self):
            self.screen.blit(self.fondo, (0, 0))
            pygame.draw.rect(self.screen, self.game.COLOR_FONDO_POPUP, self.popup, border_radius=15)
            pygame.draw.rect(self.screen, self.game.TEXT_COLOR, self.popup, 3, border_radius=15)

            if not self.final_msg:
                self.screen.blit(self.game.font_mono_24.render(self.msg, True, self.game.TEXT_COLOR), (self.popup.centerx - 80, self.popup.top + 60))
                self.selected = -1
                mouse = pygame.mouse.get_pos()
                for i, text in enumerate(self.options):
                    option_rect = pygame.Rect(self.popup.centerx + (i-0.5)*180 - 50, self.popup.bottom-90 - 20, 100, 40)
                    surf = self.game.font_mono_30.render(text, True, self.game.COLOR_SELECCIONADO if option_rect.collidepoint(mouse) else self.game.TEXT_COLOR)
                    self.screen.blit(surf, surf.get_rect(center=(self.popup.centerx + (i-0.5)*180, self.popup.bottom-90)))
                    if option_rect.collidepoint(mouse):
                        self.selected = i
            else:
                lines = self.game._render_multiline_text(self.final_msg, self.game.font_mono_20, self.game.TEXT_COLOR, self.popup.width - 40)
                for i, l in enumerate(lines):
                    self.screen.blit(l, l.get_rect(center=(self.popup.centerx, self.popup.top + 80 + i * 28)))
                elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
                if "COBARDE" in self.final_msg:
                    countdown = max(0, 10 - int(elapsed))
                    cd_surface = self.game.font_mono_20.render(f"Cerrando en {countdown} segundos...", True, self.game.TEXT_COLOR)
                    self.screen.blit(cd_surface, cd_surface.get_rect(center=(self.popup.centerx, self.popup.bottom - 60)))

            pygame.display.flip()

    # --- Bucle Principal del Juego ---
    def run(self):
        running = True
        while running:
            if self.current_screen.next_screen:
                next_screen_name = self.current_screen.next_screen
                self.current_screen.next_screen = None # Resetear para la próxima iteración

                if next_screen_name == "QUIT":
                    running = False
                elif next_screen_name == "MENU":
                    self.current_screen = self.MenuScreen(self.screen, self.clock, self.background_image, self.font_renderer_menu, self)
                elif next_screen_name == "AJUSTES":
                    self.last_screen_surface = self.screen.copy() # Guardar la pantalla actual antes de ir a ajustes
                    self.current_screen = self.AjustesScreen(self.screen, self.clock, self.background_image, self.config, self)
                elif next_screen_name == "CREDITOS":
                    print("Mostrando créditos..."); time.sleep(2)
                    self.current_screen = self.MenuScreen(self.screen, self.clock, self.background_image, self.font_renderer_menu, self) # Volver al menú después de créditos
                elif next_screen_name == "CINEMATICA_VIDEO":
                    result = self._reproducir_cinematica_y_ejecutar_juego()
                    if result == "QUIT":
                        running = False
                    else:
                        self.current_screen = self.MenuScreen(self.screen, self.clock, self.background_image, self.font_renderer_menu, self) # Volver al menú si la cinemática termina o falla
                elif next_screen_name == "CONFIRM_QUIT":
                    self.last_screen_surface = self.screen.copy() # Guardar la pantalla actual antes de la confirmación
                    self.current_screen = self.ConfirmQuitScreen(self.screen, self.clock, self.last_screen_surface, self)
                self.current_screen_name = next_screen_name # Actualizar el nombre de la pantalla actual

            for event in pygame.event.get():
                self.current_screen.handle_event(event)

            self.current_screen.update()
            self.current_screen.draw()

            self.clock.tick(60)

        pygame.quit()
        sys.exit()

# Para ejecutar el juego
if __name__ == "__main__":
    game = Game()
    game.run()
