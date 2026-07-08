from typing import List
import pygame
from enemybrrr import Enemy
from bulletbrrr import Bullet
from bulletbrrr import Bomb
from image_loader import *
screen = pygame.display.set_mode(( 1600, 900 ))
clock = pygame.time.Clock()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIRECTORY = os.path.join(BASE_DIR, "assets", "assets1")
pygame.init()

el_sound_effects = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"inf1.ogg"))
el_sound_effects2 = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"infll.mp3"))
el_sound_effects2.set_volume(2)
Dlvl1 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"lvl1.png")).convert_alpha()
Dlvl1 = pygame.transform.scale(Dlvl1, (420 / 2.5, 420 / 2.5))
Dlvl2 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"lvl2.png")).convert_alpha()
Dlvl2 = pygame.transform.scale(Dlvl2, (420 / 2.5, 420 / 2.5))
Dlvl3 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"lvl3.png")).convert_alpha()
Dlvl3 = pygame.transform.scale(Dlvl3, (420 / 2.5, 420 / 2.5))
Dlvl4 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"lvl4.png")).convert_alpha()
Dlvl4 = pygame.transform.scale(Dlvl4, (420 / 2.5, 420 / 2.5))
dm = 0
Blvl1 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"teslalvl1.png")).convert_alpha()
Blvl1 = pygame.transform.scale(Blvl1, (391 / 2, 293 / 2))
Blvl2 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"teslalvl2.png")).convert_alpha()
Blvl2 = pygame.transform.scale(Blvl2, (391 / 2, 293 / 2))
Blvl3 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"teslalvl3.png")).convert_alpha()
Blvl3 = pygame.transform.scale(Blvl3, (391 / 2, 293 / 2))
Blvl4 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"teslalvl4.png")).convert_alpha()
Blvl4 = pygame.transform.scale(Blvl4, (391 / 2, 293 / 2))

Clvl1 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl1.png")).convert_alpha()
Clvl1 = pygame.transform.scale(Clvl1, (512 / 2, 512 / 2))
Clvl2 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl2.png")).convert_alpha()
Clvl2 = pygame.transform.scale(Clvl2, (512 / 2, 512 / 2))
Clvl3 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl3.png")).convert_alpha()
Clvl3 = pygame.transform.scale(Clvl3, (512 / 2, 512 / 2))
Clvl4 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl4.png")).convert_alpha()
Clvl4 = pygame.transform.scale(Clvl4, (512 / 2, 512 / 2))

Flvl1 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl1.png")).convert_alpha()
Flvl1 = pygame.transform.scale(Flvl1, (512 / 2, 512 / 2))
Flvl2 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl2.png")).convert_alpha()
Flvl2 = pygame.transform.scale(Flvl2, (512 / 2, 512 / 2))
Flvl3 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl3.png")).convert_alpha()
Flvl3 = pygame.transform.scale(Flvl3, (512 / 2, 512 / 2))
Flvl4 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl4.png")).convert_alpha()
Flvl4 = pygame.transform.scale(Flvl4, (512 / 2, 512 / 2))

Alvl1 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl1.png")).convert_alpha()
Alvl1 = pygame.transform.scale(Alvl1, (512 / 2, 512 / 2))
Alvl2 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl2.png")).convert_alpha()
Alvl2 = pygame.transform.scale(Alvl2, (512 / 2, 512 / 2))
Alvl3 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl3.png")).convert_alpha()
Alvl3 = pygame.transform.scale(Alvl3, (512 / 2, 512 / 2))
Alvl4 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"wiz_lvl4.png")).convert_alpha()
Alvl4 = pygame.transform.scale(Alvl4, (512 / 2, 512 / 2))

Elvl1 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"teslalvl1.png")).convert_alpha()
Elvl1 = pygame.transform.scale(Elvl1, (391 / 2, 293 / 2))
Elvl2 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"teslalvl2.png")).convert_alpha()
Elvl2 = pygame.transform.scale(Elvl2, (391 / 2, 293 / 2))
Elvl3 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"teslalvl3.png")).convert_alpha()
Elvl3 = pygame.transform.scale(Elvl3, (391 / 2, 293 / 2))
Elvl4 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY2,"teslalvl4.png")).convert_alpha()
Elvl4 = pygame.transform.scale(Elvl4, (391 / 2, 293 / 2))

image = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"FestiveBow.png")).convert_alpha()
image = pygame.transform.scale(image, (174 / 4, 65 / 4))

image_rect = image.get_rect()
image_center = image_rect.center
def importer(frames, a=90, b=90, aa=0, bb=18, aaa=False) :
    lst = []
    for i in range(aa, bb):
        filename1 = frames.format(i)
        frame1 = pygame.image.load(filename1).convert_alpha()
        frame1 = pygame.transform.smoothscale(frame1, (a, b))
        frame1 = pygame.transform.flip(frame1, aaa, False)
        lst.append(frame1)
    return lst
frames = os.path.join(DEFAULT_DIRECTORY,"wizards ({:02d}).png")
wiz1 = importer(frames, aa=1, bb=17)
frames = os.path.join(DEFAULT_DIRECTORY,"fire_ball ({:01d}).gif")
fires = importer(frames, aa=0, bb=4, a=256 / 4, b=256 / 4)
frames = os.path.join(DEFAULT_DIRECTORY,"infball ({:02d}).gif")
infballs = importer(frames, aa=1, bb=76, a=406 / 4, b=422 / 4)
frames = os.path.join(DEFAULT_DIRECTORY,"laserbeam ({:02d}).gif")
lasers1 = importer(frames, aa=0, bb=4, a=185 / 4, b=1511 / 4)
lll = []
for laser in lasers1 :
    ll = pygame.transform.rotate(laser, 90)
    ll = pygame.transform.flip(ll, True, False)
    ll = pygame.transform.rotate(laser, 180)
    ll = pygame.transform.rotate(laser, 90)
    lll.append(ll)
lasers1 = lll

lasers2 = importer(frames, aa=4, bb=11, a=185 / 4, b=1511 / 4)
lll = []
for laser in lasers2 :
    ll = pygame.transform.rotate(laser, 90)
    ll = pygame.transform.flip(ll, True, False)
    ll = pygame.transform.rotate(laser, 180)
    ll = pygame.transform.rotate(laser, 90)
    lll.append(ll)
lasers2 = lll

lasers3 = importer(frames, aa=11, bb=15, a=185 / 4, b=1511 / 4)
lll = []
for laser in lasers3 :
    ll = pygame.transform.rotate(laser, 90)
    ll = pygame.transform.flip(ll, True, False)
    ll = pygame.transform.rotate(laser, 180)
    ll = pygame.transform.rotate(laser, 90)
    lll.append(ll)
lasers3 = lll
w, h = lasers1[0].get_size()
frames = os.path.join(DEFAULT_DIRECTORY,"eleball ({:02d}).gif")
eles = importer(frames, aa=1, bb=21, a=376 / 3.8, b=376 / 3.8)
frames = os.path.join(DEFAULT_DIRECTORY,"archer ({:02d}).png")
archer1 = importer(frames, aa=1, bb=33)
frames = os.path.join(DEFAULT_DIRECTORY,"archer ({:02d}).png")
archer2 = importer(frames, aa=1, bb=33, aaa= True)
frames = os.path.join(DEFAULT_DIRECTORY,"wizards ({:02d}).png")
wiz2 = importer(frames, aa=1, bb=17, aaa=True)

frames = os.path.join(DEFAULT_DIRECTORY,"lstwiz ({:02d}).png")
wizz2 = importer(frames, aa=1, bb=17, aaa=True)

frames = os.path.join(DEFAULT_DIRECTORY,"lstwiz ({:02d}).png")
wizz1 = importer(frames, aa=1, bb=17, aaa=False)

lighttor = []
frame_tor = []


dm = 0
lightningg = os.path.join(DEFAULT_DIRECTORY,"fire_m ({:02d}).gif")
fire_frames = []
for i in range(1, 17):
    filename1 = lightningg.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    image_sizelegg = frame1.get_size()
    frame1 = pygame.transform.smoothscale(frame1, (image_sizelegg[0] / 3.3, image_sizelegg[1] / 3.3))
    fire_frames.append(frame1)

