import pygame
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIRECTORY = os.path.join(BASE_DIR, "assets", "assets1")
pygame.display.init()
WIDTH, HEIGHT = 1600, 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
def importer(frames, a=120, b=120, aa=1, bb=17, aaa=True) :
    lst = []
    for i in range(aa, bb):
        filename1 = frames.format(i)
        frame1 = pygame.image.load(filename1).convert_alpha()
        frame1 = pygame.transform.smoothscale(frame1, (a, b))
        frame1 = pygame.transform.flip(frame1, aaa, False)
        lst.append(frame1)
    return lst

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

