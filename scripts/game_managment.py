import pygame

import pygame_gui
import math
import os
from typing import List
from enemybrrr import Enemy
from cannonbrrr import Cannon
from cannonbrrr import ArcherTower
from cannonbrrr import Mortar
from cannonbrrr import InfernoTower
from cannonbrrr import WizardTower
from cannonbrrr import Smasher
from cannonbrrr import FelectroTower
from cannonbrrr import TornadoTower
from bulletbrrr import Bullet
from barracks import Barracks
from herobrrr import Hero
import bulletbrrr
import cannonbrrr
import creator
import random
from sheep import Sheep
framer = 0
import image_loader
from test3 import window_managment
from test3 import window_managment_update
pygame.mixer.set_num_channels(50)
hero_points = {
"(726, 159)": 0,
"(710, 247)": 0,
"(767, 320)": 0,
"(709, 395)": 0,
"(604, 425)": 0,
"(492, 414)": 0,
"(394, 343)": 0,
"(250, 336)": 0,
"(330, 581)": 0,
"(499, 596)": 0,
"(648, 602)": 0,
"(770, 629)": 0,
"(822, 743)": 0,
"(902, 572)": 0,
"(1045, 509)": 0,
"(1159, 631)": 0,
"(1305, 679)": 0,
"(1109, 395)": 0,
"(1204, 315)": 0,
"(1313, 246)": 0,
"(1420, 237)": 0
}



screen = pygame.display.set_mode((1600, 900))
manager = pygame_gui.UIManager((1600, 900))



paths = [[(800, 0), (756, 68), (687, 117), (645, 210), (684, 305), (682, 359), (556, 389), (498, 368), (472, 305), (309, 293), (171, 288), (37, 293)]
,[(841, 0), (788, 79), (715, 135), (687, 207), (709, 300), (705, 385), (555, 418), (476, 396), (451, 345), (306, 328), (173, 321), (36, 325)]
,[(886, 0), (828, 99), (739, 152), (728, 206), (756, 289), (728, 418), (554, 456), (454, 430), (414, 372), (303, 368), (176, 360), (36, 368)]
,[(1600, 204), (1403, 220), (1277, 243), (1182, 307), (1088, 399), (1015, 495), (905, 545), (788, 584), (652, 593), (449, 578), (272, 567), (32, 561)]
,[(907, 900), (887, 814), (829, 715), (785, 631), (657, 584), (514, 572), (323, 564), (32, 560)]
,[(865, 880), (844, 816), (805, 747), (725, 631), (527, 628), (357, 610), (170, 610), (31, 604)]]

def effect_animator():
    pass



path_points1 = [(800, 17), (756, 68), (687, 117), (645, 210), (684, 305), (682, 359), (556, 389), (498, 368), (472, 305), (309, 293), (171, 288), (37, 293)]
path_points2 = [(841, 18), (788, 79), (715, 135), (687, 207), (709, 300), (705, 385), (555, 418), (476, 396), (451, 345), (306, 328), (173, 321), (36, 325)]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIRECTORY = os.path.join(BASE_DIR, "assets", "assets1")
flag = []
for i in range(16):
    fffrg = image_loader.ufg.format(i)
    firrg = pygame.image.load(fffrg).convert_alpha()
    firrg = pygame.transform.smoothscale(firrg, (100, 75))
    flag.append(firrg)
up_sound = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"upgrade_succeed.ogg"))
fail_sound = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"upgrade_failed.ogg"))
build_sound = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"build_tower.ogg"))

hd1 = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"hero_death_1.ogg"))
hd2 = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"hero_death_2.ogg"))
hd3 = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"hero_death_3.ogg"))

bb = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"Bomb.png")).convert_alpha()
bb = pygame.transform.scale(bb, (50, 50))
running  = True
crusor = os.path.join(DEFAULT_DIRECTORY,"finger_up.png")
sheep_sound = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"sheep.ogg"))
cursor_image = pygame.image.load(crusor).convert_alpha()
image_sizelec = cursor_image.get_size()
cursor_img_rect = cursor_image.get_rect()

