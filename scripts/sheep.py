import pygame
import os
import random
import math
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIRECTORY = os.path.join(BASE_DIR, "assets", "assets1")
pygame.init()
screen = pygame.display.set_mode(( 1600, 900 ))
def importer(frames, a=70, b=70, aa=0, bb=18, aaa=False) :
    lst = []
    for i in range(aa, bb):
        filename1 = frames.format(i)
        frame1 = pygame.image.load(filename1).convert_alpha()
        frame1 = pygame.transform.smoothscale(frame1, (a, b))
        frame1 = pygame.transform.flip(frame1, aaa, False)
        lst.append(frame1)
    return lst

frames = os.path.join(DEFAULT_DIRECTORY,"Walking_{:03d}.png")
sheep_walk = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"Walking_{:03d}.png")
sheep_walk2 = importer(frames, aaa=True)
frames = os.path.join(DEFAULT_DIRECTORY,"idle_{:03d}.png")
sheep_idle = importer(frames, aa=0, bb=12)
frames = os.path.join(DEFAULT_DIRECTORY,"Fearing_{:03d}.png")
sheep_scared = importer(frames, aa=0, bb=6)
frames = os.path.join(DEFAULT_DIRECTORY,"Hurt_{:03d}.png")
sheep_hurt = importer(frames, aa=0, bb=12)
frames = os.path.join(DEFAULT_DIRECTORY,"Idle Blinking_{:03d}.png")
sheep_idle2 = importer(frames, aa=0, bb=12)
frames = os.path.join(DEFAULT_DIRECTORY,"Dying_{:03d}.png")
sheep_death = importer(frames, aa=0, bb=18)
frames = os.path.join(DEFAULT_DIRECTORY,"Eating_{:03d}.png")
sheep_eat1 = importer(frames, aa=0, bb=12)
sheep_eat2 = importer(frames, aa=0, bb=12)
sheep_eat3 = importer(frames, aa=0, bb=12)
sheep_eat4 = importer(frames, aa=0, bb=12)
sheep_eat5 = importer(frames, aa=0, bb=12)

class Sheep :
    sheeps = []
    def __init__(self,x, y, walking=sheep_walk, idle= sheep_idle, animation_pack= sheep_idle) -> None:
        self.x = 447
        self.y = 583
        self.walking = walking
        self.idle = idle
        self.animation_pack = animation_pack
        self.frame = 0
        self.area = pygame.Rect(self.x, self.y, 50, 50)
        self.current_time = pygame.time.get_ticks()
        self.current_time2 = pygame.time.get_ticks()
        self.speed = 0
        self.walking_st = False
        self.current_loc = (447, 583)
        self.clicked = 0
        self.death = sheep_death
        Sheep.sheeps.append(self)
    def sheep_animator(self) :
        current_lightrp2g = self.animation_pack[int(self.frame)]
        screen.blit(current_lightrp2g, (self.x - 35 , self.y - 35))
        self.frame += 0.05
        if self.animation_pack == sheep_idle or self.animation_pack == sheep_idle2 :
            if self.frame >= 12 :
                self.frame = 0
                self.animation_pack = random.choice([sheep_idle, sheep_idle2, sheep_idle])

        elif self.animation_pack == sheep_walk or self.animation_pack == sheep_walk2 :
            if self.frame >= 18 :
                self.frame = 0
        elif self.animation_pack == sheep_scared :
            current_time = pygame.time.get_ticks()
            if current_time >= self.current_time + 5000 :
                self.frame = 0
                self.animation_pack = sheep_idle
            if self.frame >= 6 :
                self.frame = 0
        elif self.animation_pack == sheep_hurt :
            if self.frame >= 12 :
                self.frame = 0
                self.animation_pack = sheep_scared
        elif self.animation_pack == sheep_eat1 :
            if self.frame >= 12 :
                self.frame = 0
                self.animation_pack = sheep_eat2
        elif self.animation_pack == sheep_eat2 :
            if self.frame >= 12 :
                self.frame = 0
                self.animation_pack = sheep_eat3
        elif self.animation_pack == sheep_eat3 :
            if self.frame >= 12 :
                self.frame = 0
                self.animation_pack = sheep_eat4
        elif self.animation_pack == sheep_eat4 :
            if self.frame >= 12 :
                self.frame = 0
                self.animation_pack = sheep_eat5
        elif self.animation_pack == sheep_eat5 :
            if self.frame >= 12 :
                self.frame = 0
                self.animation_pack = sheep_idle
        elif self.animation_pack == sheep_death :
            if self.frame >= 18 :
                self.frame = 0

    def sheep_pressed(self) :
        self.frame = 0
        self.animation_pack = sheep_hurt
        self.current_time = pygame.time.get_ticks()
        self.current_time2 += 3000
    
    def walk_state(self) :
        current_time = pygame.time.get_ticks()
        if current_time >= self.current_time2 + 20000 :
            lst = [(447, 583), (546, 578), (685, 545)]
            lst.remove(self.current_loc)
            target = random.choice(lst)
            self.current_loc = target
            self.area = pygame.Rect(target[0], target[1], 50, 50)
            self.tx = target[0]
            self.ty = target[1]
            if self.tx >= self.x : 
                self.animation_pack = sheep_walk
            else :
                self.animation_pack = sheep_walk2
            self.speed = 0.15
            self.walking_st = True
            self.current_time2 = current_time
        if self.walking_st == True :
            angle = math.atan2(self.ty - self.y, self.tx  - self.x)
            self.x += self.speed * math.cos(angle)
            self.y += self.speed * math.sin(angle)
            if math.sqrt((self.tx - self.x) ** 2 + (self.ty - self.y) ** 2) <= 5 :
                self.frame = 0
                self.animation_pack = sheep_eat1
                self.speed = 0
                self.walking_st = False