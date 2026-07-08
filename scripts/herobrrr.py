from typing import List
from enemybrrr import Enemy
import math
import pygame
import random
from hero_importer import (walking_animation1, walking_animationn2, walking_animation2, walking_animation3, walking_animationn1,
                           idle_animation1,idle_animation2,idle_animation3,idle_animationn1,idle_animationn2,idle_animationn3,attack_animation1,attack_animation2
                           ,attack_animation3,attack_animationn1,attack_animationn2,attack_animationn3,walking_animationn3)

class Hero :
    heros : List["Hero"] = []
    all_targets : List["Hero"] = []

    heros_to_remove = []
    def __init__(self, x, y, health, damage, ix , iy, types, barrack, lvl, range = 100) :
        self.x = x
        self.y = y
        self.lvl = lvl
        self.health = health
        self.max_health = health
        self.damage = damage
        self.frame = 0
        self.walking_animation1 = eval(f'walking_animation{self.lvl}')
        self.walking_animation2 = eval(f'walking_animationn{self.lvl}')
        self.idle_animation1 = eval(f'idle_animation{self.lvl}')
        self.idle_animation2 = eval(f'idle_animationn{self.lvl}')
        self.attack_animation1 = eval(f'attack_animation{self.lvl}')
        self.attack_animation2 = eval(f'attack_animationn{self.lvl}')
        self.animation_pack = self.idle_animation1
        self.ix = ix
        self.iy = iy
        self.ispeed = 70
        self.speed = 70
        self.delay = pygame.time.get_ticks()
        self.type = types
        self.barrack = barrack
        self.range = range
        self.targets = []
        self.idle = False
        self.attack = False
        self.walk = False
        self.cd = 0
        self.ok = True
        self.movee = False
        self.ball = None
        self.target_index = 0
        self.calc = False
        self.state = True
        Hero.heros.append(self)
        Enemy.all.append(self)

    def hero_state(self, hd_lst) :
        lst = self.get_enemies_in_range()
        lst = list(filter(lambda enemy : enemy.targeted_state == False, lst))
        lst = list(filter(lambda enemy : enemy.intargetable == False, lst))
        if len(self.targets) == 0 and lst != [] and self.movee == False and self.walk == False :
            self.targeted_enemy = random.choice(lst)
            Hero.all_targets.append(self.targeted_enemy)
            self.ispeed = self.targeted_enemy.speed
            self.give = self.targeted_enemy.animation_pack
            self.targeted_enemy.speed = 0
            self.targeted_enemy.ispeed = 0
            self.targeted_enemy.targeted_state = True
            self.speed = 70
            self.idle = False
            self.walk = True
            self.attack = False
            self.targets.append(self.targeted_enemy)
            if self.x > self.targeted_enemy.x - 50:
                self.animation_pack = self.walking_animation1
            else :
                self.animation_pack = self.walking_animation2
        if self.walk == True and len(self.targets) != 0 :
            angle = math.atan2(self.targeted_enemy.y + 5 - self.y, self.targeted_enemy.x - 50  - self.x)
            self.x += self.speed * math.cos(angle) * Enemy.delta
            self.y += self.speed * math.sin(angle) * Enemy.delta
            if self.targets[0]  in Enemy.enemies_to_remove :
                self.targets = []
                
            if math.sqrt((self.targeted_enemy.x - 50 - self.x) ** 2 + (self.targeted_enemy.y + 5 - self.y) ** 2) <= 1 :
                self.walk = False
                self.attack = True
                self.speed = 0
        if self.attack == True :
            if int(self.frame) == 15 :
                self.ok = False
                self.targeted_enemy.health -= 300
                self.frame = 0
            if int(self.targeted_enemy.frame) == 15 :
                self.targeted_enemy.ok = False
                self.health -= self.targeted_enemy.damage
                self.targeted_enemy.frame = 0
            current_time = pygame.time.get_ticks()
            if current_time >= self.cd :
                self.ok = True
                self.frame = 0
                self.animation_pack = random.choice([self.attack_animation1, self.attack_animation2])
                self.targeted_enemy.animation_pack = random.choice([self.targeted_enemy.attack_animation1, self.targeted_enemy.attack_animation2])
                self.targeted_enemy.frame = 0
                self.targeted_enemy.ok = True
                self.cd = 1000 + current_time
            if self.targeted_enemy.health <= 0 :
                if self.targeted_enemy in Enemy.enemies :
                    Enemy.enemies_to_remove.append(self.targeted_enemy)
                self.speed = 70
                self.idle = False
                self.attack = False
                self.targets = []
        if len(self.targets) == 0 and self.idle == False :
            if self.x > self.ix :
                self.animation_pack = self.walking_animation1
            else :
                self.animation_pack = self.walking_animation2
            self.speed  = 70
            angle = math.atan2(self.iy - self.y, self.ix - self.x)
            self.x += self.speed * math.cos(angle) * Enemy.delta
            self.y += self.speed * math.sin(angle) * Enemy.delta
            if math.sqrt((self.ix - self.x) ** 2 + (self.iy  - self.y) ** 2) <= 5 :
                self.speed = 0
                self.animation_pack = random.choice([self.idle_animation1, self.idle_animation2])
                self.idle = True
                self.attack = False
                self.walk = False
                self.movee = False
                self.target_index = 0
                self.target_points = []
        if self.health <= 0 :
            Hero.heros_to_remove.append(self)
            self.targeted_enemy.targeted_state = False
            self.targeted_enemy.ok = True
            self.targeted_enemy.ispeed = self.targeted_enemy.iispeed
            self.targeted_enemy.animation_pack = self.give
            Hero.all_targets.remove(self.targeted_enemy)
            death_sound = random.choice(hd_lst)
            channel = pygame.mixer.find_channel()
            channel.play(death_sound)
            if self.type == "A" :
                current_times = pygame.time.get_ticks()
                self.barrack.cd1 = current_times + 5000
                self.barrack.hero1 = []
            elif self.type == 'B' :
                current_time2 = pygame.time.get_ticks()
                self.barrack.cd2 = current_time2 + 5000
                self.barrack.hero2 = []
            elif self.type == 'C' :
                current_time3 = pygame.time.get_ticks()
                self.barrack.cd3 = current_time3 + 5000
                self.barrack.hero3 = []
            else :
                current_time4 = pygame.time.get_ticks()
                self.barrack.cd4 += current_time4 + 5000
                self.barrack.hero4 = []

    def get_enemies_in_range(self):
        enemies_in_range = []
        for enemy in Enemy.enemies:
            enemy_x, enemy_y = enemy.x, enemy.y
            distance = math.sqrt((self.x - enemy_x) ** 2 + (self.y - enemy_y) ** 2)
            if  distance <= self.range:
                enemies_in_range.append(enemy)
        return enemies_in_range
    
    def get_enemies_in_range2(self):
        enemies_in_range = []
        for enemy in Enemy.enemies:
            enemy_x, enemy_y = enemy.x, enemy.y
            distance = math.sqrt((self.x - enemy_x) ** 2 + (self.y - enemy_y) ** 2)
            if distance <= 300:
                enemies_in_range.append(enemy)
        return enemies_in_range
    
    def animator(self, screen) :
        if self.ok == True or self.attack == False  :
            self.frame += 25 * Enemy.delta
            if self.frame >= 16:
                self.frame = 0
        enemy_x = self.x
        enemy_y = self.y
        enemy_health = self.health
        enemy_max_health = self.max_health
        skeleton_pos = (int(enemy_x), int(enemy_y))
        health_percentage = enemy_health / enemy_max_health
        health_bar_width = int(50 * health_percentage)  
        health_bar_height = 5 
        health_bar_pos = (skeleton_pos[0], skeleton_pos[1])
        if enemy_health != enemy_max_health :
            pygame.draw.rect(screen, (255, 0, 0), (health_bar_pos[0]-30, health_bar_pos[1]-50, 50, health_bar_height))
            pygame.draw.rect(screen, (0, 255, 0), (health_bar_pos[0]-30, health_bar_pos[1]-50, health_bar_width, health_bar_height))
        curr_back = self.animation_pack[int(self.frame)]
        screen.blit(curr_back, (self.x - 60, self.y - 60))