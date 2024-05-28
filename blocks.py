import pygame
from random import randrange
WIDTH, HEIGHT = 1280, 720

class Blocks:
    """make the blocks that the ball will destroy"""


    def __init__(self):

        self.block_list = [pygame.Rect(25 + 125 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
        self.colour_list = [(randrange(30,256), randrange(30,256), randrange(30,256)) for i in range(10) for j in range(4)]
        self.blocks = []

    def draw_blocks(self, screen):
        self.blocks = [pygame.draw.rect(screen, self.colour_list[colour], block) for colour, block in enumerate(self.block_list)]

    def clear_blocks(self, screen):
        self.blocks.clear()


