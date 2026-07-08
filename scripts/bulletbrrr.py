import math
import pygame
from enemybrrr import Enemy
from image_loader import *
screen = pygame.display.set_mode(( 1600, 900 ))
clock = pygame.time.Clock()
pygame.init()

lightb = []
frame_b = []
lightp = []
frame_p = []
lightpl = []
frame_pl = []
enemy_pl = []
lightpi = []
frame_pi = []
lightpib = []
frame_pib = []
lightpii = []
frame_pii = []
DEFAULT_DIRECTORY = "C:/Users/HP/New folder/assets1" 

image = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"FestiveBow.png")).convert_alpha()
image_rect = image.get_rect()
image_center = image_rect.center

firefire = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"firefire.png")).convert_alpha()
firefire = pygame.transform.scale(firefire, (70, 70))
base = os.path.join(DEFAULT_DIRECTORY,"pp{:02d}.png")
lightning = os.path.join(DEFAULT_DIRECTORY,"l{:01d}.gif")
fucking = os.path.join(DEFAULT_DIRECTORY,"p0.gif")
fucking = pygame.image.load(fucking).convert_alpha()
fucking = pygame.transform.smoothscale(fucking, (50, 50))
laser_attack_sound = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"laser_attack.ogg"))
arrow_sound = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"arrow_hit.ogg"))
bbbb7 = os.path.join(DEFAULT_DIRECTORY,"blood7 ({:02d}).gif")
blood7 = []
for i in range(11):
    fib = bbbb7.format(i)
    frb = pygame.image.load(fib).convert_alpha()
    frb = pygame.transform.smoothscale(frb, (140, 140))
    blood7.append(frb)
animationp = []
for i in range(0, 12):
    filename1 = base.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    image_sizele = frame1.get_size()
    frame1 = pygame.transform.smoothscale(frame1, (image_sizele[0] / 10 , image_sizele[1]  / 10))
    animationp.append(frame1)
lightning_effect = []
for i in range(9):
    fil = lightning.format(i)
    frl = pygame.image.load(fil).convert_alpha()
    lightning_effect.append(frl)
e_sound_effects = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"magic_jail.ogg"))