lightningg = os.path.join(DEFAULT_DIRECTORY,"el ({:02d}).gif")
el_frames = []
for i in range(1, 50):
    filename1 = lightningg.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    image_sizeleggg = frame1.get_size()
    frame1 = pygame.transform.smoothscale(frame1, (image_sizeleggg[0] / 2.3, image_sizeleggg[1] / 2.3))
    el_frames.append(frame1)

def find_collision(point1, point2, point3, angle_degrees):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    m1 = (y2 - y1) / (x2 - x1)
    angle_radians = math.radians(angle_degrees)
    m2 = math.tan(angle_radians)
    b1 = y1 - m1 * x1
    b2 = y3 - m2 * x3
    x_intersection = (b2 - b1) / (m1 - m2)
    y_intersection = m1 * x_intersection + b1
    
    return x_intersection, y_intersection

rock_sound = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"rock.mp3"))
lightningg = os.path.join(DEFAULT_DIRECTORY,"g{:02d}.png")


DEFAULT_DIRECTORY = "C:/Users/HP/New folder/assets1" 
firefire = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"firefire.png")).convert_alpha()
firefire = pygame.transform.scale(firefire, (70, 70))
bb = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"Bomb.png")).convert_alpha()
bb = pygame.transform.scale(bb, (50, 50))
bb2 = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"Bombpoisoni.png")).convert_alpha()
bb2 = pygame.transform.scale(bb2, (50, 50))


cannon_frames = []
for i in range(0, 12):
    filename1 = lightningg.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    image_sizeleg = frame1.get_size()
    frame1 = pygame.transform.smoothscale(frame1, (image_sizeleg[0] / 5, image_sizeleg[1] / 5))
    cannon_frames.append(frame1)
lightb2 = []
animation_list = []
frame_b2 = []
wiz = wiz1
lightb2g = []
def determine_motion(current_loc, target_loc, reference_loc):
    vector_current = (current_loc[0] - reference_loc[0], current_loc[1] - reference_loc[1])
    vector_target = (target_loc[0] - reference_loc[0], target_loc[1] - reference_loc[1])
    cross_product = vector_current[0] * vector_target[1] - vector_current[1] * vector_target[0]
    
    if cross_product > 0:
        return -1
    elif cross_product < 0:
        return 1
frame_b2g = []
import math

class Cannon:
    cannons : List['Cannon'] = []
    def __init__(self, x, y, lvl, damage, model, cooldown, range = 500):
        self.x = x
        self.y = y
        self.lvl = lvl
        self.damage = damage
        self.model = model
        self.cooldown = cooldown
        self.last_bullet_time = pygame.time.get_ticks()
        self.range = range
        self.attack = False
        self.frame = 0
        self.bullet = None
        self.timer = None
        self.area = pygame.Rect(self.x - 100, self.y - 100, 200, 200)
        self.image = eval(f'{self.model}lvl{self.lvl}')
        self.animation_pack = None
        self.show_range = False

        Cannon.cannons.append(self)
        Enemy.all.append(self)

    def create_bullet(self):
        if self.model != 'G' and self.model != 'E' :
            current_time = pygame.time.get_ticks()
            if current_time - self.last_bullet_time >= self.cooldown:
                self.last_bullet_time += self.cooldown
                targets : List['Enemy'] = self.get_enemies_in_range()
                targets.sort(key=lambda target: target.x)
                if len(targets) != 0 :
                    target = targets[0]
                    by = targets[0].y
                    bx = targets[0].x
                    ix = self.x
                    iy = self.y
                    target_x = bx
                    target_y = by
                    if self.model == 'A' :
                        self.lst = targets
                        self.timer = True
                    elif self.model == 'D' :
                        
                        speed = 400
                        B = (target.x, target.y)
                        A = (self.x, self.y)
                        C = (target.target_x, target.target_y)
                        angle = math.atan2(by - self.y, bx - self.x)
                        AB = (-B[0] + A[0], -B[1] + A[1])
                        BC = (C[0] - B[0], C[1] - B[1])
                        dot_product = AB[0] * BC[0] + AB[1] * BC[1]
                        magnitude_AB = math.sqrt(AB[0]**2 + AB[1]**2)
                        magnitude_BC = math.sqrt(BC[0]**2 + BC[1]**2)
                        angle_rad = math.acos(dot_product / (magnitude_AB * magnitude_BC))
                        extra = math.asin((math.sin(angle_rad) * target.speed / speed))
                        heb = determine_motion((target.x, target.y), (target.target_x, target.target_y), (self.x, self.y))
                        angle = angle - heb * extra
                        size = (25, 25)
                        degrees = math.degrees(angle)
                        ahem = find_collision((target.x, target.y), (target.target_x, target.target_y), (self.x, self.y), (degrees))
                        bullet = Bullet(self.x, self.y, self.lvl, self.damage, self.model, target, angle, ahem[0], ahem[1], ix, iy, self.bullet_image,size, ahem=ahem, speedd=speed)
                        Bullet.bullets.append(bullet)
                    if self.model == 'A' :
                        self.archer = True
                        self.frame = 0
                        if self.x > target_x :
                            self.anim = archer2
                        else :
                            self.anim = archer1


                    if self.model == "D" :
                        channel = pygame.mixer.find_channel()
                        channel.play(cannon_sound)
                        Lx = self.x
                        Ly = self.y
                        lightb2.append([Lx,Ly])
                        frame_b2.append(0)

    def get_enemies_in_range(self):
        enemies_in_range = []
        for enemy in Enemy.enemies:
            enemy_x, enemy_y = enemy.x, enemy.y
            distance = math.sqrt((self.x - enemy_x) ** 2 + (self.y - enemy_y) ** 2)
            if distance <= self.range:
                enemies_in_range.append(enemy)
        return enemies_in_range