crusord = os.path.join(DEFAULT_DIRECTORY,"finger_up.png")
cursor_imaged = pygame.image.load(crusord).convert_alpha()
image_sizelecd = cursor_imaged.get_size()
cursor_imaged = pygame.transform.smoothscale(cursor_imaged, (image_sizelecd[0]/3, image_sizelecd[1]/3))
cursor_img_rectd = cursor_imaged.get_rect()

crusordp = os.path.join(DEFAULT_DIRECTORY,"finger_down.png")
cursor_imagedp = pygame.image.load(crusordp).convert_alpha()
image_sizelecdp = cursor_imagedp.get_size()
cursor_imagedp = pygame.transform.smoothscale(cursor_imagedp, (image_sizelecdp[0]/3, image_sizelecdp[1]/3))
cursor_img_rectdp = cursor_imagedp.get_rect()
pressed = False


clock = pygame.time.Clock()
r_effect = []
for i in range(7):
    fffr = image_loader.uf.format(i)
    firr = pygame.image.load(fffr).convert_alpha()
    firr = pygame.transform.smoothscale(firr, (200, 200))
    r_effect.append(firr)

pygame.init() 
poison_effect = []
for i in range(23):
    fffp = image_loader.po.format(i)
    firp = pygame.image.load(fffp).convert_alpha()
    firp = pygame.transform.smoothscale(firp, (150, 150))
    poison_effect.append(firp)
hero_idle = os.path.join(DEFAULT_DIRECTORY,"herolvl1 ({:02d}).png")
hero_walk = os.path.join(DEFAULT_DIRECTORY,"herolvl1w ({:02d}).png")
hero_attack2 = os.path.join(DEFAULT_DIRECTORY,"herolvl1s ({:02d}).png")
hero_attack = os.path.join(DEFAULT_DIRECTORY,"herolvl1j ({:02d}).png")
pygame.mixer.music.load(os.path.join(DEFAULT_DIRECTORY,"kro_bgmusic_t2_battle1.mp3"))
pygame.mixer.music.play(-1)
lightning_effecth = []
for i in range(11):
    filh = image_loader.lightningh.format(i)
    frlh = pygame.image.load(filh).convert_alpha()
    frlh = pygame.transform.smoothscale(frlh, (200, 200))
    lightning_effecth.append(frlh)

animation_idle_hero = []
for i in range(1, 17):
    filename1 = hero_idle.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (120, 120))
    frame1 = pygame.transform.flip(frame1, True, False)
    animation_idle_hero.append(frame1)

animation_attack_hero = []
for i in range(1, 17):
    filename1 = hero_attack.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (120, 120))
    frame1 = pygame.transform.flip(frame1, True, False)
    animation_attack_hero.append(frame1)

#sheep = Sheep(500, 500)
specific_area = pygame.Rect(500, 500, 50, 50)
lightning = os.path.join(DEFAULT_DIRECTORY,"l{:01d}.gif")
bbbb7 = os.path.join(DEFAULT_DIRECTORY,"blood7 ({:02d}).gif")
blood7 = []
for i in range(11):
    fib = bbbb7.format(i)
    frb = pygame.image.load(fib).convert_alpha()
    frb = pygame.transform.smoothscale(frb, (480 / 4.5, 270 / 4.5))
    blood7.append(frb)

lightning_effect = []
for i in range(9):
    fil = lightning.format(i)
    frl = pygame.image.load(fil).convert_alpha()
    lightning_effect.append(frl)

exp_effects = []
for i in range(0, 6):
    filename1 = image_loader.effects.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (140, 140))
    exp_effects.append(frame1)

frame_death = []
heb = []
deaths = []


lightningg = os.path.join(DEFAULT_DIRECTORY,"g{:02d}.png")
cannon_frames = []
for i in range(0, 12):
    filename1 = lightningg.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    image_sizeleg = frame1.get_size()
    frame1 = pygame.transform.smoothscale(frame1, (image_sizeleg[0] / 2, image_sizeleg[1] / 2))
    cannon_frames .append(frame1)


