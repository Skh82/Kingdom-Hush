from typing import List
import pygame
import math
import os
import random
import pygame
pygame.init()
screen = pygame.display.set_mode(( 1600, 900 ))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIRECTORY = os.path.join(BASE_DIR, "assets", "assets1")
base_filenameskedA = os.path.join(DEFAULT_DIRECTORY,"1_Reaper_Man_Dying_{:03d}.png")
base_filenameskedAA = os.path.join(DEFAULT_DIRECTORY,"1_Reaper_Man_Walking_{:03d}.png")
animation_deathB = []
def importer(frames, a=120, b=120) :
    lst = []
    for i in range(1, 17):
        filename1 = frames.format(i)
        frame1 = pygame.image.load(filename1).convert_alpha()
        frame1 = pygame.transform.smoothscale(frame1, (a, b))
        lst.append(frame1)
    return lst
frames = os.path.join(DEFAULT_DIRECTORY,"walkB ({:02d}).png")
walkB = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"deathB ({:02d}).png")
deathB = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"attackB ({:02d}).png")
attackB = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"spawn ({:02d}).png")
spawnG = importer(frames)
path_points1 = [(800, 0), (756, 68), (687, 117), (645, 210), (684, 305), (682, 359), (556, 389), (498, 368), (472, 305), (309, 293), (171, 288), (37, 293)]
path_points2 = [(841, 0), (788, 79), (715, 135), (687, 207), (709, 300), (705, 385), (555, 418), (476, 396), (451, 345), (306, 328), (173, 321), (36, 325)]
path_points3 = [(886, 0), (828, 99), (739, 152), (728, 206), (756, 289), (728, 418), (554, 456), (454, 430), (414, 372), (303, 368), (176, 360), (36, 368)]
path_points4 = [(1600, 204), (1403, 220), (1277, 243), (1182, 307), (1088, 399), (1015, 495), (905, 545), (788, 584), (652, 593), (449, 578), (272, 567), (32, 561)]
path_points5 = [(x, y - 30) for x, y in path_points4]
path_points6 = [(x, y + 30) for x, y in path_points4]
path_points7 = [(907, 900), (887, 814), (829, 715), (785, 631), (657, 584), (514, 572), (323, 564), (32, 560)]
path_points8 = [(865, 880), (844, 816), (805, 747), (725, 631), (527, 628), (357, 610), (170, 610), (31, 604)]

shot_attack_sound = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"kr4_linirea_musketeer_shot.ogg"))

frames = os.path.join(DEFAULT_DIRECTORY,"walkS ({:02d}).png")
walkS = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"deathS ({:02d}).png")
deathS = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"slashS ({:02d}).png")
attackS = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"gunner ({:02d}).png")
shooting_animation = importer(frames)
for i in range(0, 15):
    filename1 = base_filenameskedA.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (70, 70))
    animation_deathB.append(frame1)
animation_walkB = []
for i in range(0, 23):
    filename1 = base_filenameskedAA.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (70, 70))
    animation_walkB.append(frame1)
animation_attackB = []
for i in range(0, 23):
    filename1 = base_filenameskedAA.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (70, 70))
    animation_attackB.append(frame1)
spawn_attack_sound = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"spawns.ogg"))
heal_sound = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"heal.ogg"))