class Bullet :
    bullets = []
    bullets_to_remove = []
    def __init__(self, x, y, lvl, damage, model, target, angle, target_x, target_y, ix, iy, image, size, ahem, speedd) -> None:
        self.x = x
        self.y = y
        self.lvl = lvl
        self.damage = damage
        self.model = model
        self.target = target
        self.target_x = target_x
        self.target_y = target_y
        self.ix = ix
        self.iy = iy
        self.angle = math.atan2(self.target_y - self.y, self.target_x - self.x)
        self.frame = 0
        self.size = size
        self.image = image
        self.ahem = ahem
        self.speed = speedd
    def bullet_move(self) :
        self.x += self.speed * math.cos(self.angle) * Enemy.delta
        self.y += self.speed * math.sin(self.angle) * Enemy.delta
        if math.sqrt((self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2) <= 20 :
            Bullet.bullets_to_remove.append(self)
            if math.sqrt((self.target.x - self.x) ** 2 + (self.target.y - self.y) ** 2) <= 30 :
                self.target.health -= self.damage
            if self.target.health <= 0 :
                Enemy.enemies_to_remove.append(self.target)
            if self.model == 'D' :
                if self.lvl != 4 :
                    Lx = self.x
                    Ly = self.y
                    lightb.append([Lx,Ly])
                    frame_b.append(0)
                else :
                    Lx = self.x
                    Ly = self.y
                    lightp.append([Lx,Ly])
                    frame_p.append(0)
                channel = pygame.mixer.find_channel()
                channel.play(explosive_sound_effects)
                for enemy in Enemy.enemies :
                    if math.sqrt((enemy.x - self.target_x) ** 2 + (enemy.y - self.target_y) ** 2) <= 100 :
                        enemy.health -= self.damage / 1.5
                        if self.lvl == 4 :
                            current_time = pygame.time.get_ticks()
                            enemy.fire_duration = 2000 + current_time
                        if enemy.health <= 0 :
                            Enemy.enemies_to_remove.append(enemy)

            elif self.model == 'B' :
                if self.lvl == 3 :
                    current_time = pygame.time.get_ticks()
                    self.target.fire_duration = 2000 + current_time
                    self.target.firee = True
                elif self.lvl == 4 :
                    Lx = self.target.x
                    Ly = self.target.y
                    lightpii.append([Lx,Ly])
                    frame_pii.append(0)
                    channel = pygame.mixer.find_channel()
                    channel.play(e_sound_effects)
                    current_time = pygame.time.get_ticks()
                    self.target.pause_duration = 1000 + current_time
                else :
                    Llx = self.x
                    Lly = self.y
                    lightpl.append([Llx,Lly])
                    frame_pl.append(0)
                    enemy_pl.append(self.target)


            elif self.model == 'C' :
                Lx = self.target.x
                Ly = self.target.y
                lightpi.append([Lx,Ly])
                frame_pi.append(0)
                lightpii.append([Lx,Ly])
                frame_pii.append(0)
                current_time = pygame.time.get_ticks()
                self.target.pause_duration = 500 + current_time
                channel = pygame.mixer.find_channel()
                channel.play(laser_attack_sound)
            elif self.model == 'A' :
                Lx = self.target.x
                Ly = self.target.y
                lightpib.append([Lx,Ly])
                frame_pib.append(0)
                channel = pygame.mixer.find_channel()
                channel.play(arrow_sound)
    def bullet_draw(self) :
        if self.model == 'D' :
            distance1 = math.sqrt((self.ix - self.x) ** 2 + (self.iy - self.y) ** 2)
            distance2 = math.sqrt((self.target_x - self.ix) ** 2 + (self.target_y - self.iy) ** 2)
            window.blit(circle_image, (self.x, self.y))
            screen.blit(self.image, (self.x - 25, self.y - 25 - math.sin((math.pi)*distance1/distance2)* 200))
        elif self.model == 'B' :
            if self.lvl == 3 :
                self.frame += 0.06
                if self.frame >= 4:
                    self.frame = 0
                screen.blit(self.image[int(self.frame)], (self.x - self.size[0] / 2, self.y - self.size[1] / 2))
            elif self.lvl == 4 :
                self.frame += 0.06
                if self.frame >= 20:
                    self.frame = 0
                screen.blit(self.image[int(self.frame)], (self.x - 376 / 7.8 , self.y - 376 / 7.8))

        elif self.model == 'A' :
            screen.blit(self.image, (self.x - self.size[0]/2, self.y - self.size[1]/2))
class Bomb(Bullet):
    def bullet_move(self):
        self.x += self.speed * math.cos(self.angle) * Enemy.delta
        self.y += self.speed * math.sin(self.angle) * Enemy.delta
        if math.sqrt((self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2) <= 4 :
            Bullet.bullets_to_remove.append(self)
            if math.sqrt((self.target.x - self.x) ** 2 + (self.target.y - self.y) ** 2) <= 30 :
                self.target.health -= self.damage
            if self.target.health <= 0 :
                Enemy.enemies_to_remove.append(self.target)
            if self.lvl != 4 :
                Lx = self.x
                Ly = self.y
                lightb.append([Lx,Ly])
                frame_b.append(0)
                channel = pygame.mixer.find_channel()
                channel.play(explosive_sound_effects)
                for enemy in Enemy.enemies :
                    if math.sqrt((enemy.x - self.target_x) ** 2 + (enemy.y - self.target_y) ** 2) <= 100 :
                        enemy.health -= self.damage / 1.5
                        if self.lvl == 4 :
                            current_time = pygame.time.get_ticks()
                            enemy.fire_duration = 2000 + current_time
                        if enemy.health <= 0 :
                            Enemy.enemies_to_remove.append(enemy)
            else :
                Lx = self.x
                Ly = self.y
                lightp.append([Lx,Ly])
                frame_p.append(0)
                channel = pygame.mixer.find_channel()
                channel.play(explosive_sound_effects)
                for enemy in Enemy.enemies :
                    if math.sqrt((enemy.x - self.target_x) ** 2 + (enemy.y - self.target_y) ** 2) <= 100 :
                        enemy.health -= self.damage / 1.5
                        if self.lvl == 4 :
                            current_time = pygame.time.get_ticks()
                            enemy.fire_duration = 2000 + current_time
                        if enemy.health <= 0 :
                            Enemy.enemies_to_remove.append(enemy)