lightningg = os.path.join(DEFAULT_DIRECTORY,"smash ({:01d}).png")
bang_frames = []
for i in range(0, 4):
    filename1 = lightningg.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    image_sizelegg = frame1.get_size()
    frame1 = pygame.transform.smoothscale(frame1, (image_sizelegg[0] / 3, image_sizelegg[1] / 3))
    bang_frames.append(frame1)



animation_attack2_hero = []
for i in range(1, 17):
    filename1 = hero_attack2.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (120, 120))
    frame1 = pygame.transform.flip(frame1, True, False)
    animation_attack2_hero.append(frame1)


animation_walk_hero = []
for i in range(1, 17):
    filename1 = hero_walk.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (120, 120))
    frame1 = pygame.transform.flip(frame1, True, False)
    animation_walk_hero.append(frame1)


animation_walk_hero2 = []
for i in range(1, 17):
    filename1 = hero_walk.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (120, 120))
    animation_walk_hero2.append(frame1)

barracks_image = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"barracks.png")).convert_alpha()
barracks_image = pygame.transform.scale(barracks_image, (200, 160))

hd_lst = [hd1, hd2, hd3]




lighttor = cannonbrrr.lighttor
frame_tor = cannonbrrr.frame_tor


lightb = bulletbrrr.lightb
frame_b = bulletbrrr.frame_b
lightp = bulletbrrr.lightp
frame_p = bulletbrrr.frame_p
lightpl = bulletbrrr.lightpl
frame_pl = bulletbrrr.frame_pl
lightb2 = cannonbrrr.lightb2
frame_b2 = cannonbrrr.frame_b2

lightb2g = cannonbrrr.lightb2g
frame_b2g = cannonbrrr.frame_b2g

frame_back = 0
lightpi = bulletbrrr.lightpi
frame_pi = bulletbrrr.frame_pi
lightpib = bulletbrrr.lightpib
frame_pib = bulletbrrr.frame_pib
lightpii = bulletbrrr.lightpii
frame_pii = bulletbrrr.frame_pii

DEFAULT_DIRECTORY = "C:/Users/HP/New folder/assets1" 
back = os.path.join(DEFAULT_DIRECTORY,"backmain.png")
explosive_sound_effects = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"exp_sound.ogg"))
hero1_sound_effects = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"summon_hero1.ogg"))
hero2_sound_effects = pygame.mixer.Sound(os.path.join(DEFAULT_DIRECTORY,"summon_hero2.ogg"))

frame_fire = 0
pygame.mouse.set_visible(False)
DEFAULT_DIRECTORY = "C:/Users/HP/New folder/assets1" 
base_filenameskedA = os.path.join(DEFAULT_DIRECTORY,"1_Reaper_Man_Dying_{:03d}.png")
base_filenameskedAA = os.path.join(DEFAULT_DIRECTORY,"1_Reaper_Man_Walking_{:03d}.png")
animation_deathB = []
pointers = []
for i in range(0, 15):
    filename1 = base_filenameskedA.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (100, 100))
    animation_deathB.append(frame1)
animation_walkB = []
for i in range(0, 23):
    filename1 = base_filenameskedAA.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (100, 100))
    animation_walkB.append(frame1)
animation_attackB = []
for i in range(0, 23):
    filename1 = base_filenameskedAA.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (100, 100))
    animation_attackB.append(frame1)


def importer(frames, a=120, b=120, aa=1, bb=17, aaa=True) :
    lst = []
    for i in range(aa, bb):
        filename1 = frames.format(i)
        frame1 = pygame.image.load(filename1).convert_alpha()
        frame1 = pygame.transform.smoothscale(frame1, (a, b))
        frame1 = pygame.transform.flip(frame1, aaa, False)
        lst.append(frame1)
    return lst



frames = os.path.join(DEFAULT_DIRECTORY,"snower ({:02d}).png")
snower1 = importer(frames)
snower2 = importer(frames, aaa=False)

frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl1w ({:02d}).png")
walking_animation1 = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl1w ({:02d}).png")
walking_animationn1 = importer(frames, aaa=False)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl1 ({:02d}).png")
idle_animation1 = importer(frames)
idle_animationn1 = importer(frames, aaa=False)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl1s ({:02d}).png")
attack_animation1 = importer(frames, aaa=False)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl1j ({:02d}).png")
attack_animationn1 = importer(frames, aaa=False)

frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl2w ({:02d}).png")
walking_animation2 = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl2w ({:02d}).png")
walking_animationn2 = importer(frames, aaa=False)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl2 ({:02d}).png")
idle_animation2 = importer(frames)
idle_animationn2 = importer(frames, aaa=False)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl2s ({:02d}).png")
attack_animation2 = importer(frames, aaa=False)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl2j ({:02d}).png")
attack_animationn2 = importer(frames, aaa=False)

frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl3w ({:02d}).png")
walking_animation3 = importer(frames)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl3w ({:02d}).png")
walking_animationn3 = importer(frames, aaa=False)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl3 ({:02d}).png")
idle_animation3 = importer(frames)
idle_animationn3 = importer(frames, aaa=False)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl3s ({:02d}).png")
attack_animation3 = importer(frames, aaa=False)
frames = os.path.join(DEFAULT_DIRECTORY,"heroolvl3j ({:02d}).png")
attack_animationn3 = importer(frames, aaa=False)
ffff = os.path.join(DEFAULT_DIRECTORY,"ff ({:02d}).gif")
animation_tornado = []
for i in range(0, 32):
    filename1 = ffff.format(i)
    frame1 = pygame.image.load(filename1).convert_alpha()
    frame1 = pygame.transform.smoothscale(frame1, (595 / 2, 418 / 2))
    frame1.set_alpha(220)
    animation_tornado.append(frame1)
imagef = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"FestiveBow.png")).convert_alpha()
imagef = pygame.transform.scale(imagef, (174 / 4, 65 / 4))

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

def move_point_away(p1, p2, p, distance= 10, side=False):
    v = (p2[0] - p1[0], p2[1] - p1[1])
    magnitude = math.sqrt(v[0]**2 + v[1]**2)
    u = (v[1]/magnitude, -v[0]/magnitude)
    if side == False:
        u = (-u[0], -u[1])
    new_point = (p[0] + distance*u[0], p[1] + distance*u[1])
    return new_point


level_up = False
champ_move = False
back2 = pygame.image.load(back).convert_alpha()
back2 = pygame.transform.smoothscale(back2, (1600, 900))
clock = pygame.time.Clock()

