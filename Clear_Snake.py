#-*-coding: utf-8-*-

import pygame, random

class Blocks():
    def __init__(self, block_w=10, block_h=10):
        self.block_w = block_w
        self.block_h = block_h
        
        print self.block_x, self.block_y
        
    def set_position(self):                     # redraw method
        self.block_x = random.randint(0,800)    #
        self.block_y = random.randint(0,600)    #

block = Blocks(15,15)
