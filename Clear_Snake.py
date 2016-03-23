#-*-coding: utf-8-*-

import pygame, random

class Blocks():
    def __init__(self, block_w=10, block_h=10):
        self.block_w = block_w
        self.block_h = block_h
<<<<<<< HEAD
        self.block_x = random.randint(0,800)
        self.block_y = random.randint(0,600)

class Main():
    def __init__(self, x_pos=400, y_pos=270):
        self.x_pos = x_pos
        self.y_pos = y_pos
        x_change = y_change = 0
        """ ### MAIN LOOP ### """
        pygame.init()
        display = pygame.display.set_mode((800,600))
        displayColour = (30, 144, 255)
        pygame.display.set_caption('Fresh Seva')
        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    x_keys = {pygame.K_LEFT: x_change - 10,
                            pygame.K_RIGHT: x_change + 10}
                    y_keys = {pygame.K_DOWN: y_change - 10,
                            pygame.K_UP: y_change + 10}

                x_pos += x_change
                y_pos += y_change
                pygame.draw.rect(display, (0,0,0), [x_pos, y_pos, 20, 20])
                display.fill(displayColour)

                if event.type == pygame.QUIT:
                        gameExit = True





block = Blocks()
main = Main()
=======
        
        print self.block_x, self.block_y
        
    def set_position(self):                     # redraw method
        self.block_x = random.randint(0,800)    #
        self.block_y = random.randint(0,600)    #

block = Blocks(15,15)
>>>>>>> 3032b5c8566d96faf0dbfa16da0e13900e7f52b1