### main game loop logic###
def main() :
    update = False
    build = False
    money = 100000
    global running, champ_move, framer, frame_fire, pressed
    while running == True :
        frame_fire += 0.05
        if frame_fire >= 16 :
            frame_fire = 0
        dt = clock.tick(60) / 1000.0
        Enemy.delta = dt
        screen.blit(back2, (0 , 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and not build and not update:
                    mouse_posss = pygame.mouse.get_pos()
                    button1, button2 , button3, button4 ,button5, button6, window = window_managment(mouse_posss[0], mouse_posss[1], manager=manager)
                    window.show()
                    build = True
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                    ### building towers logic ###
                    if event.ui_element == button1:
                        cannon = ArcherTower(mouse_posss[0], mouse_posss[1],1, 300, 'A', 1500, 300)
                        channel = pygame.mixer.find_channel()
                        channel.play(build_sound)
                        build = False
                    elif event.ui_element == button2:
                        cannon = TornadoTower(mouse_posss[0], mouse_posss[1],1, 300, 'F', 3000, 300)
                        channel = pygame.mixer.find_channel()
                        channel.play(build_sound)
                        build = False
                    elif event.ui_element == button3:
                        cannon = Mortar(mouse_posss[0], mouse_posss[1],1, 300, 'D', 3000, 200)
                        channel = pygame.mixer.find_channel()
                        channel.play(build_sound)
                        build = False
                    elif event.ui_element == button4:
                        cannon = InfernoTower(mouse_posss[0], mouse_posss[1],1, 300, 'E', 1000, 200)
                        channel = pygame.mixer.find_channel()
                        channel.play(build_sound)
                        build = False
                    elif event.ui_element == button5:
                        cannon = Smasher(mouse_posss[0], mouse_posss[1],1, 800, 'G', 3000, 200)
                        channel = pygame.mixer.find_channel()
                        channel.play(build_sound)
                        build = False
                    elif event.ui_element == button6:
                        cannon = FelectroTower(mouse_posss[0], mouse_posss[1],1, 300, 'B', 1000, 200)
                        channel = pygame.mixer.find_channel()
                        channel.play(build_sound)
                        build = False
                    ### building towers logic ###
                    
    
                    elif event.ui_element == buttonU:
                        ### upgrade towers logic ###
                        if money >= 100 * up_cannon.lvl :
                            if up_cannon.model == 'E':
                                if up_cannon.attack:
                                    up_cannon.Schannel.stop()
                            if up_cannon.model == 'A':
                                aaa = ArcherTower
                            elif up_cannon.model == 'E':
                                aaa = InfernoTower
                            elif up_cannon.model == 'D':
                                aaa = Mortar
                            elif up_cannon.model == 'C':
                                aaa = WizardTower
                            elif up_cannon.model == 'B':
                                aaa = FelectroTower
                            elif up_cannon.model == 'F':
                                aaa = TornadoTower
                            cannon_j = aaa(up_cannon.x, up_cannon.y, up_cannon.lvl + 1 , up_cannon.damage, up_cannon.model, up_cannon.cooldown, up_cannon.range)
                            Cannon.cannons.remove(up_cannon)
                            Enemy.all.remove(up_cannon)
                            channel = pygame.mixer.find_channel()
                            channel.play(up_sound)
                            money -= 100 * up_cannon.lvl
                        else:
                            channel = pygame.mixer.find_channel()
                            channel.play(fail_sound)

                        windowU.hide()
                        update = False
                    window.hide()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s :
                    running = False
                    Enemy.running = False
                if event.key == pygame.K_SPACE:
                    champ_move = True
                if event.key == pygame.K_p:
                    Enemy.pause = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                pressed = True
                if event.button == 3:
                    mouse_pos = pygame.mouse.get_pos()
                    barracks = Barracks(mouse_pos[0], mouse_pos[1], 0, barracks_image=barracks_image, hero_points=hero_points)
                        ### upgrade towers logic ###
                    
                    
                if event.button == 1 :
                    ### upgrade hero logic ###
                    mouse_pos = pygame.mouse.get_pos()
                    fps = clock.get_fps()
                    #lighttor.append([mouse_pos[0], mouse_pos[1]])
                    #frame_tor.append(0)
                    #for enemy in Enemy.enemies:
                    #    if math.sqrt((mouse_pos[0] - enemy.x) ** 2 + (mouse_pos[1] - enemy.y) ** 2) <= 200:
                    #        enemy.tornado = True
                    #        enemy.targetx = mouse_pos[0]
                    #        enemy.targety = mouse_pos[1]
                    #        current_time = pygame.time.get_ticks()
                    #        enemy.tornado_duration = 1500 + current_time
                    #if sheep.area.collidepoint(mouse_pos[0], mouse_pos[1]) == True and sheep.animation_pack != sheep.walking and sheep.animation_pack != sheep.death :
                    #    sheep.sheep_pressed()
                    #    channel = pygame.mixer.find_channel()
                    #    channel.play(sheep_sound)
                    #    sheep.clicked += 1
                    #    if sheep.clicked == 10 and sheep in Sheep.sheeps:
                    #        sheep.animation_pack = sheep.death
                    #        sheep.frame = 0
                    for barrack in  Barracks.barracks :
                        if barrack.area.collidepoint(mouse_pos[0], mouse_pos[1]) == True :
                            if barrack.level_up == True :
                                if len(barrack.hero1) != 0 :
                                    (barrack.hero1[0]).lvl +=1
                                    (barrack.hero1[0]).health = (barrack.hero1[0].max_health)
                                    (barrack.hero1[0]).walking_animation1 = eval(f'walking_animation{(barrack.hero1[0]).lvl}')
                                    (barrack.hero1[0]).walking_animation2 = eval(f'walking_animationn{(barrack.hero1[0]).lvl}')
                                    (barrack.hero1[0]).idle_animation1 = eval(f'idle_animation{(barrack.hero1[0]).lvl}')
                                    (barrack.hero1[0]).idle_animation2 = eval(f'idle_animationn{(barrack.hero1[0]).lvl}')
                                    (barrack.hero1[0]).attack_animation1 = eval(f'attack_animation{(barrack.hero1[0]).lvl}')
                                    (barrack.hero1[0]).attack_animation2 = eval(f'attack_animationn{(barrack.hero1[0]).lvl}')
                                    (barrack.hero1[0]).animation_pack = eval(f'idle_animation{(barrack.hero1[0]).lvl}')
                                if len(barrack.hero2) != 0 :
                                    (barrack.hero2[0]).lvl +=1
                                    (barrack.hero2[0]).health = (barrack.hero1[0].max_health)
                                    (barrack.hero2[0]).walking_animation1 = eval(f'walking_animation{(barrack.hero2[0]).lvl}')
                                    (barrack.hero2[0]).walking_animation2 = eval(f'walking_animationn{(barrack.hero2[0]).lvl}')
                                    (barrack.hero2[0]).idle_animation1 = eval(f'idle_animation{(barrack.hero2[0]).lvl}')
                                    (barrack.hero2[0]).idle_animation2 = eval(f'idle_animationn{(barrack.hero2[0]).lvl}')
                                    (barrack.hero2[0]).attack_animation1 = eval(f'attack_animation{(barrack.hero2[0]).lvl}')
                                    (barrack.hero2[0]).attack_animation2 = eval(f'attack_animationn{(barrack.hero2[0]).lvl}')
                                    (barrack.hero2[0]).animation_pack = eval(f'idle_animation{(barrack.hero2[0]).lvl}')
                                if len(barrack.hero3) != 0 :
                                    (barrack.hero3[0]).lvl +=1
                                    (barrack.hero3[0]).health = (barrack.hero1[0].max_health)
                                    (barrack.hero3[0]).walking_animation1 = eval(f'walking_animation{(barrack.hero3[0]).lvl}')
                                    (barrack.hero3[0]).walking_animation2 = eval(f'walking_animationn{(barrack.hero3[0]).lvl}')
                                    (barrack.hero3[0]).idle_animation1 = eval(f'idle_animation{(barrack.hero3[0]).lvl}')
                                    (barrack.hero3[0]).idle_animation2 = eval(f'idle_animationn{(barrack.hero3[0]).lvl}')
                                    (barrack.hero3[0]).attack_animation1 = eval(f'attack_animation{(barrack.hero3[0]).lvl}')
                                    (barrack.hero3[0]).attack_animation2 = eval(f'attack_animationn{(barrack.hero3[0]).lvl}')
                                    (barrack.hero3[0]).animation_pack = eval(f'idle_animation{(barrack.hero3[0]).lvl}')
                                if barrack.lvl != 3 :
                                    barrack.lvl += 1
                                    barrack.level_up = False
                                    barrack.area = pygame.Rect(barrack.x - 100, barrack.y - 100, 200, 200)
                                    break
                            barrack.level_up = True
                        else :
                            barrack.level_up = False
                            barrack.area = pygame.Rect(barrack.x - 100, barrack.y - 100, 200, 200)
                    for cannon in Cannon.cannons :
                        if cannon.area.collidepoint(mouse_pos[0], mouse_pos[1]) == True and not update and not build:
                            if cannon.lvl != 4 :
                                txt = f'lvl{cannon.lvl+1}:{100*cannon.lvl}'
                                buttonU, windowU = window_managment_update(mouse_pos[0], mouse_pos[1], manager, txt)
                                up_cannon = cannon
                                windowU.show()
                                update = True
                            cannon.show_range = True
                        else:
                            cannon.show_range = False
                    ### upgrade hero logic ###
                            
            else :
                pressed = False

            ### effects and game logic ###
            manager.process_events(event)
        for hero in Hero.heros :
            hero.hero_state(hd_lst)
        for enemy in Enemy.enemies :
            enemy.update_enemy_pos()

            
        ### enemy death animation ###
        marked_for_removal = []
        for j in range(len(frame_death)):
            frame_death[j] += 30 * Enemy.delta
            if frame_death[j] >= 16:
                marked_for_removal.append(j)
        marked_for_removal.reverse()
        for index in marked_for_removal:
            frame_death.pop(index)
            heb.pop(index)
            deaths.pop(index)
        for j in range(len(frame_death)):
            current_framehrr = deaths[j].death_animation[int(frame_death[j])]
            screen.blit(current_framehrr, (heb[j][0] - deaths[j].offset_x, heb[j][1] - deaths[j].offset_y))
        ### enemy death animation ###
            


        ### all objcts animation ###
        Enemy.all.sort(key=lambda ch: ch.y)
        for ch in Enemy.all :
            if ch in Hero.heros:
                ch.animator(screen)
            elif ch in Barracks.barracks:
                ch.animator(screen, barracks_image)
            else :
                ch.animator()
        ### all objcts animation ###
                

        ### towers and bullets main logic ###
        for enemy in Enemy.enemies_to_remove :
            if enemy in Enemy.enemies :
                Enemy.enemies.remove(enemy)
                a = enemy.x
                b = enemy.y
                heb.append([a, b])
                frame_death.append(0)
                deaths.append(enemy)
            if enemy in Enemy.all :
                Enemy.all.remove(enemy)
        Enemy.enemies_to_remove = []
        for hero in Hero.heros_to_remove :
            if hero in Hero.heros :
                Hero.heros.remove(hero)
            if hero in Enemy.all :
                Enemy.all.remove(hero)
        Hero.heros_to_remove = []
        for cannon in Cannon.cannons :
            cannon.create_bullet()
        for bullet in Bullet.bullets :
            bullet.bullet_move()
            bullet.bullet_draw()
        for bullet in Bullet.bullets_to_remove :
            Bullet.bullets.remove(bullet)
        Bullet.bullets_to_remove = []
        ### towers and bullets main logic ###


        ### effects animation ###
        exp_removal = []
        for i in range(len(frame_b)) :
            frame_b[i] += 15 * Enemy.delta
            if frame_b[i] >= 6 :
                exp_removal.append(i)
        exp_removal.reverse()
        for index in exp_removal:
            frame_b.pop(index)
            lightb.pop(index)
        for i in range(len(frame_b)):
            current_lightrp = exp_effects[int(frame_b[i])]
            screen.blit(current_lightrp, (lightb[i][0] - 70, lightb[i][1]- 70) )
        exp2_removal = []
        for i in range(len(frame_b2)) :
            frame_b2[i] += 15 * Enemy.delta
            if frame_b2[i] >= 11 :
                exp2_removal.append(i)
        exp2_removal.reverse()
        for index in exp2_removal:
            frame_b2.pop(index)
            lightb2.pop(index)
        for i in range(len(frame_b2)):
            current_lightrp2 = lightning_effecth[int(frame_b2[i])]
            screen.blit(current_lightrp2, (lightb2[i][0] - 100, lightb2[i][1]- 200) )

        poison_removal = []

        for i in range(len(frame_p)) :
            frame_p[i] += 15 * Enemy.delta
            if frame_p[i] >= 23 :
                poison_removal.append(i)

        poison_removal.reverse()
        for index in poison_removal:
            frame_p.pop(index)
            lightp.pop(index)
        for i in range(len(frame_p)):
            current_lightrp = poison_effect[int(frame_p[i])]
            screen.blit(current_lightrp, (lightp[i][0] - 75, lightp[i][1]- 75) )
        for enemy in Enemy.enemies :
            if enemy.fire_duration != 0 and enemy.firee == True :
                current_lightrp = flag[int(frame_fire)]
                screen.blit(current_lightrp, (enemy.x - 50, enemy.y - 37.5) )
        poisoni_removal = []
        for i in range(len(frame_pi)) :
            frame_pi[i] += 15 * Enemy.delta
            if frame_pi[i] >= 9 :
                poisoni_removal.append(i)
        poisoni_removal.reverse()
        for index in poisoni_removal:
            frame_pi.pop(index)
            lightpi.pop(index)
        for i in range(len(frame_pi)):
            current_lightrpi = lightning_effect[int(frame_pi[i])]
            screen.blit(current_lightrpi, (lightpi[i][0] - 200, lightpi[i][1]- 270) )

        poisonib_removal = []
        for i in range(len(frame_pib)) :
            frame_pib[i] += 15 * Enemy.delta
            if frame_pib[i] >= 11 :
                poisonib_removal.append(i)
        poisonib_removal.reverse()
        for index in poisonib_removal:
            frame_pib.pop(index)
            lightpib.pop(index)
        for i in range(len(frame_pib)):
            current_lightrpib = blood7[int(frame_pib[i])]
            screen.blit(current_lightrpib, (lightpib[i][0] - 480 / 9, lightpib[i][1]- 270 / 9) )


        poisonii_removal = []

        for i in range(len(frame_pii)) :
            frame_pii[i] += 15 * Enemy.delta
            if frame_pii[i] >= 6 :
                poisonii_removal.append(i)

        poisonii_removal.reverse()

        for index in poisonii_removal:
            frame_pii.pop(index)
            lightpii.pop(index)

        for i in range(len(frame_pii)):

            current_lightrpii = r_effect[int(frame_pii[i])]
            screen.blit(current_lightrpii, (lightpii[i][0] - 100, lightpii[i][1]- 100) )
        exp2g_removal = []
        for i in range(len(frame_b2g)) :
            frame_b2g[i] += 15 * Enemy.delta
            if frame_b2g[i] >= 4 :
                exp2g_removal.append(i)
        exp2g_removal.reverse()
        for index in exp2g_removal:
            frame_b2g.pop(index)
            lightb2g.pop(index)
        for i in range(len(frame_b2g)):
            current_lightrp2g = bang_frames[int(frame_b2g[i])]
            screen.blit(current_lightrp2g, (lightb2g[i][0] - image_sizelegg[0] / 6, lightb2g[i][1]- image_sizelegg[1] / 6) )
        tor_removal = []
        for i in range(len(frame_tor)) :
            frame_tor[i] += 13 * Enemy.delta
            if frame_tor[i] >= 32 :
                tor_removal.append(i)
        tor_removal.reverse()
        for index in tor_removal:
            frame_tor.pop(index)
            lighttor.pop(index)
        for i in range(len(frame_tor)):
            current_lightrpt = animation_tornado[int(frame_tor[i])]
            screen.blit(current_lightrpt, (lighttor[i][0] - 595 / 4, lighttor[i][1]- 418 / 4 - 50) )
        ### effects animation ###
        
        

        for barrack in Barracks.barracks :
            barrack.hero_creator()
            if barrack.level_up == True :
                screen.blit(bb, (barrack.x - 25, barrack.y - 25 - 50))
                barrack.area = pygame.Rect(barrack.x - 25, barrack.y - 50 - 25, 50, 50)
        for enemy in Enemy.enemies :
            framer += 20 * Enemy.delta
            if framer >= 15 :
                framer = 0
            if enemy.inf == True :
                screen.blit(flag[int(framer)], (enemy.x - 100 / 2, enemy.y - 75 / 2))





        manager.update(dt)
        manager.draw_ui(screen)
        if pressed:
            cursor_img_rectd.center = pygame.mouse.get_pos()
            cursor_img_rectd.centerx = pygame.mouse.get_pos()[0]
            cursor_img_rectd.centery = pygame.mouse.get_pos()[1] + 20
            screen.blit(cursor_imagedp, cursor_img_rectd)
        else:
            cursor_img_rectd.center = pygame.mouse.get_pos()
            cursor_img_rectd.centerx = pygame.mouse.get_pos()[0]
            cursor_img_rectd.centery = pygame.mouse.get_pos()[1] + 20
            screen.blit(cursor_imaged, cursor_img_rectd)
            ### effects and game logic ###
        
        pygame.display.flip()
    pygame.quit()