#-*-coding: utf-8-*-

import pygame, random
from pygame import *

block = None

class Data:
    def __init__(self, last_x = -20, last_y = -20):
        self.x = last_x
        self.y = last_y


class Blocks:
    def __init__(self, block_w=15, block_h=15):
        self.block_w = block_w
        self.block_h = block_h
        self.set_pos()
    def set_pos(self):
        self.block_x = random.randint(0,30) * 15
        self.block_y = random.randint(0,20) * 15


class Main:
    def __init__(self, snake_len=0, blocks_plus=0, x_pos=450, y_pos=300):
        self.x_pos, self.y_pos = x_pos, y_pos
        self.x_change = self.y_change = 0
        self.clock = pygame.time.Clock()
        self.snake_len = snake_len
        self.main_loop()
    def main_loop(self, gameExit=False):
        positions = []
        snake_blocks = []
        self.gameExit = gameExit
        """ ### MAIN LOOP ### """
        pygame.init()
        self.display = pygame.display.set_mode((750,600))
        displayColour = (245, 230, 150)
        pygame.display.set_caption('Fresh Seva')
        while not self.gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True
                """ SAVING FROM AN ERROR + MAIN ENGINE'S HERE """
                try:
                    if event.type == pygame.KEYDOWN:
                        try:
                            x_keys = {276: -15,
                                        275: 15}
                            self.x_change = x_keys[event.key]
                            self.y_change = 0
                        except:
                            y_keys = {274: 15,
                                        273: -15}
                            self.y_change = y_keys[event.key]
                            self.x_change = 0
                except:
                    print("An Error Occurs!")
                    self.gameExit = True

                """ DATA PROCESSING """
            self.x_pos += self.x_change if abs(self.x_change) <= 15 else 15
            self.y_pos += self.y_change if abs(self.y_change) <= 15 else 15
            if self.x_pos <= -15 or abs(self.x_pos) >= 765:
                self.lose()
            if self.y_pos <= -15 or abs(self.y_pos) >= 615:
                self.lose()
            self.display.fill(displayColour)
            """ CHECKING BLOCK'S STATUS """
            check = (((self.x_pos >= bl.block_x and self.x_pos <= bl.block_x+bl.block_w)
            and (self.x_pos+15 >= bl.block_x and self.x_pos+15 <= bl.block_x+bl.block_w))
            and (self.y_pos >= bl.block_y and self.y_pos <= bl.block_y+bl.block_w)
            and (self.y_pos+15 >= bl.block_y and self.y_pos+15 <= bl.block_y+bl.block_w))

            """ MAIN CHECKING BEGINS HERE """
            if check:
                del(self.bl_drown)
                bl.set_pos()
                self.snake_len += 1
                positions = positions[(-2 - self.snake_len):]
                self.block_print()
            else:
                self.block_print()

            pygame.draw.rect(self.display, (0,0,0), [self.x_pos, self.y_pos, 15, 15])

            """ SNAKE'S LENGTH ADDING """
            if self.snake_len:
                for X in range(self.snake_len):
                    globals()['storage%i' % X] = Data()
                    snake_blocks.append(globals()['storage%i' % X])
                    snake_blocks = snake_blocks[-self.snake_len:]

            positions.append([self.x_pos,self.y_pos])

            if snake_blocks:
                for i in range(len(snake_blocks)):
                    a = positions[(-2 - i)][0]
                    b = positions[(-2 - i)][1]
                    pygame.draw.rect(self.display, (0, 0, 0), [a, b, 15, 15])
                    if self.x_pos == a:
                        if self.y_pos == b:
                            self.lose()

            """ THE LAST PART OF THE MAIN LOOP """
            pygame.display.update()

            self.clock.tick(15)
    """ OTHER FUNCTIONS """
    def lose(self):
        print("YOU LOSE!")
        self.gameExit = True

    def block_print(self):
        self.bl_drown = pygame.draw.rect(self.display, (0,244,15), [bl.block_x, bl.block_y, bl.block_w, bl.block_h])


bl = Blocks()
main = Main()

""" ### CLEAR_SNAKE BUILD 1.7 ### """
