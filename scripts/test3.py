import pygame
import pygame_gui


def window_managment(pos_x, pos_y, manager):
    window2 = pygame_gui.elements.UIWindow(
        rect=pygame.Rect((pos_x - 150, pos_y -250), (300, 400)),
        manager=manager,
        draggable=False,
        window_display_title='SHOP'
    )

    button1 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150 - 100, 50), (200, 50)),
        text='ARCHER TOWER',
        manager=manager,
        container=window2,
    )

    button2 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150- 100, 100), (200, 50)),
        text='WIZARD TOWER',
        manager=manager,
        container=window2
    )
    button3 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150- 100, 150), (200, 50)),
        text='MORTAR',
        manager=manager,
        container=window2
    )
    button4 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150- 100, 200), (200, 50)),
        text='INFERNO TOWER',
        manager=manager,
        container=window2
    )
    button5 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150- 100, 250), (200, 50)),
        text='SMASHER',
        manager=manager,
        container=window2
    )
    button6 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150- 100, 300), (200, 50)),
        text='FELECTRO TOWER',
        manager=manager,
        container=window2
    )
    return button1, button2, button3, button4,button5, button6, window2

def window_managment_update(pos_x, pos_y, manager, txt):
    windowU = pygame_gui.elements.UIWindow(
        rect=pygame.Rect((pos_x - 150, pos_y -250), (300, 300)),
        manager=manager,
        draggable=False,
        window_display_title='UPGRADE',
    )

    buttonU = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150 - 100, 50), (200, 50)),
        text=txt,
        manager=manager,
        container=windowU,
    )

    return buttonU, windowU