class Enemy:
    enemies : List['Enemy'] = []
    enemies_to_remove : List['Enemy'] = []
    all : List['Enemy'] = []
    pause : List['Enemy'] = False
    running : List['Enemy'] = True
    a = 0
    delta = 0

    def __init__(self, model : str, health : int, path_points, target_index = 0, speed = 25, death= None, walk= None, attack1= None, attack2=None, offset_x= 60, offset_y= 60, damage= 50, front= None, back= None) -> None :
        self.model = model
        self.health = 3000
        self.target_index = target_index
        self.damage = damage
        self.speed = speed
        self.ispeed = self.speed
        self.iispeed = self.speed
        self.path_points = path_points
        self.x = self.path_points[0][0]
        self.y = self.path_points[0][1]
        self.target_x, self.target_y = self.path_points[self.target_index]
        self.frame = 0
        self.max_health = 3000
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.offset_xd = 75
        self.offset_yd = 75
        self.pause_duration = 0
        self.fire_duration = 0
        self.targeted_state = False
        self.fire = False
        self.firee = False
        self.frame_f = 0
        self.death_animation = death
        self.walk_animation = walk
        self.attack_animation1 = attack1
        self.attack_animation2 = attack2
        self.animation_pack = walk
        self.spawn_state = False
        self.ok = True
        self.inf = False
        self.inff = None
        self.front = front
        self.back = back
        self.angle = None
        self.tornado_duration = 0
        self.tornado = False
        self.intargetable = False
        self.angle = math.atan2(self.target_y - self.y, self.target_x - self.y)
        Enemy.enemies.append(self)
        Enemy.all.append(self)

    def update_enemy_pos(self) :
        distance_to_target = math.sqrt((self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2)
        self.angle = math.atan2(self.target_y - self.y, self.target_x - self.x)
        if distance_to_target > 5:
            self.x += self.speed * math.cos(self.angle) * Enemy.delta
            self.y += self.speed * math.sin(self.angle) * Enemy.delta
        else:
            self.target_index += 1
            if self.target_index >= len(self.path_points):
                Enemy.enemies_to_remove.append(self)
            else :
                self.target_x = self.path_points[self.target_index][0]
                self.target_y = self.path_points[self.target_index][1]
                self.angle = math.atan2(self.target_y - self.y, self.target_x - self.x)
                angle_degrees = math.degrees(self.angle)
                if -135 < angle_degrees < - 45 :
                    self.animation_pack = self.back
                elif 45 < angle_degrees < 135 :
                    self.animation_pack = self.front
                else :
                    self.animation_pack = self.walk_animation
        Enemy.time = pygame.time.get_ticks()
        if self.tornado:
            angle = math.atan2(self.targety - self.y, self.targetx - self.x)
            self.x += self.speed * math.cos(angle) * Enemy.delta * 1.8
            self.y += self.speed * math.sin(angle) * Enemy.delta * 1.8

        if self.time - self.tornado_duration >= 0:
            if self.tornado:
                self.health -= 500
                if self.angle < 0:
                    self.target_index += 1 
                if self.health <= 0:
                    Enemy.enemies_to_remove.append(self)
            self.tornado = False


        Enemy.time = pygame.time.get_ticks()
        if self.fire_duration > 0 :
            self.health -= 0.2
            self.fire = True
            if self.targeted_state == False :
                self.ispeed = self.iispeed / 2
            if self.health <= 0 :
                Enemy.enemies_to_remove.append(self)
        if self.time - self.fire_duration >= 0 :
            self.fire_duration = 0
            self.fire = False
            self.firee = False
            if self.targeted_state == False :
                self.ispeed = self.iispeed

        Enemy.time = pygame.time.get_ticks()
        if self.pause_duration > 0 :
            self.speed = 0
        if self.time - self.pause_duration >= 0 :
            self.speed = self.ispeed

    def animator(self) :
        if self.ok == True :
            self.frame += 35 * Enemy.delta
            if self.frame >= 16:
                self.frame = 0
        enemy_x = self.x
        enemy_y = self.y
        enemy_health = self.health
        enemy_max_health = self.max_health
        skeleton_pos = (int(enemy_x), int(enemy_y))
        health_percentage = enemy_health / enemy_max_health
        health_bar_width = int(30 * health_percentage)  
        health_bar_height = 3
        health_bar_pos = (skeleton_pos[0], skeleton_pos[1] - 30)
        if enemy_health != enemy_max_health :
            pygame.draw.rect(screen, (255, 0, 0), (health_bar_pos[0]-20, health_bar_pos[1]-20, 30, health_bar_height))
            pygame.draw.rect(screen, (0, 255, 0), (health_bar_pos[0]-20, health_bar_pos[1]-20, health_bar_width, health_bar_height))
        try:
            cur_back = self.animation_pack[int(self.frame)]
            screen.blit(cur_back, (self.x - self.offset_x , self.y - self.offset_y))
        except:
            print(self.animation_pack)
            print(self.frame)
class EnemyA(Enemy):
    pass
class EnemyB(Enemy):
    pass
class EnemyG(Enemy):
    def __init__(self, model: str, health: int, path_points, target_index=0, speed=0.17, walk= None, death= None, attack=None, offset_x=None, offset_y=None, damage=None) -> None:
        super().__init__(model, health, path_points, target_index, speed, death, walk, attack, offset_x, offset_y, damage)
        self.spawncd = 10000
    def spawn(self) :
        current_time = pygame.time.get_ticks()
        if current_time >= self.spawncd and self.targeted_state == False :
            self.frame = 0
            self.animation_pack = spawnG
            channel = pygame.mixer.find_channel()
            channel.play(spawn_attack_sound)
            enemy = EnemyB('B', 1000, path_points1, self.target_index, self.iispeed * 1.4, walk=walkB, death=deathB, attack=attackB)
            enemy.x = self.x
            enemy.y = self.y
            enemy = EnemyB('B', 1000, path_points2, self.target_index, self.iispeed * 1.4, walk=walkB, death=deathB, attack=attackB)
            enemy.x = self.x
            enemy.y = self.y
            enemy = EnemyB('B', 1000, path_points3, self.target_index, self.iispeed * 1.4, walk=walkB, death=deathB, attack=attackB)
            enemy.x = self.x
            enemy.y = self.y
            self.spawncd = current_time + 10000
    def animator(self) :
        if self.ok == True :
            self.frame += 0.05
            if self.frame >= 16:
                self.frame = 0
        if self.animation_pack == spawnG and int(self.frame) == 15 :
            self.animation_pack = self.walk_animation
        enemy_x = self.x
        enemy_y = self.y
        enemy_health = self.health
        enemy_max_health = self.max_health
        skeleton_pos = (int(enemy_x), int(enemy_y))
        health_percentage = enemy_health / enemy_max_health
        health_bar_width = int(50 * health_percentage)  
        health_bar_height = 5 
        health_bar_pos = (skeleton_pos[0], skeleton_pos[1] - 30)
        if enemy_health != enemy_max_health :
            pygame.draw.rect(screen, (255, 0, 0), (health_bar_pos[0]-30, health_bar_pos[1]-50, 50, health_bar_height))
            pygame.draw.rect(screen, (0, 255, 0), (health_bar_pos[0]-30, health_bar_pos[1]-50, health_bar_width, health_bar_height))
        cur_back = self.animation_pack[int(self.frame)]
        screen.blit(cur_, (self.x - self.offset_x , self.y - self.offset_y))
class EnemyN(Enemy):
    def skeleton_spawn(self) :
        channel = pygame.mixer.find_channel()
        channel.play(spawn_attack_sound)
        enemy = EnemyS('S', 1000, path_points1, self.target_index, 0.3, walk=walkS, death=deathS, attack=attackS)
        enemy.x = self.x
        enemy.y = self.y
        enemy = EnemyS('S', 1000, path_points2, self.target_index, 0.3, walk=walkS, death=deathS, attack=attackS)
        enemy.x = self.x
        enemy.y = self.y
        enemy = EnemyS('S', 1000, path_points3, self.target_index, 0.3, walk=walkS, death=deathS, attack=attackS)
        enemy.x = self.x
        enemy.y = self.y
class EnemyS(Enemy):
    pass
class EnemyK(Enemy):
    pass
class EnemyL(Enemy):
    def __init__(self, model: str, health: int, path_points, target_index=0, speed=0.17, death=None, walk=None, attack=None, offset_x=60, offset_y=60, damage=50) -> None:
        super().__init__(model, health, path_points, target_index, speed, death, walk, attack, offset_x, offset_y, damage)
        self.shoot_delay = 5000
    def shoot(self, lst) :
        current_time = pygame.time.get_ticks()
        if current_time >= self.shoot_delay and self.targeted_state == False and len(lst) != 0 :
            tar = random.choice(lst)
            tar.health -= 100
            self.shoot_delay = 5000 + current_time
            self.frame = 0
            self.animation_pack = shooting_animation
            channel = pygame.mixer.find_channel()
            channel.play(shot_attack_sound)
            
    def animator(self) :
        if self.ok == True :
            self.frame += 0.05
            if self.frame >= 16:
                self.frame = 0
        if self.animation_pack == shooting_animation and int(self.frame) == 15 :
            self.animation_pack = self.walk_animation
        enemy_x = self.x
        enemy_y = self.y
        enemy_health = self.health
        enemy_max_health = self.max_health
        skeleton_pos = (int(enemy_x), int(enemy_y))
        health_percentage = enemy_health / enemy_max_health
        health_bar_width = int(50 * health_percentage)  
        health_bar_height = 5 
        health_bar_pos = (skeleton_pos[0], skeleton_pos[1] - 30)
        if enemy_health != enemy_max_health :
            pygame.draw.rect(screen, (255, 0, 0), (health_bar_pos[0]-30, health_bar_pos[1]-50, 50, health_bar_height))
            pygame.draw.rect(screen, (0, 255, 0), (health_bar_pos[0]-30, health_bar_pos[1]-50, health_bar_width, health_bar_height))
        cur_back = self.animation_pack[int(self.frame)]
        screen.blit(cur_back, (self.x - self.offset_x , self.y - self.offset_y))
class EnemyC(Enemy):

    def __init__(self, model: str, health: int, path_points, target_index=0, speed=25, death=None, walk=None, attack1=None, attack2=None, offset_x=60, offset_y=60, damage=50, front=None, back=None) -> None:
        super().__init__(model, health, path_points, target_index, speed, death, walk, attack1, attack2, offset_x, offset_y, damage, front, back)
        self.flag = True

    def update_enemy_pos(self):
        if self.health < self.max_health/2 and self.flag:
            self.iispeed = self.iispeed * 2
            self.ispeed = self.ispeed * 2
            self.speed = self.speed * 2
            self.flag = False
            self.intargetable = True
        return super().update_enemy_pos()
class EnemyD(Enemy):
    def __init__(self, model: str, health: int, path_points, target_index=0, speed=25, death=None, walk=None, attack1=None, attack2=None, offset_x=60, offset_y=60, damage=50, front=None, back=None) -> None:
        super().__init__(model, health, path_points, target_index, speed, death, walk, attack1, attack2, offset_x, offset_y, damage, front, back)
        self.spawn_cd = 20000 + pygame.time.get_ticks()

    def update_enemy_pos(self):
        Enemy.time = pygame.time.get_ticks()
        if Enemy.time >= self.spawn_cd:
            channel = pygame.mixer.find_channel()
            channel.play(spawn_attack_sound)
            enemy = EnemyD('D', 1000, self.path_points, self.target_index, self.iispeed, walk=self.walk_animation, death=self.death_animation, attack1=self.attack_animation1,
                           attack2=self.attack_animation2)
            enemy.animation_pack = self.walk_animation
            enemy.x = self.x
            enemy.y = self.y
            enemy.front = self.front
            enemy.back = self.back
            self.spawn_cd = Enemy.time + 20000
        pygame.draw.circle(screen, (0,0,0), self.path_points[self.target_index], 5)
        return super().update_enemy_pos()
class EnemyH(Enemy):
    def __init__(self, model: str, health: int, path_points, target_index=0, speed=25, death=None, walk=None, attack1=None, attack2=None, offset_x=60, offset_y=60, damage=50, front=None, back=None) -> None:
        super().__init__(model, health, path_points, target_index, speed, death, walk, attack1, attack2, offset_x, offset_y, damage, front, back)
        self.cd = 5000 + pygame.time.get_ticks()

    def update_enemy_pos(self):
        Enemy.time = pygame.time.get_ticks()
        if self.time >= self.cd and not self.targeted_state:
            channel = pygame.mixer.find_channel()
            channel.play(heal_sound)
            for enemy in Enemy.enemies:
                if math.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2) <= 150:
                    enemy.health = min(enemy.health+500, enemy.max_health)
            self.cd = self.time + 5000
        return super().update_enemy_pos()
    
    def animator(self) :
        if self.ok == True :
            self.frame += 20 * Enemy.delta
            if self.frame >= 16:
                self.frame = 0
        enemy_x = self.x
        enemy_y = self.y
        enemy_health = self.health
        enemy_max_health = self.max_health
        skeleton_pos = (int(enemy_x), int(enemy_y))
        health_percentage = enemy_health / enemy_max_health
        health_bar_width = int(50 * health_percentage)  
        health_bar_height = 3
        health_bar_pos = (skeleton_pos[0], skeleton_pos[1] - 30)
        if enemy_health != enemy_max_health :
            pygame.draw.rect(screen, (255, 0, 0), (health_bar_pos[0]-30, health_bar_pos[1]-50, 50, health_bar_height))
            pygame.draw.rect(screen, (0, 255, 0), (health_bar_pos[0]-30, health_bar_pos[1]-50, health_bar_width, health_bar_height))
        try:
            cur_back = self.animation_pack[int(self.frame)]
            screen.blit(cur_back, (self.x - self.offset_x , self.y - self.offset_y))
        except:
            print(self.animation_pack)
            print(self.frame)