class ArcherTower(Cannon):
    def __init__(self, x, y, lvl, damage, model, cooldown, range=500):
        super().__init__(x, y, lvl, damage, model, cooldown, range)
        self.anim = archer1
        self.archer = False
    def animator(self) :
        x = self.x
        y = self.y
        screen.blit(self.image, (x- 512 / 4, y - 512 / 4))
        self.frame += 30 * Enemy.delta
        if self.frame >= 32 :
            self.frame = 0
            if self.archer == True :
                self.archer = False
        if self.archer == True :
            screen.blit(self.anim[int(self.frame)], (x- 35 - 10, y - 35 - 55 - 10))
            screen.blit(self.anim[int(self.frame)], (x- 35 - 10  + 15, y - 35 - 55))
            screen.blit(self.anim[int(self.frame)], (x- 35 - 10  - 15, y - 35 - 55))
            if int(self.frame) == 15 and self.timer == True :
                targets = self.lst
                self.projection_prediction(targets)
                self.timer = False
                if len(targets) > 1 :
                    self.projection_prediction(targets, a=-20, b=-50, ta=1)
                else :
                    self.projection_prediction(targets, a=-20, b=-50, ta=0)
                if len(targets) > 2 :
                    self.projection_prediction(targets, a=0, b=-30, ta=2)
                else :
                    self.projection_prediction(targets, a=0, b=-30, ta=0)
        else :
            screen.blit(self.anim[0], (x- 35 - 10, y - 35 - 55 - 10))
            screen.blit(self.anim[0], (x- 35 - 10 - 15, y - 35 - 55))
            screen.blit(self.anim[0], (x- 35 - 10 + 15, y - 35 - 55))

    def projection_prediction(self, targets, a=20, b=-50, ta=0):
        target = targets[ta]
        by = targets[ta].y
        bx = targets[ta].x
        ix = self.x + a
        iy = self.y + b
        speed = 750
        B = (target.x, target.y)
        A = (self.x + a, self.y + b)
        C = (target.target_x, target.target_y)
        angle = math.atan2(by - self.y - b, bx - self.x - a)
        AB = (-B[0] + A[0], -B[1] + A[1])
        BC = (C[0] - B[0], C[1] - B[1])
        dot_product = AB[0] * BC[0] + AB[1] * BC[1]
        magnitude_AB = math.sqrt(AB[0]**2 + AB[1]**2)
        magnitude_BC = math.sqrt(BC[0]**2 + BC[1]**2)
        angle_rad = math.acos(dot_product / (magnitude_AB * magnitude_BC))
        extra = math.asin((math.sin(angle_rad) * target.speed / speed))
        heb = determine_motion((target.x, target.y), (target.target_x, target.target_y), (self.x + a, self.y + b))
        angle = angle - heb * extra
        degrees = math.degrees(angle)
        rotated_image = pygame.transform.rotate(image, -degrees)
        size = rotated_image.get_size()
        self.bullet_image = rotated_image
        ahem = find_collision((target.x, target.y), (target.target_x, target.target_y), (self.x + a, self.y + b), (degrees))
        bullet = Bullet(self.x + a, self.y + b, self.lvl, self.damage, self.model, target, angle, ahem[0], ahem[1], ix, iy, self.bullet_image,size, ahem=ahem, speedd=speed)
        Bullet.bullets.append(bullet)      
