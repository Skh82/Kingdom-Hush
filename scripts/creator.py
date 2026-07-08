from enemybrrr import EnemyB
from enemybrrr import EnemyA
from enemybrrr import EnemyD
from enemybrrr import EnemyC
from enemybrrr import EnemyG
from enemybrrr import EnemyN
from enemybrrr import EnemyS
from enemybrrr import EnemyK
from enemybrrr import EnemyL
from enemybrrr import EnemyH
from enemybrrr import Enemy

path_points1 = [(800, 0), (756, 68), (687, 117), (645, 210), (684, 305), (682, 359), (556, 389), (498, 368), (472, 305), (309, 293), (171, 288), (37, 293)]
path_points2 = [(841, 0), (788, 79), (715, 135), (687, 207), (709, 300), (705, 385), (555, 418), (476, 396), (451, 345), (306, 328), (173, 321), (36, 325)]
path_points3 = [(886, 0), (828, 99), (739, 152), (728, 206), (756, 289), (728, 418), (554, 456), (454, 430), (414, 372), (303, 368), (176, 360), (36, 368)]
path_points4 = [(1600, 204), (1403, 220), (1277, 243), (1182, 307), (1088, 399), (1015, 495), (905, 545), (788, 584), (652, 593), (449, 578), (272, 567), (32, 561)]
path_points5 = [(x, y - 30) for x, y in path_points4]
path_points6 = [(x, y + 30) for x, y in path_points4]
path_points7 = [(907, 900), (887, 814), (829, 715), (785, 631), (657, 584), (514, 572), (323, 564), (32, 560)]
path_points8 = [(865, 880), (844, 816), (805, 747), (725, 631), (527, 628), (357, 610), (170, 610), (31, 604)]
path_points9 = [(1555, 675),(1438, 682),(1315, 685),(1201, 662),(1106, 580),(1047, 510),(979, 548),(882, 587),(777, 621),(645, 620),(531, 609),(395, 596),(291, 594),(168, 598),(47, 597)]
path_points10 = [(1559, 657),(1399, 672),(1194, 647),(1094, 548),(980, 578),(837, 641),(675, 653),(551, 641),(354, 573),(221, 619),(113, 582),(51, 611)]

import openpyxl
import time
import threading
workbook = openpyxl.load_workbook('enemy_data.xlsx')
worksheet = workbook.active
print_thread_running = True
data = []
import os
import pygame
screen = pygame.display.set_mode(( 1600, 900 ))
clock = pygame.time.Clock()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIRECTORY = os.path.join(BASE_DIR, "assets", "assets1")
pygame.init()


def importer(sprite_sheet, resize=120) :
    frame_width = sprite_sheet.get_width() // 16
    frame_height = sprite_sheet.get_height() // 6
    animations = []
    for i in range(6):
        animation_frames = []
        for j in range(16):
            frame = sprite_sheet.subsurface((j * frame_width, i * frame_height, frame_width, frame_height))
            pygame.image.save(frame, f'animation_{i}_frame_{j}.jpg')
            frame = pygame.transform.flip(frame, True, False)
            frame = pygame.transform.smoothscale(frame, (resize, resize))
            animation_frames.append(frame)
        animations.append(animation_frames)
    return animations[0], animations[1], animations[2], animations[3], animations[4], animations[5]

sprite_sheetA = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"Character3.png")).convert_alpha()
walkA, slashA, jabA, deathA, frontA, backA = importer(sprite_sheetA)
sprite_sheetB = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"CharacterRR.png")).convert_alpha()
walkB, slashB, jabB, deathB, frontB, backB = importer(sprite_sheetB)
sprite_sheetC = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"Untitled.png")).convert_alpha()
walkC, slashC, jabC, deathC, frontC, backC = importer(sprite_sheetC, resize=150)
sprite_sheetD = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"Untitled2.png")).convert_alpha()
walkD, slashD, jabD, deathD, frontD, backD = importer(sprite_sheetD)
sprite_sheetH = pygame.image.load(os.path.join(DEFAULT_DIRECTORY,"Untitled3.png")).convert_alpha()
walkH, slashH, jabH, deathH, frontH, backH = importer(sprite_sheetH, resize=180)

for row in worksheet.iter_rows(values_only=True):
    data.append(row)  
def create_enemies():
    for line in data:
        time.sleep(line[2])
        a = eval(f'Enemy{line[0]}')
        enemy = a(line[0], line[1], eval(f"path_points{line[3]}"), walk=eval(f'walk{line[0]}'),
        death=eval(f'death{line[0]}'), attack1=eval(f'slash{line[0]}'), attack2=eval(f'jab{line[0]}'),  offset_x=((eval(f'walk{line[0]}'))[0].get_size())[0] / 2,
        offset_y=((eval(f'walk{line[0]}'))[0].get_size())[0] / 2, damage=line[4], front=eval(f'front{line[0]}'), back=eval(f'back{line[0]}'))
        
print_thread = threading.Thread(target=create_enemies)
print_thread.start()
stop_event = threading.Event()
