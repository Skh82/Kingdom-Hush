import pygame
import math
from enemybrrr import Enemy
from herobrrr import Hero
class Barracks :
    barracks = []
    def __init__(self, x, y, cd, barracks_image, hero_points) :
        current_time = pygame.time.get_ticks()
        self.x = x
        self.y = y
        self.image = barracks_image
        self.cd1 = cd + current_time
        self.cd2 = cd + current_time
        self.cd3 = cd + current_time
        self.cd4 = cd + current_time
        self.hero1 = []
        self.hero2 = []
        self.hero3 = []
        self.hero4 = []
        self.level_up = False
        self.area = pygame.Rect(self.x - 100, self.y - 100, 200, 200)
        self.lvl = 1
        Barracks.barracks.append(self)
        distances = {}
        for point in hero_points:
            x, y = eval(point)
            distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
            distances[point] = distance
        self.target_point = min(distances, key=distances.get)
        Enemy.all.append(self)
    def hero_creator(self) :
        current_time = pygame.time.get_ticks()
        if current_time >= self.cd1 and self.hero1 == [] :
            self.hero1.append(Hero(self.x, self.y, 1000, 0.1, (eval(self.target_point))[0] - 30, (eval(self.target_point))[1], "A", self, lvl=self.lvl))
            #channel = pygame.mixer.find_channel()
            #channel.play(random.choice([hero1_sound_effects, hero2_sound_effects]))
        if current_time >= self.cd2 and self.hero2 == [] :
            self.hero2.append(Hero(self.x, self.y, 1000, 0.11, (eval(self.target_point))[0] , (eval(self.target_point))[1] + 20, "B", self, lvl=self.lvl))
            #channel = pygame.mixer.find_channel()
            #channel.play(random.choice([hero1_sound_effects, hero2_sound_effects]))
        if current_time >= self.cd3 and self.hero3 == [] :
            self.hero3.append(Hero(self.x, self.y, 1000, 0.11, (eval(self.target_point))[0], (eval(self.target_point))[1] - 20, "C", self, lvl=self.lvl))
            #channel = pygame.mixer.find_channel()
            #channel.play(random.choice([hero1_sound_effects, hero2_sound_effects]))
    def animator(self, screen, barracks_image) :
        screen.blit(barracks_image, (self.x - 100, self.y - 80))