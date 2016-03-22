#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, random


class Block():
    block_width = 15
    block_height = 15
    block_color = (0,255,0)
    block_pos_x = random.randint(0, 800)
    block_pos_y = random.randint(0, 600)
""" BLOCKS END HERE """

class Snake:
    def __init__(self):
        pygame.init()

        gameDisplay = pygame.display.set_mode((800,600))
        gameDisplayColour = (30, 144, 255)
        pygame.display.set_caption('Bald Seva')

        gameExit = False

        self.lead_x = 400
        self.lead_y = 270
        lead_x_change = 0
        lead_y_change = 0

        clock = pygame.time.Clock()

        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                try:
                    if event.type == pygame.KEYDOWN:
                        x_val = {pygame.K_LEFT: -1,
                            pygame.K_RIGHT: 1}
                        lead_x_change = x_val[event.key]
                        lead_y_change = 0
                except:
                    y_val = {273: -1,
                                274: 1}
                    lead_y_change = y_val[event.key]
                    lead_x_change = 0

            self.lead_x += lead_x_change
            self.lead_y += lead_y_change
            if abs(self.lead_x) >= 790 or abs(self.lead_x) <= 0:
                lead_x_change = 0
                self.lose()
                break
            if abs(self.lead_y) >= 590 or abs(self.lead_y) <= 0:
                lead_y_change = 0
                self.lose()
                break

            gameDisplay.fill(gameDisplayColour)
            pygame.draw.rect(gameDisplay, (0,255,0), [Block.block_pos_x, Block.block_pos_y, 9, 9])
            pygame.draw.rect(gameDisplay, (0, 0, 0), [self.lead_x, self.lead_y, 15, 15])
            print(self.lead_x, Block.block_pos_x)
            pygame.display.update()

            clock.tick(10)
    """ MAIN LOOP ENDS HERE """

    def diff(self):
        if abs(self.lead_x - Block.block_pos_x) / 100 <= 0.8:
            if abs(self.lead_y - Block.block_pos_y) / 100 <= 0.8:
                print "IT WORKED!!!"


    def lose(self):
        print("Congrats! You lose!")



obj_1 = Snake()
obj_2 = Block()
pygame.quit()
quit()