class InfernoTower(Cannon):
    def __init__(self, x, y, lvl, damage, model, cooldown, range=500):
        super().__init__(x, y, lvl, damage, model, cooldown, range)
        self.Schannel = None
        self.dm = 0
        self.fframe = 0
        self.framel = 0
        self.f = []

    def animator(self):
        screen.blit(self.image, (self.x- 391 / 4 + 5, self.y - 293 / 4 - 20))
        if not self.attack:
            self.dm = 0
            enemies_in_range = self.get_enemies_in_range()
            if enemies_in_range != []:
                self.attack = True
                enemies_in_range.sort(key=lambda target: target.x, reverse=True)
                self.target = enemies_in_range[0]
        
        if self.attack:
            if self.animation_pack == None :
                self.animation_pack = lasers1
                channel = pygame.mixer.find_channel()
                channel.play(el_sound_effects)
                self.Schannel = pygame.mixer.find_channel()
                self.Schannel.play(el_sound_effects2, -1)
                self.target.inf = True
            if math.sqrt((self.x - self.target.x) ** 2 + (self.y - self.target.y) ** 2) <= self.range :
                self.dm += 0.02
                self.target.health -= self.dm
                if len(self.f) == 0 :
                    self.f.append(self.target)
                if self.target.health <= 0 :
                    self.Schannel.stop()
                    self.animation_pack = lasers3
                    self.framel = 0
                    Enemy.enemies_to_remove.append(self.target)
                    self.attack = False
            else:
                self.Schannel.stop()
                self.animation_pack = lasers3
                self.framel = 0
                self.attack = False
                self.target.inf = False
        if self.f != [] :
            self.framel += 14 * Enemy.delta 
            a = math.sqrt((self.x - self.f[0].x) ** 2 + (self.y - 50 - 70 - self.f[0].y) ** 2)
            angle = math.atan2( self.y - 50 - 70 - self.f[0].y, self.x - self.f[0].x)
            degrees = math.degrees(angle)
            ssrrimage = pygame.transform.scale(self.animation_pack[int(self.framel)], (2 * a, h))
            rrimage = pygame.transform.rotate(ssrrimage, -degrees)
            www, hhh= rrimage.get_size()
            screen.blit(rrimage, (self.x - www/2 , self.y - 50 - 70 - hhh/2))
            if self.framel >= len(self.animation_pack) - 1:
                self.framel = 0
                if self.animation_pack == lasers1 :
                    self.animation_pack = lasers2
                if self.animation_pack == lasers3 :
                    self.animation_pack = None
                    self.f = []
        self.fframe += 20 * Enemy.delta
        if self.fframe >= 74 :
            self.fframe = 0
        screen.blit(infballs[int(self.fframe)], (self.x- 406 / 8, self.y - 422 / 8 - 50 - 70))
