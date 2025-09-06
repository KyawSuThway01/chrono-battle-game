import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
BUTTON_COLOR = (70, 130, 180)
HOVER_COLOR = (100, 150, 200)
SLIDER_COLOR = (200, 200, 200)
SLIDER_HANDLE_COLOR = (255, 50, 50)

# Load font
font = pygame.font.Font(None, 50)


class Settings:
    def __init__(self):
        self.light_value = 50  # Initial light level (0-100)
        self.sound_value = 50  # Initial sound level (0-100)
        self.selected_slider = None

    def draw_text(self, text, x, y):
        text_obj = font.render(text, True, WHITE)
        text_rect = text_obj.get_rect(center=(x, y))
        screen.blit(text_obj, text_rect)

    def draw_slider(self, x, y, value, label):
        pygame.draw.rect(screen, SLIDER_COLOR, (x, y, 200, 10))
        handle_x = x + (value * 2)
        pygame.draw.circle(screen, SLIDER_HANDLE_COLOR, (handle_x, y + 5), 10)
        self.draw_text(f"{label}: {value}%", x + 100, y - 20)

    def settings_screen(self):
        running = True
        while running:
            screen.fill(BLACK)
            self.draw_text("Settings", WIDTH // 2, 50)
            self.draw_text("Press ESC to return", WIDTH // 2, HEIGHT - 50)

            # Draw sliders
            self.draw_slider(300, 200, self.light_value, "Light")
            self.draw_slider(300, 300, self.sound_value, "Sound")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if 190 <= my <= 210:
                        self.selected_slider = "light"
                    elif 290 <= my <= 310:
                        self.selected_slider = "sound"
                if event.type == pygame.MOUSEBUTTONUP:
                    self.selected_slider = None
                if event.type == pygame.MOUSEMOTION and self.selected_slider:
                    mx, my = pygame.mouse.get_pos()
                    new_value = min(100, max(0, (mx - 300) // 2))
                    if self.selected_slider == "light":
                        self.light_value = new_value
                    elif self.selected_slider == "sound":
                        self.sound_value = new_value

            pygame.display.update()


if __name__ == "__main__":
    settings = Settings()
    settings.settings_screen()
