import math
import random
import pygame
from enemybrrr import Enemy
from bulletbrrr import Bullet
from typing import List
import os
screen = pygame.display.set_mode(( 1600, 900 ))
clock = pygame.time.Clock()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIRECTORY = os.path.join(BASE_DIR, "assets", "assets1")
pygame.init()


def importer(frames, a=90, b=90, aa=1, bb=17, aaa=False) :
    lst = []
    for i in range(aa, bb):
        filename1 = frames.format(i)
        frame1 = pygame.image.load(filename1).convert_alpha()
        frame1 = pygame.transform.smoothscale(frame1, (a, b))
        frame1 = pygame.transform.flip(frame1, aaa, False)
        lst.append(frame1)
    return lst
frames = os.path.join(DEFAULT_DIRECTORY,"snowball_{:02d}.png")
balls1 = importer(frames, aa=1, bb=7, a=512/11, b=386/11)


frames = os.path.join(DEFAULT_DIRECTORY,"walkK ({:02d}).png")
walkK = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"deathK ({:02d}).png")
deathK = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"slashK ({:02d}).png")
attackK = importer(frames)





class Champion :
    def __init__(self,x , y, ix, iy) -> None:
        self.x = x
        self.y = y
        self.ix = ix
        self.iy = iy
        self.delay = pygame.time.get_ticks()
        self.ball_frames = []
        self.animation_pack = walkK
        self.frame = 0
        self.range = 400
        self.move = False
        self.movee = False
        self.idle = True
        self.attack = False
        self.targets = []
        self.ispeed = 0.3
        self.speed = 0.3
        self.targets = []
    def get_enemies_in_range(self):
        enemies_in_range = []
        for enemy in Enemy.enemies:
            enemy_x, enemy_y = enemy.x, enemy.y
            distance = math.sqrt((self.x - enemy_x) ** 2 + (self.y - enemy_y) ** 2)
            if  distance <= self.range:
                enemies_in_range.append(enemy)
        return enemies_in_range
    def champ_spell(self, clss):
        targets : List['Enemy'] = self.get_enemies_in_range()
        targets.sort(key=lambda target: target.x)
        targets.reverse()
        if len(targets) != 0 :
            target = targets[0]
            by = targets[0].y
            bx = targets[0].x
            ix = self.x
            iy = self.y
            if math.sqrt((self.x - bx) ** 2 + (self.y - by) ** 2) <= 200 :
                targetss = list(filter(lambda enemy : enemy.targeted_state == False , targets))
                if len(self.targets) == 0 and targetss != [] :
                    self.targeted_enemy = targetss[0]
                    clss.all_targets.append(self.targeted_enemy)
                    self.ispeed = self.targeted_enemy.speed
                    self.targeted_enemy.speed = 0
                    self.targeted_enemy.ispeed = 0
                    self.targeted_enemy.targeted_state = True
                    self.speed = 0.3
                    self.idle = False
                    self.move = True
                    self.attack = False
                    self.targets.append(self.targeted_enemy)
                    if self.move == True and len(self.targets) != 0 :
                        angle = math.atan2(self.targeted_enemy.y + 5 - self.y, self.targeted_enemy.x + 50  - self.x)
                        self.x += self.speed * math.cos(angle)
                        self.y += self.speed * math.sin(angle)
                        if self.targets[0]  in Enemy.enemies_to_remove :
                            self.targets = []
                        if math.sqrt((self.targeted_enemy.x + 50 - self.x) ** 2 + (self.targeted_enemy.y + 5 - self.y) ** 2) <= 1 :
                            self.move = False
                            self.attack = True
                            self.speed = 0
                    if self.attack == True :
                        if int(self.frame) == 15 :
                            self.ok = False
                            self.targeted_enemy.health -= 50
                            self.frame = 0
                        if int(self.targeted_enemy.frame) == 15 :
                            self.targeted_enemy.ok = False
                            self.health -= self.targeted_enemy.damage
                            self.targeted_enemy.frame = 0
                        current_time = pygame.time.get_ticks()
                        if current_time >= self.cd :
                            self.ok = True
                            self.frame = 0
                            self.animation_pack = random.choice([self.animation_pack, self.animation_pack])
                            self.targeted_enemy.animation_pack = self.targeted_enemy.attack_animation
                            self.targeted_enemy.frame = 0
                            self.targeted_enemy.ok = True
                            self.cd = 1000 + current_time
                        if self.targeted_enemy.health <= 0 :
                            if self.targeted_enemy in Enemy.enemies :
                                Enemy.enemies_to_remove.append(self.targeted_enemy)
                            self.speed = 0.3
                            self.move = True
                            self.idle = False
                            self.attack = False
                            self.targets = []
                    if len(self.targets) == 0 and self.idle == False :
                        if self.x > self.ix :
                            self.animation_pack = self.animation_pack
                        else :
                            self.animation_pack = self.animation_pack
                        angle = math.atan2(self.iy - self.y, self.ix  - self.x)
                        self.x += self.speed * math.cos(angle)
                        self.y += self.speed * math.sin(angle)
                        if math.sqrt((self.ix - self.x) ** 2 + (self.iy - self.y) ** 2) <= 5 :
                            self.speed = 0
                            self.animation_pack = self.animation_pack
                            self.idle = True
                            self.attack = False
                            self.move = False
            else :
                current_time = pygame.time.get_ticks()
                if current_time >= self.delay :
                    self.delay = current_time + 2000
                    self.idle = True
                    self.attack = False
                    self.move = False
                    angle = math.atan2(by - self.y, bx - self.x)
                    angle_degrees = math.degrees(angle)
                    self.ball_frames = []
                    for im in balls1 :
                        self.ball_frames.append(pygame.transform.rotate(im, -angle_degrees + 180))
                    size = (self.ball_frames[0]).get_size()
                    ball = Snow(self.x, self.y, angle, target, size, self.ball_frames)
                    Bullet.bullets.append(ball)
    def champ_state(self, clss) :
        if self.movee == False :
            self.champ_spell(clss)
        if self.movee == True :
            bx = self.ix
            by = self.iy
            angle = math.atan2(by - self.y, bx - self.x)
            self.x += 0.3 * math.cos(angle)
            self.y += 0.3 * math.sin(angle)
            if math.sqrt((self.ix - self.x) ** 2 + (self.iy - self.y) ** 2) <= 5 :
                self.movee = False
                self.idle = True
                current_time = pygame.time.get_ticks()
                self.delay = current_time + 2000
        elif self.attack == True :
            pass

    def champ_animator(self) :
        self.frame += 0.07
        if self.frame >= 16 :
            self.frame = 0
        screen.blit(self.animation_pack[int(self.frame)], (self.x - 45, self.y - 45))


        



