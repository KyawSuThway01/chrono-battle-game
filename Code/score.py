# score_level.py
import pygame


class ScoreLevel:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset()
        self.game_over_sound = pygame.mixer.Sound("./Audio/Game_Over Audio - (2).wav")



        # Font configuration
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)

        # Timing configuration
        self.score_increment_interval = 1000  # 1 second
        self.last_score_increment = pygame.time.get_ticks()

    def reset(self):
        """Reset all game progress"""
        self.score = 0
        self.level = 1
        self.game_over = False
        self.last_score_increment = pygame.time.get_ticks()

    def update(self):
        """Update score and level automatically"""
        if not self.game_over:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_score_increment > self.score_increment_interval:
                self.score += 10  # 10 points per second
                self.last_score_increment = current_time
                self._update_level()

    def _update_level(self):
        """Increase level based on score"""
        self.level = 1 + self.score // 100  # New level every 100 points

    def draw(self, screen):
        """Draw current score/level or game over screen"""
        if self.game_over:
            self._draw_game_over(screen)
        else:
            self._draw_hud(screen)

    def _draw_hud(self, screen):
        """Draw in-game HUD"""
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        level_text = self.font.render(f"Level: {self.level}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))

    def _draw_game_over(self, screen):
        """Draw game over screen"""
        # Dark overlay
        pygame.mixer.music.stop()  # Stop the menu background music
        pygame.mixer.music.set_volume(80 / 100)  # Adjust volume
        pygame.mixer.music.play(-1)
        pygame.mixer.music.load("./Audio/Game_Over Audio - (2).wav")  # Load the game music
        overlay = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        screen.blit(overlay, (0, 0))

        # Game Over text
        game_over_text = self.big_font.render("GAME OVER", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
        screen.blit(game_over_text, text_rect)

        # Score display
        final_score_text = self.font.render(f"Final Score: {self.score}  Level: {self.level}", True, (255, 255, 255))
        score_rect = final_score_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 50))
        screen.blit(final_score_text, score_rect)

        # Restart instruction
        restart_text = self.font.render("Press TAB Key to restart", True, (200, 200, 200))
        restart_rect = restart_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 150))
        screen.blit(restart_text, restart_rect)

    def handle_input(self, event):
        """Handle restart input"""
        if self.game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                self.reset()
                return True  # Signal to restart game
        return False