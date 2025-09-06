import pygame as py
import os
import time

class Hero:
    def __init__(self, width):
        # Character properties
        self.hero_x = width // 2 - (300 // 2)
        self.hero_y = 320  # Ground level
        self.speed = 10
        self.jumping = False
        self.filling = False
        self.dying = False  # New death state
        self.jump_index = 0
        self.fill_index = 0
        self.death_index = 0  # New death animation index
        self.jump_velocity = 23  # Initial jump velocity
        self.gravity = 2  # Gravity force
        self.count = 0

        # Health properties
        self.max_health = 100
        self.current_health = 100
        self.health_bar_width = 100  # Width of full health bar

        self.hitting = False
        self.hit_index = 0

        self.attacking = False
        self.attack_index = 0

        self.attacking_two = False

        self.jump_sound = py.mixer.Sound("./Audio/Player_Jumping.wav")  # Replace with your jump sound file
        self.jump_fall = py.mixer.Sound("./Audio/Player_Jump_Fall.wav")
        self.sword = py.mixer.Sound("./Audio/Player_Sword_Attack.wav")

        # Animation frames
        self.run_frames = ['hero/Run/run_frame_0.gif', 'hero/Run/run_frame_1.gif', 'hero/Run/run_frame_2.gif',
                           'hero/Run/run_frame_3.gif', 'hero/Run/run_frame_4.gif', 'hero/Run/run_frame_5.gif',
                           'hero/Run/run_frame_6.gif', 'hero/Run/run_frame_7.gif']
        self.jump_frames = ['hero/Jump/jump_frame_0.gif', 'hero/Jump/jump_frame_1.gif', 'hero/Jump/jump_frame_2.gif']
        self.fill_frames = ['hero/Fill/fill_frame_0.gif', 'hero/Fill/fill_frame_1.gif', 'hero/Fill/fill_frame_2.gif']
        self.death_frames = ['hero/Death/death_frame_0.gif', 'hero/Death/death_frame_1.gif', 'hero/Death/death_frame_2.gif',
                             'hero/Death/death_frame_3.gif', 'hero/Death/death_frame_4.gif', 'hero/Death/death_frame_5.gif',
                             'hero/Death/death_frame_6.gif']
        self.hit_frames = ['hero/hit/hit_frame_0.gif', 'hero/hit/hit_frame_1.gif', 'hero/hit/hit_frame_2.gif']
        self.attack1_frames = ['hero/attack1/attack1_frame_0.gif', 'hero/attack1/attack1_frame_1.gif', 'hero/attack1/attack1_frame_2.gif'
                               'hero/attack1/attack1_frame_3.gif', 'hero/attack1/attack1_frame_4.gif', 'hero/attack1/attack1_frame_5.gif',
                               'hero/attack1/attack1_frame_6.gif']
        self.attack2_frames = ['hero/attack2/attack1_frame_0.gif', 'hero/attack2/attack1_frame_1.gif',
                               'hero/attack2/attack1_frame_2.gif'
                               'hero/attack2/attack1_frame_3.gif', 'hero/attack2/attack1_frame_4.gif',
                               'hero/attack2/attack1_frame_5.gif',
                               'hero/attack2/attack1_frame_6.gif']
        # Load animation frames
        self.run_frame = [py.transform.scale2x(py.image.load(run)) for run in self.run_frames if os.path.exists(run)]
        self.jump_frame = [py.transform.scale2x(py.image.load(jump)) for jump in self.jump_frames if
                           os.path.exists(jump)]
        self.fill_frame = [py.transform.scale2x(py.image.load(fill)) for fill in self.fill_frames if
                           os.path.exists(fill)]
        self.death_frame = [py.transform.scale2x(py.image.load(death)) for death in self.death_frames if
                            os.path.exists(death)]
        self.hit_frame = [py.transform.scale2x(py.image.load(hit)) for hit in self.hit_frames if
                            os.path.exists(hit)]
        self.attack1_frame = [py.transform.scale2x(py.image.load(attack1)) for attack1 in self.attack1_frames if
                          os.path.exists(attack1)]
        self.attack2_frame = [py.transform.scale2x(py.image.load(attack1)) for attack1 in self.attack2_frames if
                              os.path.exists(attack1)]

        self.index = 0  # Running animation index

    def handle_attack1(self):
        """Trigger attack1 animation."""
        if not self.attacking and not self.dying and not self.hitting and not self.attacking_two:  # Prevent attack during death
            self.attacking = True
            self.attack_index = 0  # Reset attack animation index
            self.sword.play()

    def handle_attack2(self):
        """Trigger attack1 animation."""
        if not self.attacking_two and not self.dying and not self.hitting and not self.attacking:  # Prevent attack during death
            self.attacking_two = True
            self.attack_index = 0  # Reset attack animation index
            self.sword.play()


    def handle_jump(self):
        if not self.jumping and not self.filling and not self.dying and not self.hitting:
            self.jumping = True
            self.jump_velocity = 26
            self.jump_sound.play()

    def handle_death(self):
        """Trigger death animation."""
        if not self.dying:
            self.dying = True
            self.death_index = 0

    def take_damage(self, amount):
        """Reduce health when taking damage."""
        self.current_health -= amount

        self.hitting = True
        # self.hit_index = 0  # Reset hit animation index
        self.hit_index = 0  # Reset hit animation index

        if self.current_health <= 0:
            self.current_health = 0
            self.handle_death()  # Trigger death animation when health reaches 0

    def draw_health_bar(self, screen):
        """Draw health bar above the hero."""
        bar_x = self.hero_x + 120  # Adjust to center the health bar
        bar_y = self.hero_y + 80  # Position above the hero

        # Background bar (Red - Full health)
        py.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, self.health_bar_width, 10))

        # Current health bar (Green - Remaining health)
        health_ratio = self.current_health / self.max_health
        py.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, self.health_bar_width * health_ratio, 10))

    def update(self):
        if self.dying:
            if self.death_index < len(self.death_frame) - 1:
                self.death_index += 1
            return  # Stop updating movement when dying

        if self.attacking:
            if self.attack_index < len(self.attack1_frame) - 1:
                self.attack_index += 1
            else:
                self.attacking = False  # Stop attack animation after playing once

        if self.attacking_two:
            if self.attack_index < len(self.attack2_frame) - 1:
                self.attack_index += 1
            else:
                self.attacking_two = False  # Stop attack animation after playing once

        if self.hitting:
            if self.hit_index < len(self.hit_frame) - 1:
                self.hit_index += 1

            else:
                self.hitting = False  # Stop hit animation after playing once


        if self.jumping:
            self.hero_y -= self.jump_velocity
            self.jump_velocity -= self.gravity

            if self.jump_velocity < 0:
                self.filling = True
                self.jumping = False

        if self.filling:
            self.fill_index = (self.fill_index + 1) % len(self.fill_frame)

            self.hero_y -= self.jump_velocity
            self.jump_velocity -= self.gravity

            if self.hero_y >= 320:
                self.hero_y = 320
                self.filling = False
                self.jump_fall.play()


        elif not self.jumping and not self.filling and not self.hitting and not self.attacking:
            self.index = (self.index + 1) % len(self.run_frame)

    def draw(self, screen):
        if self.dying:
            screen.blit(self.death_frame[self.death_index], (self.hero_x, self.hero_y))
        elif self.attacking:
            screen.blit(self.attack1_frame[self.attack_index % len(self.attack1_frame)], (self.hero_x, self.hero_y))
        elif self.attacking_two:
            screen.blit(self.attack2_frame[self.attack_index % len(self.attack2_frame)], (self.hero_x, self.hero_y))
        elif self.hitting:
            screen.blit(self.hit_frame[self.hit_index % len(self.hit_frame)], (self.hero_x, self.hero_y))
        elif self.jumping:
            screen.blit(self.jump_frame[self.jump_index % len(self.jump_frame)], (self.hero_x, self.hero_y))
            self.jump_index += 1
        elif self.filling:
            screen.blit(self.fill_frame[self.fill_index], (self.hero_x, self.hero_y))
        else:
            screen.blit(self.run_frame[self.index], (self.hero_x, self.hero_y))

        # Draw health bar
        self.draw_health_bar(screen)