class Snow :
    def __init__(self, x, y, angle, target, size, frames) -> None:
        self.x = x
        self.y = y
        self.speed = 1.5
        self.angle = angle
        self.target = target
        self.target_x = target.x
        self.target_y = target.y
        self.damage = 30
        self.frames = frames
        self.size = size
        self.frame = 0
    def bullet_move(self) :
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        if math.sqrt((self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2) <= 5 :
            self.target.health -= self.damage
            Bullet.bullets_to_remove.append(self)
            if self.target.health <= 0 :
                Enemy.enemies_to_remove.append(self.target)
    def bullet_draw(self) :
        self.frame += 0.08
        if self.frame >= 6 :
            self.frame = 0
        screen.blit(self.frames[int(self.frame)], (self.x - (self.size)[0] / 2, self.y - (self.size[1] / 2)))

        
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
        self.ispeed = 0.3
        self.speed = 0.3
        self.delay = pygame.time.get_ticks()
        self.type = types
        self.barrack = barrack
        self.range = range
        self.targets = []
        self.idle = True
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
    def hero_state(self) :
        self.snower()
        lst = self.get_enemies_in_range()
        lst = list(filter(lambda enemy : enemy.targeted_state == False , lst))
        if len(self.targets) == 0 and lst != [] and self.movee == False and self.walk == False :
            self.targeted_enemy = random.choice(lst)
            Hero.all_targets.append(self.targeted_enemy)
            self.ispeed = self.targeted_enemy.speed
            self.targeted_enemy.speed = 0
            self.targeted_enemy.ispeed = 0
            self.targeted_enemy.targeted_state = True
            self.speed = 0.3
            self.idle = False
            self.walk = True
            self.attack = False
            self.targets.append(self.targeted_enemy)
            if self.x > self.targeted_enemy.x :
                self.animation_pack = self.walking_animation1
            else :
                self.animation_pack = self.walking_animation2
        if self.walk == True and len(self.targets) != 0 :
            angle = math.atan2(self.targeted_enemy.y + 5 - self.y, self.targeted_enemy.x + 50  - self.x)
            self.x += self.speed * math.cos(angle)
            self.y += self.speed * math.sin(angle)
            if self.targets[0]  in Enemy.enemies_to_remove :
                self.targets = []
                
            if math.sqrt((self.targeted_enemy.x + 50 - self.x) ** 2 + (self.targeted_enemy.y + 5 - self.y) ** 2) <= 1 :
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
                self.targeted_enemy.animation_pack = self.targeted_enemy.attack_animation
                self.targeted_enemy.frame = 0
                self.targeted_enemy.ok = True
                self.cd = 1000 + current_time
            if self.targeted_enemy.health <= 0 :
                if self.targeted_enemy in Enemy.enemies :
                    Enemy.enemies_to_remove.append(self.targeted_enemy)
                self.speed = 0.3
                self.idle = True
                self.attack = False
                self.targets = []
                self.ix = self.x
                self.iy = self.y
        if len(self.targets) == 0 and self.idle == False :
            if self.x > self.ix :
                self.animation_pack = self.walking_animation1
            else :
                self.animation_pack = self.walking_animation2
            self.speed  = 0.3
            if self.calc == True :
                self.target_points = interpolate_points((self.x , self.y), (self.ix, self.iy))
                aangle = math.atan2(self.iy - self.y, self.ix  - self.x)
                for num in range(len(self.target_points)) :
                    if point_in_polygon((self.target_points[num][0], self.target_points[num][1]), polygon_points) == False :
                        print('F')
                    else :
                        self.state = False
                        sider = count_points_on_sides((self.x, self.y), (self.ix , self.iy), polygon_points)
                        while self.state == False :
                            self.target_points[num] = move_point_away((self.x , self.y),(self.ix, self.iy), ((self.target_points)[num][0], (self.target_points)[num][1]), side=sider)
                            if point_in_polygon((self.target_points[num][0], self.target_points[num][1]), polygon_points) == False :
                                self.state = True
                self.target_points.append((self.ix, self.iy))
            self.calc = False
            pygame.draw.lines(screen, (0, 0, 0), False, self.target_points, 5)
            #for point in self.target_points :
            #    pygame.draw.circle(screen, (255, 255, 255), (point[0], point[1]), 7)
            angle = math.atan2(self.target_points[self.target_index][1] - self.y, self.target_points[self.target_index][0]  - self.x)
            self.x += self.speed * math.cos(angle)
            self.y += self.speed * math.sin(angle)
            if self.x > self.target_points[self.target_index][0] :
                self.animation_pack = self.walking_animation1
            else :
                self.animation_pack = self.walking_animation2
            if math.sqrt((self.target_points[self.target_index][0] - self.x) ** 2 + (self.target_points[self.target_index][1] - self.y) ** 2) <= 5 :
                self.target_index += 1
            if self.target_index == 15 :
                self.speed = 0
                if self.animation_pack == self.walking_animation1 :
                    self.animation_pack = self.idle_animation1
                else :
                    self.animation_pack = self.idle_animation2
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
            self.targeted_enemy.animation_pack = self.targeted_enemy.walk_animation
            Hero.all_targets.remove(self.targeted_enemy)
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
    def snower(self) :
        current_time = pygame.time.get_ticks()
        if current_time >= self.delay and self.movee == False and self.idle == True :
            targets2 : List['Enemy'] = self.get_enemies_in_range2()
            targets2.sort(key=lambda target: target.x)
            targets2.reverse()
            self.delay = current_time + 2000
            self.idle = True
            self.attack = False
            self.move = False
            if targets2 != [] :
                bx = targets2[0].x
                by = targets2[0].y
                if self.x > bx :
                    self.animation_pack = snower1
                else :
                    self.animation_pack = snower2
                self.frame = 0
                target = targets2[0]
                angle = math.atan2(by - self.y, bx - self.x)
                angle_degrees = math.degrees(angle)
                self.ball_frames = []
                for im in balls1 :
                    self.ball_frames.append(pygame.transform.rotate(im, -angle_degrees + 180))
                size = (self.ball_frames[0]).get_size()
                self.ball = Snow(self.x, self.y, angle, target, size, self.ball_frames)
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
    def animator(self) :
        if self.ok == True or self.attack == False  :
            self.frame += 0.06
            if self.frame >= 10 and (self.animation_pack == snower1 or self.animation_pack == snower2) and self.ball not in Bullet.bullets :
                Bullet.bullets.append(self.ball)
            if self.frame >= 16:
                self.frame = 0
                if self.animation_pack == snower1 or self.animation_pack == snower2 :
                    if self.animation_pack == snower1 :
                        self.animation_pack = self.idle_animation1
                    else :
                        self.animation_pack = self.idle_animation2
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