class FelectroTower(Cannon):
    def __init__(self, x, y, lvl, damage, model, cooldown, range=500):
        super().__init__(x, y, lvl, damage, model, cooldown, range)
        if self.lvl == 3 :
            self.bullet_image = fires
        else :
            self.bullet_image = eles

    def animator(self):
        x = self.x
        y = self.y
        screen.blit(self.image, (x- 100, y - 75))
        if self.lvl == 3 :
            self.frame += 15 * Enemy.delta
            if self.frame >= 16 :
                self.frame = 0
            current_framehrr = fire_frames[int(self.frame)]
            screen.blit(current_framehrr, (x- image_sizelegg[0] / 6.6 - 5, y - image_sizelegg[1] / 6.6 - 80))
        elif self.lvl == 4 :
            self.frame += 15 * Enemy.delta
            if self.frame >= 49 :
                self.frame = 0      
            current_framehrr = el_frames[int(self.frame)]
            screen.blit(current_framehrr, (x- image_sizeleggg[0] / 4.6 - 5, y - image_sizeleggg[1] / 4.6 - 80))       

    def create_bullet(self):
            current_time = pygame.time.get_ticks()
            if current_time - self.last_bullet_time >= self.cooldown:
                self.last_bullet_time += self.cooldown
                targets : List['Enemy'] = self.get_enemies_in_range()
                targets.sort(key=lambda target: target.x)
                if len(targets) != 0 :
                    target = targets[0]
                    by = targets[0].y
                    bx = targets[0].x
                    ix = self.x
                    iy = self.y
                    if self.lvl == 3 :
                        ix = self.x
                        iy = self.y - 70
                        speed = 500
                        B = (target.x, target.y)
                        A = (self.x , self.y - 70)
                        C = (target.target_x, target.target_y)
                        angle = math.atan2(by - self.y + 70, bx - self.x)
                        AB = (-B[0] + A[0], -B[1] + A[1])
                        BC = (C[0] - B[0], C[1] - B[1])
                        dot_product = AB[0] * BC[0] + AB[1] * BC[1]
                        magnitude_AB = math.sqrt(AB[0]**2 + AB[1]**2)
                        magnitude_BC = math.sqrt(BC[0]**2 + BC[1]**2)
                        angle_rad = math.acos(dot_product / (magnitude_AB * magnitude_BC))
                        extra = math.asin((math.sin(angle_rad) * target.speed / speed))
                        heb = determine_motion((target.x, target.y), (target.target_x, target.target_y), (self.x , self.y - 70))
                        angle = angle - heb * extra
                        degrees = math.degrees(angle)
                        self.bullet_image = []
                        for frame in fires :
                            rotated_image = pygame.transform.rotate(frame, -degrees)
                            self.bullet_image.append(rotated_image)
                        size = self.bullet_image[0].get_size()
                        ahem = find_collision((target.x, target.y), (target.target_x, target.target_y), (self.x, self.y - 70), (degrees))
                        bullet = Bullet(self.x, self.y - 70, self.lvl, self.damage, self.model, target, angle, ahem[0], ahem[1], ix, iy, self.bullet_image,size, ahem=ahem, speedd=speed)
                        Bullet.bullets.append(bullet)
                    else :
                        B = (target.x, target.y)
                        A = (self.x , self.y - 70)
                        speed = 500
                        C = (target.target_x, target.target_y)
                        angle = math.atan2(by - self.y + 70, bx - self.x)
                        AB = (-B[0] + A[0], -B[1] + A[1])
                        BC = (C[0] - B[0], C[1] - B[1])
                        dot_product = AB[0] * BC[0] + AB[1] * BC[1]
                        magnitude_AB = math.sqrt(AB[0]**2 + AB[1]**2)
                        magnitude_BC = math.sqrt(BC[0]**2 + BC[1]**2)
                        angle_rad = math.acos(dot_product / (magnitude_AB * magnitude_BC))
                        extra = math.asin((math.sin(angle_rad) * target.speed / speed))
                        heb = determine_motion((target.x, target.y), (target.target_x, target.target_y), (self.x , self.y - 70))
                        angle = angle - heb * extra
                        degrees = math.degrees(angle)
                        size = self.bullet_image[0].get_size()
                        ahem = find_collision((target.x, target.y), (target.target_x, target.target_y), (self.x, self.y - 70), (degrees))
                        bullet = Bullet(self.x, self.y - 70, self.lvl, self.damage, self.model, target, angle, ahem[0], ahem[1], ix, iy, self.bullet_image,size, ahem=ahem, speedd=speed)
                        Bullet.bullets.append(bullet)
