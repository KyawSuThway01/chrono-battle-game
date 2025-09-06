import pygame
import sys
from main import run_game  # Import your game function
from PIL import Image


def extract_gif_frames(gif_path):
    gif = Image.open(gif_path)
    frames = []
    try:
        while True:
            frame = gif.copy()
            frames.append(frame.convert("RGBA"))
            gif.seek(len(frames))  # Move to the next frame
    except EOFError:
        pass
    return frames

def convert_frames_to_surfaces(frames):
    pygame_frames = []
    for frame in frames:
        mode = frame.mode
        size = frame.size
        data = frame.tobytes()
        pygame_frame = pygame.image.fromstring(data, size, mode)
        pygame_frames.append(pygame_frame)
    return pygame_frames

# Initialize pygame
pygame.init()

# Global variables
light_level = 80  # Default light level (0-100)
sound_level = 80  # Default sound level (0-100)

# Load background music
pygame.mixer.init()
pygame.mixer.music.load("./Audio/Game Start Menu Audio.wav")  # Replace with your music file
pygame.mixer.music.set_volume(sound_level)  # Adjust volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # Loop indefinitely



# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
BUTTON_COLOR = (70, 130, 180)
HOVER_COLOR = (255, 200, 0)

# Load font
font = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 25) #Libre_Baskerville,Monomakh/Libre_Baskerville/LibreBaskerville-Regular.ttf

# Load GIF frames
gif_frames = extract_gif_frames('./background_image/output.gif')  # Replace with your GIF path
pygame_frames = convert_frames_to_surfaces(gif_frames)
current_frame = 0
frame_delay = 100  # Delay between frames in milliseconds
last_frame_time = pygame.time.get_ticks()

# Load settings background image
settings_bg = pygame.image.load("./background_image/Setting.jpg")
about_bg = pygame.image.load("./background_image/About us.jpg")


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def draw_button(surface, color, hover_color, rect, text, text_color):
    mx, my = pygame.mouse.get_pos()
    if rect.collidepoint((mx, my)):
        pygame.draw.rect(surface, hover_color, rect, border_radius=10)
    else:
        pygame.draw.rect(surface, color, rect, border_radius=10)
    draw_text(text, font, text_color, surface, rect.centerx, rect.centery)

def apply_light_effect(surface, light_level):
    """Apply a brightness overlay based on the light level."""
    brightness = light_level / 100  # Normalize light level to a range of 0 to 1
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.fill((0, 0, 0))
    overlay.set_alpha(int(255 * (1 - brightness)))  # Adjust transparency based on light level
    surface.blit(overlay, (0, 0))

def main_menu():
    global current_frame, last_frame_time, light_level

    while True:
        screen.fill(BLACK)  # Clear screen

        # Animate GIF background (if applicable)
        current_time = pygame.time.get_ticks()
        if current_time - last_frame_time > frame_delay:
            current_frame = (current_frame + 1) % len(pygame_frames)
            last_frame_time = current_time
        screen.blit(pygame_frames[current_frame], (0, 0))

        # Apply light effect to the background_image menu
        apply_light_effect(screen, light_level)

        # Buttons
        start_button = pygame.Rect(300, 200, 200, 60)
        settings_button = pygame.Rect(300, 300, 200, 60)
        about_button = pygame.Rect(300, 400, 200, 60)

        # Draw buttons
        draw_button(screen, BUTTON_COLOR, HOVER_COLOR, start_button, "Start", WHITE)
        draw_button(screen, BUTTON_COLOR, HOVER_COLOR, settings_button, "Settings", WHITE)
        draw_button(screen, BUTTON_COLOR, HOVER_COLOR, about_button, "About", WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if start_button.collidepoint((mx, my)):

                    run_game()  # Start game function
                elif settings_button.collidepoint((mx, my)):
                    settings_screen()
                elif about_button.collidepoint((mx, my)):
                    about_screen()

        pygame.display.update()

def settings_screen():
    global light_level, sound_level

    running = True
    slider_width = 200
    slider_height = 20
    sound_slider = pygame.Rect(300, 200, slider_width, slider_height)
    light_slider = pygame.Rect(300, 300, slider_width, slider_height)
    dragging_sound = False
    dragging_light = False

    while running:
        screen.blit(settings_bg, (0, 0))  # Draw settings background
        draw_text("S e t t i n g s", pygame.font.Font(
            "./Libre_Baskerville,Monomakh/Libre_Baskerville/LibreBaskerville-Italic.ttf", 50), (255, 0, 0), screen, WIDTH // 2, HEIGHT // 2 - 180)

        draw_text("Press ESC to return", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 200)

        # Draw sound slider
        pygame.draw.rect(screen, GRAY, sound_slider, border_radius=10)
        sound_handle = pygame.Rect(300 + int((sound_level / 100) * slider_width) - 10, 195, 20, 30)
        pygame.draw.rect(screen, BUTTON_COLOR, sound_handle, border_radius=10)
        draw_text(f"Sound: {sound_level}%", font, WHITE, screen, WIDTH // 2, 170)

        # Draw light slider
        pygame.draw.rect(screen, GRAY, light_slider, border_radius=10)
        light_handle = pygame.Rect(300 + int((light_level / 100) * slider_width) - 10, 295, 20, 30)
        pygame.draw.rect(screen, BUTTON_COLOR, light_handle, border_radius=10)
        draw_text(f"Light: {light_level}%", font, WHITE, screen, WIDTH // 2, 270)

        # Apply light effect to the settings screen
        apply_light_effect(screen, light_level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or pygame.K_RIGHT or pygame.K_LEFT:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if sound_handle.collidepoint((mx, my)):
                    dragging_sound = True
                if light_handle.collidepoint((mx, my)):
                    dragging_light = True
            if event.type == pygame.MOUSEBUTTONUP:
                dragging_sound = False
                dragging_light = False
            if event.type == pygame.MOUSEMOTION:
                if dragging_sound:
                    mx, my = pygame.mouse.get_pos()
                    sound_level = int(((mx - 300) / slider_width) * 100)
                    sound_level = max(0, min(100, sound_level))
                    pygame.mixer.music.set_volume(sound_level / 100)  # Adjust volume correctly
                if dragging_light:
                    mx, my = pygame.mouse.get_pos()
                    light_level = int(((mx - 300) / slider_width) * 100)
                    light_level = max(0, min(100, light_level))

        pygame.display.update()

def about_screen():
    running = True
    while running:
        screen.blit(about_bg, (0, 0))

        draw_text("Chrono Battle", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 140)
        draw_text("Chrono Battle is an action-packed game where", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 100)
        draw_text("you play as a brave warrior fighting against powerful enemies.", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 80)
        draw_text("Your goal is to survive, defeat enemies,", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 60)
        draw_text("and level up as the game gets harder.", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 40)

        draw_text("In this adventure, time and speed are your biggest challenges.", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 10)
        draw_text("As you progress, the game becomes faster, and enemies get stronger.", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 30)
        draw_text("You must jump, attack, and dodge to stay alive.", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 50)

        draw_text(" Features ", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 85)
        draw_text(" Exciting combat with cool attack moves", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 120)
        draw_text(" Increasing speed and difficulty at every level", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 140)
        draw_text(" Epic background music and sound effects", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 160)
        draw_text(" Score system to track your progress", font_small, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 180)

        # draw_text("Press ESC to return", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 220)

        # Apply light effect to the about screen
        apply_light_effect(screen, light_level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or pygame.K_LEFT or pygame.K_RIGHT:
                    running = False

        pygame.display.update()


if __name__ == "__main__":
    main_menu()