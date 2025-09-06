import pygame
import pygame as py
from hero import Hero
from enemies import Enemy
from score import ScoreLevel
import random

def run_game():
    # Initialize Pygame
    py.init()
    pygame.mixer.music.stop()  # Stop the menu background music
    pygame.mixer.music.load("./Audio/Game Background Audio.wav")  # Load the game music
    pygame.mixer.music.set_volume(1)  # Adjust volume
    pygame.mixer.music.play(-1)  # Play the new music in a loop



    # Load game over sound
    game_over_sound = py.mixer.Sound("./Audio/Game_Over Audio - (2).wav")
    game_over_sound.set_volume(1.0)

    # Screen dimensions
    width = 800
    height = 600
    screen = py.display.set_mode((width, height))
    py.display.set_caption("Chrono Battle")

    hit = py.mixer.Sound("./Audio/Damage Hit Screen.wav")


    # Background properties
    bg_offset = 0
    speed = 5

    # Create instances
    hero = Hero(width)
    enemy = Enemy(800)
    score_level = ScoreLevel(width, height)

    running = True
    game_over = False
    clock = py.time.Clock()

    while running:

        if score_level.level == 1:
            background = py.image.load('./background_image/bk_level_one.jpg')
            background = py.transform.scale(background, (width, height))  # Scale background to screen size
        elif score_level.level == 3:
            background = py.image.load('./background_image/bk_level_two.jpg')
            background = py.transform.scale(background, (width, height))  # Scale background to screen size
        elif score_level.level == 6:
            background = py.image.load('./background_image/bk_level_3.jpg')
            background = py.transform.scale(background, (width, height))  # Scale background to screen size


        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

            if score_level.handle_input(event):  # Reset game if button pressed
                pygame.mixer.music.stop()  # Stop the menu background music
                pygame.mixer.music.load("./Audio/Game Background Audio.wav")  # Load the game music
                pygame.mixer.music.set_volume(1)  # Adjust volume
                pygame.mixer.music.play(-1)  # Play the new music in a loop
                hero = Hero(width)
                enemy = Enemy(800)
                score_level = ScoreLevel(width, height)
                game_over = False
                speed = 5

        if not game_over:

            keys = py.key.get_pressed()
            if keys[py.K_SPACE]:
                hero.handle_jump()
            elif keys[py.K_w]:  # Press 'W' to trigger attack1
                if not hero.attacking:
                    hero.handle_attack1()
            elif keys[py.K_s]:
                hero.handle_attack2()

            # Update hero and background
            hero.update()
            bg_offset -= speed
            if bg_offset <= -width:
                bg_offset = 0

            # Drawing the screen
            screen.fill((0, 255, 255))
            screen.blit(background, (bg_offset, 0))
            screen.blit(background, (bg_offset + width, 0))

            # Move and draw enemy
            enemy.move()
            enemy.draw(screen)

            # Draw the hero
            hero.draw(screen)

            # Update and draw score
            score_level.update()
            score_level.draw(screen)

            # Adjust speed based on score
            #   # Increase speed by 1 every 100 points
            # Adjust speed based on score
            if score_level.score % 100 == 0 and speed < 20:
                speed += 0.1  # Increase speed by 1 every 100 points
                enemy.speed += 0.1
                hero.speed += 0.1
                enemy.bomb_speed += 0.1

            # Collision detection
            hero_pos = pygame.Vector2(hero.hero_x, hero.hero_y)
            enemy_pos = pygame.Vector2(enemy.hero_x, enemy.hero_y)
            bomb_pos = pygame.Vector2(enemy.bomb_x, enemy.hero_y + 42)
            # if hero_pos.distance_to(enemy_pos) < 80:

            if hero_pos.distance_to(bomb_pos) < 80:

                if hero.hit_index == 0:
                    hit.play()
                elif hero.hit_index == 2:
                    hit.play()

                hero.take_damage(3)
                if hero.current_health <= 0:
                    game_over_sound.play()
                    score_level.game_over = True
                    score_level.draw(screen)
            if hero_pos.x < enemy_pos.x and hero_pos.distance_to(enemy_pos) < 50  and hero.attacking :
                enemy.throw = False
                enemy.death = False
            else:
                if enemy.hero_x < -20:
                    enemy.throw = True
                    enemy.random_enemy = random.choice(
                        [enemy.mushroom, enemy.eye, enemy.gobil, enemy.nec, enemy.skeleton, enemy.wizard])
                    enemy.hero_x = 800

            py.display.flip()
            clock.tick(10)

    py.quit()