class WizardTower(Cannon):
    def __init__(self, x, y, lvl, damage, model, cooldown, range=500):
        super().__init__(x, y, lvl, damage, model, cooldown, range)
        self.anim = wiz1
        self.wiz = False
        self.bullet_image = None

    def animator(self):
        x = self.x
        y = self.y
        screen.blit(self.image, (x- 512 / 4, y - 512 / 4))
        self.frame += 20 * Enemy.delta
        if self.frame >= 16 :
            self.frame = 0
            if self.wiz == True :
                self.wiz = False
        if self.wiz == True :
            screen.blit(self.anim[int(self.frame)], (x- 35 - 10, y - 35 - 55))
        else :
            screen.blit(self.anim[0], (x- 35 - 10, y - 35 - 55))

    def create_bullet(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_bullet_time >= self.cooldown:
            self.last_bullet_time += self.cooldown
            targets : List['Enemy'] = self.get_enemies_in_range()
            targets.sort(key=lambda target: target.x)
            if len(targets) != 0 :
                target = targets[0]
                by = targets[0].y
                bx = targets[0].x
                ix = self.x
                iy = self.y
                speed = 1000
                B = (target.x, target.y)
                A = (self.x, self.y)
                C = (target.target_x, target.target_y)
                angle = math.atan2(by - self.y, bx - self.x)
                AB = (-B[0] + A[0], -B[1] + A[1])
                BC = (C[0] - B[0], C[1] - B[1])
                dot_product = AB[0] * BC[0] + AB[1] * BC[1]
                magnitude_AB = math.sqrt(AB[0]**2 + AB[1]**2)
                magnitude_BC = math.sqrt(BC[0]**2 + BC[1]**2)
                angle_rad = math.acos(dot_product / (magnitude_AB * magnitude_BC))
                extra = math.asin((math.sin(angle_rad) * target.speed / speed))
                heb = determine_motion((target.x, target.y), (target.target_x, target.target_y), (self.x, self.y))
                angle = angle - heb * extra
                degrees = math.degrees(angle)
                ahem = find_collision((target.x, target.y), (target.target_x, target.target_y), (self.x, self.y), (degrees))
                bullet = Bullet(self.x, self.y, self.lvl, self.damage, self.model, target, angle, ahem[0], ahem[1], ix, iy, self.bullet_image,size=None, ahem=ahem, speedd=speed)
                Bullet.bullets.append(bullet)
                self.wiz = True
                self.frame = 0
                if self.x > bx :
                    self.anim = wiz2
                else :
                    self.anim = wiz1                   
class Mortar(Cannon):
    def __init__(self, x, y, lvl, damage, model, cooldown, range=500):
        super().__init__(x, y, lvl, damage, model, cooldown, range)
        self.bullet_image = bb

    def animator(self) :
        x = self.x
        y = self.y
        screen.blit(self.image, (x- 80, y - 80))

    def create_bullet(self):
            current_time = pygame.time.get_ticks()
            if current_time - self.last_bullet_time >= self.cooldown:
                self.last_bullet_time += self.cooldown
                targets : List['Enemy'] = self.get_enemies_in_range()
                targets.sort(key=lambda target: target.x)
                if len(targets) != 0 :
                    target = targets[0]
                    by = targets[0].y
                    bx = targets[0].x
                    ix = self.x
                    iy = self.y-30
                    speed = min(math.sqrt((self.x - bx)**2+(self.y-50 - by)**2) * 1.5, 400)
                    B = (target.x, target.y)
                    A = (self.x, self.y-30)
                    C = (target.target_x, target.target_y)
                    angle = math.atan2(by - self.y+30, bx - self.x)
                    AB = (-B[0] + A[0], -B[1] + A[1])
                    BC = (C[0] - B[0], C[1] - B[1])
                    dot_product = AB[0] * BC[0] + AB[1] * BC[1]
                    magnitude_AB = math.sqrt(AB[0]**2 + AB[1]**2)
                    magnitude_BC = math.sqrt(BC[0]**2 + BC[1]**2)
                    angle_rad = math.acos(dot_product / (magnitude_AB * magnitude_BC))
                    extra = math.asin((math.sin(angle_rad) * target.speed / speed))
                    heb = determine_motion((target.x, target.y), (target.target_x, target.target_y), (self.x, self.y-30))
                    angle = angle - heb * extra
                    size = (25, 25)
                    degrees = math.degrees(angle)
                    ahem = find_collision((target.x, target.y), (target.target_x, target.target_y), (self.x, self.y-30), (degrees))
                    bullet = Bomb(self.x, self.y-30, self.lvl, self.damage, self.model, target, angle, ahem[0], ahem[1], ix, iy, self.bullet_image,size, ahem=ahem, speedd=speed)
                    Bullet.bullets.append(bullet)
                    channel = pygame.mixer.find_channel()
                    channel.play(cannon_sound)
                    Lx = self.x
                    Ly = self.y
                    lightb2.append([Lx,Ly])
                    frame_b2.append(0)
class TornadoTower(Cannon):
    def __init__(self, x, y, lvl, damage, model, cooldown, range=500):
        super().__init__(x, y, lvl, damage, model, cooldown, range)
        self.anim = wizz1
        self.wiz = False
        self.bullet_image = None

    def animator(self):
        x = self.x
        y = self.y
        screen.blit(self.image, (x- 512 / 4, y - 512 / 4))
        self.frame += 20 * Enemy.delta
        if self.frame >= 16 :
            self.frame = 0
            if self.wiz == True :
                self.wiz = False
        if self.wiz == True :
            screen.blit(self.anim[int(self.frame)], (x- 35 - 10, y - 35 - 55))
        else :
            screen.blit(self.anim[0], (x- 35 - 10, y - 35 - 55))

    def create_bullet(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_bullet_time >= self.cooldown:
            self.last_bullet_time += self.cooldown
            targets : List['Enemy'] = self.get_enemies_in_range()
            targets.sort(key=lambda target: target.x)
            if len(targets) != 0 :
                target = targets[0]
                by = targets[0].y
                bx = targets[0].x
                self.wiz = True
                self.frame = 0
                if self.x > bx :
                    self.anim = wizz2
                else :
                    self.anim = wizz1
                lighttor.append([bx, by])
                frame_tor.append(0)
                for enemy in Enemy.enemies:
                    if math.sqrt((bx - enemy.x) ** 2 + (by - enemy.y) ** 2) <= 200:
                        enemy.tornado = True
                        enemy.targetx = bx
                        enemy.targety = by
                        current_time = pygame.time.get_ticks()
                        enemy.tornado_duration = 1500 + current_time
class Smasher(Cannon):
    def __init__(self, x, y, lvl, damage, model, cooldown, range=500):
        self.x = x
        self.y = y
        self.lvl = lvl
        self.damage = damage
        self.model = model
        self.cooldown = cooldown
        self.last_bullet_time = pygame.time.get_ticks()
        self.range = range
        self.frame = 0
        self.frames = cannon_frames
        self.area = pygame.Rect(self.x - 100, self.y - 100, 200, 200)
        self.attack = False
        self.effect = False
        Cannon.cannons.append(self)
        Enemy.all.append(self)

    def animator(self):
        if not self.attack:
            screen.blit(self.frames[0], (self.x- image_sizeleg[0] / 10, self.y - image_sizeleg[1] / 10 - 80))
        else:
            self.frame += 15 * Enemy.delta
            if self.frame >= 12 :
                self.frame = 0
                self.attack = False
            if int(self.frame) == 3 and self.effect:
                Lx = self.x
                Ly = self.y
                lightb2g.append([Lx,Ly+50])
                frame_b2g.append(0)
                self.effect = False
            screen.blit(self.frames[int(self.frame)], (self.x- image_sizeleg[0] / 10, self.y - image_sizeleg[1] / 10 - 80))
        current_time = pygame.time.get_ticks()
        if current_time - self.last_bullet_time >= self.cooldown:
            self.last_bullet_time += self.cooldown
            targets : List['Enemy'] = self.get_enemies_in_range()
            if len(targets) != 0 :
                self.attack = True
                self.effect = True
                channel = pygame.mixer.find_channel()
                channel.play(rock_sound)
            for enemy in targets :
                current_timee = pygame.time.get_ticks()
                enemy.pause_duration = current_timee + 300
                enemy.health -= 100
                if enemy.health <= 0 :
                    Enemy.enemies_to_remove.append(enemy)