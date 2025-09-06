import pygame as py
import os
import random
from score import ScoreLevel


class Enemy:
    def __init__(self, width):
        self.score_level = ScoreLevel(800, 600)

        self.hero_x = width - 100  # Start from the right side of the screen
        self.hero_y = 320  # Ground level
        self.speed = 5  # Enemy movement speed
        self.is_attacking = False
        self.throw = True
        self.death = False
        self.death_index = 0
        self.random_enemy = ""
        self.count = 0
        self.level = self.score_level.level

        # Bomb effect position
        self.bomb_x = self.hero_x  # Bomb starts at enemy's position
        self.bomb_speed = 20  # Speed of bomb effect

        self.enemy_sword = py.mixer.Sound("./Audio/Enemy_Sword_Attack.wav")
        self.explore_item = py.mixer.Sound("./Audio/Bomb_Explode.wav")
        self.throw_item = py.mixer.Sound("./Audio/Bomb_ Throw from Enermy.wav")

        # Dictionary containing animation frame paths
        self.gobil = {
            "idle": [f"Enemies/Goblin/g_attack/g_attack_frame_{i}.gif" for i in range(8)],
            "fight": [f"Enemies/Goblin/fight/fight_frame_{i}.gif" for i in range(8)],
            "bomb": [f"Enemies/Goblin/bomb/bomb_frame_{i}.gif" for i in range(19)],
            "death": [f"Enemies/Death/death_frame_{i}.gif" for i in range(4)]
        }
        self.mushroom = {
            "idle": [f"Enemies/Mushroom/attack/attack_frame_{i}.gif" for i in range(10)],
            "fight": [f"Enemies/Mushroom/fight/fight_frame_{i}.gif" for i in range(7)],
            "bomb": [f"Enemies/Mushroom/boom/boom_frame_{i}.gif" for i in range(7)],
            "death": [f"Enemies/Death/death_frame_{i}.gif" for i in range(4)]
        }
        self.skeleton = {
            "idle": [f"Enemies/Skeleton/attack/attack_frame_{i}.gif" for i in range(7)],
            "bomb": [f"Enemies/Skeleton/bomb/bomb_frame_{i}.gif" for i in range(10)],
            "fight": [f"Enemies/Skeleton/fight/fight_frame_{i}.gif" for i in range(8)],
            "death": [f"Enemies/Death/death_frame_{i}.gif" for i in range(4)]
        }
        self.nec = {
            "idle": [f"Enemies/Nec/attack/attack_frame_{i}.gif" for i in range(13)],
            "fight": [f"Enemies/Nec/fight/fight_frame_{i}.gif" for i in range(19)],
            "bomb": [f"Enemies/Nec/attack_effect/attack_effect_frame_{i}.gif" for i in range(8)],
            "death": [f"Enemies/Death/death_frame_{i}.gif" for i in range(4)]
        }
        self.wizard = {
            "idle": [f"Enemies/Evil_Wizard/attack/attack_frame_{i}.gif" for i in range(12)],
            "fight": [f"Enemies/Evil_Wizard/fight/fight_frame_{i}.gif" for i in range(12)],
            "bomb": [f"Enemies/Evil_Wizard/move/move_frame_{i}.gif" for i in range(7)],
            "death": [f"Enemies/Death/death_frame_{i}.gif" for i in range(4)]
        }
        self.eye = {
            "idle": [f"Enemies/Flying_eye/attack/attack_frame_{i}.gif" for i in range(15)],
            "fight": [f"Enemies/Flying_eye/fight/fight_frame_{i}.gif" for i in range(15)],
            "bomb": [f"Enemies/Flying_eye/shoot/shoot_frame_{i}.gif" for i in range(7)],
            "death": [f"Enemies/Death/death_frame_{i}.gif" for i in range(4)]
        }

        self.random_enemy = random.choice([ self.mushroom, self.eye, self.gobil, self.nec, self.skeleton, self.wizard])


        # Dictionary to store loaded frames
        self.frames = {key: [py.transform.scale2x(py.image.load(frame)) for frame in paths if os.path.exists(frame)]
                       for key, paths in self.random_enemy.items()}

        # Animation state variables
        self.index = 0  # Animation index
        self.attack_index = 0
        self.bomb_index = 0  # Bomb animation index
        self.frame_counter = 0  # Frame counter for animation speed
        self.animation_speed = 5  # Adjust this value to control animation speed

    def move(self):
        self.hero_x -= self.speed  # Move enemy left

        # if self.throw:
        self.bomb_x -= self.bomb_speed  # Move bomb forward

        # If enemy moves off-screen, restart
        if self.hero_x < -100:
            self.random_enemy = random.choice([self.mushroom, self.eye, self.gobil, self.nec, self.skeleton, self.wizard])
            self.hero_x = 900  # Reset enemy to the right side of the screen
            self.is_attacking = True
            self.throw = True



        # If bomb moves off-screen, reset it
        if self.bomb_x > 800:
            self.bomb_x = self.hero_x  # Reset bomb position to enemy
            self.is_attacking = True
            self.throw = True


    def fight(self):
        self.is_attacking = True

    def defeat(self):
        self.death = True

    def draw(self, screen):

        self.frames = {key: [py.transform.scale2x(py.image.load(frame)) for frame in paths if os.path.exists(frame)]
                       for key, paths in self.random_enemy.items()}
        """Draws the enemy or bomb effect based on the current state"""
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.index = (self.index + 1) % len(self.frames["idle"])  # Loop through idle animation
            if len(self.frames['bomb']) > 10:
                self.bomb_index += 2   # Move bomb animation frame forward
            else:
                self.bomb_index += 1

        if self.bomb_index >= len(self.frames["bomb"]):
            self.explore_item.play()
            self.bomb_index = 0  # Reset bomb animation index
            self.bomb_x = self.hero_x  # Reset bomb position
            self.throw_item.play()


        if self.index >= len(self.frames["idle"]):
            self.index = 0
            self.bomb_index = 0
            self.bomb_x = self.hero_x
            self.throw_item.play()

        if self.throw:
            if self.random_enemy == random.choice([self.wizard]):
                self.count = 60
            elif self.random_enemy == random.choice([self.eye]):
                self.count = 90
            elif self.random_enemy == random.choice([self.mushroom]):
                self.count = 70
            else:
                self.count = 43
            screen.blit(self.frames["idle"][self.index], (self.hero_x, self.hero_y))
            screen.blit(self.frames["bomb"][self.bomb_index], (self.bomb_x, self.hero_y + self.count)) #for eye,wizard = 80

        if self.death:
            self.death_index = (self.death_index + 1) % len(self.frames["death"])
              # Temporarily stop throwing until next cycle
            screen.blit(self.frames["death"][self.death_index], (self.hero_x, self.hero_y))

        if self.is_attacking:
            self.attack_index = (self.attack_index + 1) % len(self.frames["fight"])

            if self.attack_index == 7:
                self.enemy_sword.play()
            if self.attack_index >= len(self.frames['fight']):
                self.attack_index = 0


            self.is_attacking = False  # Stop attack animation
            self.throw = False  # Temporarily stop throwing until next cycle
            self.bomb_index = 0
            # self.bomb_x -= 2
            screen.blit(self.frames["fight"][self.attack_index], (self.hero_x, self.hero_y))


