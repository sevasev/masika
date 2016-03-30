# -*-coding: utf-8-*-

import pygame
from pygame import *
import random
import time
import os

block = None

class Data:
    def __init__(self, last_x=-20, last_y=-20):
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
    def __init__(self,scores=0, snake_len=0, x_pos=375, y_pos=300):
        self.scores = scores
        self.x_pos, self.y_pos = x_pos, y_pos
        self.x_change = self.y_change = 0
        self.clock = pygame.time.Clock()
        self.snake_len = snake_len
        self.main_loop()
    def main_loop(self, gameExit=False):
        positions = []
        self.snake_blocks = []
        self.gameExit = gameExit
        """ ### MAIN LOOP ### """
        pygame.init()
        self.display = pygame.display.set_mode((750,600))
        self.displayColour = (245, 230, 150)
        pygame.display.set_caption('Clear Snake')
        while not self.gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True
                """ SAVING FROM AN ERROR + MAIN ENGINE'S HERE """
                x_keys = {276: -15, 275: 15}
                y_keys = {274: 15, 273: -15}
                if event.type == pygame.KEYDOWN:
                    if self.x_change == self.y_change:
                        try:
                            self.x_change = x_keys[event.key]
                            self.y_change = 0
                        except:
                            self.y_change = y_keys[event.key]
                            self.x_change = 0
                try:
                    if event.type == pygame.KEYDOWN:
                        if self.x_change == 0:
                            self.x_change = x_keys[event.key]
                            self.y_change = 0
                        if self.y_change == 0:
                            self.y_change = y_keys[event.key]
                            self.x_change = 0
                except:
                    pass

            """ DATA PROCESSING """
            self.x_pos += self.x_change if abs(self.x_change) <= 15 else 15
            self.y_pos += self.y_change if abs(self.y_change) <= 15 else 15

            if self.x_pos <= -5: self.x_pos = 750
            elif self.x_pos >= 750: self.x_pos = 0

            if self.y_pos <= -5: self.y_pos = 600
            elif self.y_pos >= 600: self.y_pos = 0

            self.display.fill(self.displayColour)

            """ CHECKING BLOCK'S STATUS """
            check = (((self.x_pos >= bl.block_x and self.x_pos <= bl.block_x+bl.block_w)
            and (self.x_pos+15 >= bl.block_x and self.x_pos+15 <= bl.block_x+bl.block_w))
            and ((self.y_pos >= bl.block_y and self.y_pos <= bl.block_y+bl.block_w)
            and (self.y_pos+15 >= bl.block_y and self.y_pos+15 <= bl.block_y+bl.block_w)))

            """ MAIN CHECKING BEGINS HERE """
            if check:
                del(self.bl_drown)
                bl.set_pos()
                self.snake_len += 1
                self.scores += 1
                positions = positions[(-2 - self.snake_len):]
                self.block_print()
            else:
                self.block_print()

            self.snake = pygame.draw.rect(self.display, (0,0,0), [self.x_pos, self.y_pos, 15, 15])

            """ SNAKE'S LENGTH ADDING """
            if self.snake_len:
                for X in range(self.snake_len):
                    globals()['storage%i' % X] = Data()
                    self.snake_blocks.append(globals()['storage%i' % X])
                    self.snake_blocks = self.snake_blocks[-self.snake_len:]

            positions.append([self.x_pos,self.y_pos])

            if self.snake_blocks:
                for i in range(len(self.snake_blocks)):
                    a = positions[(-2 - i)][0]
                    b = positions[(-2 - i)][1]
                    self.blocks = pygame.draw.rect(self.display, (245,0,25), [a, b, 15, 15])
                    if self.x_pos == a:
                        if self.y_pos == b:
                            self.lose()

            """ THE LAST PART OF THE MAIN LOOP """
            pygame.display.update()

            self.clock.tick(15)

    """ OTHER FUNCTIONS """
    def lose(self):
        self.new_file()
        self.file.write(str(self.scores) + '\n')
        self.file.close()
        self.best_score()
        self.display.fill(self.displayColour)
        self.text_to_screen("GAME OVER", (255,0,0))
        pygame.display.update()
        time.sleep(3)
        bl.block_x = bl.block_y = 99999
        self.gameExit = True

    def block_print(self):
        self.bl_drown = pygame.draw.rect(self.display, (245,0,25), [bl.block_x, bl.block_y, bl.block_w, bl.block_h])

    def text_to_screen(self, msg, colour):
        fontB = pygame.font.SysFont(None, 100)
        fontS = pygame.font.SysFont(None, 60)
        you_lose = fontB.render(msg, True, colour)
        q_score = fontS.render("You scored: " + str(self.scores), True, colour)
        best_score = fontS.render("Best score: " + str(self.best_res), True, colour)
        self.display.blit(you_lose, [170, 230])
        self.display.blit(q_score, [230, 310])
        self.display.blit(best_score, [234, 350])

    def best_score(self):
        res = []
        file = open('Scores.txt', 'r')
        resList = file.readlines()
        for i in resList:
            res.append(int(i))
        self.best_res = max(res) if max(res) >= self.scores else self.scores
        file.close()

    def new_file(self):
        q_path = os.getcwd()
        os.chdir(q_path)
        self.file = open('Scores.txt', 'a')


bl = Blocks()
main = Main()
pygame.quit()

""" ### CLEAR_SNAKE BUILD ALPHA 3.0 ### """

"""
WHAT TO DO:
        1. Experiment with Snake's colour --DONE
        2. Try to delete the snake's parts and a block at the end --!!!
        3. Do the impossibility of the 'back' movement --DONE ~so-so
        4. To move through walls --DONE
"""
