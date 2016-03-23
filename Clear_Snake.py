#-*-coding: utf-8-*-

import pygame, random

class Blocks():
    def __init__(self, block_w=10, block_h=10):
        self.block_w = block_w
        self.block_h = block_h
        self.set_pos()
    def set_pos(self):
        self.block_x = random.randint(0,800)
        self.block_y = random.randint(0,600)

class Main():
    def __init__(self, x_pos=400, y_pos=270):
        self.x_pos, self.y_pos = x_pos, y_pos
        self.x_change = self.y_change = 0
        self.clock = pygame.time.Clock()
        self.main_loop()
    def main_loop(self, gameExit=False):
        """ ### MAIN LOOP ### """
        pygame.init()
        display = pygame.display.set_mode((800,600))
        displayColour = (245, 245, 220)
        pygame.display.set_caption('Fresh Seva')
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                """ SAVING FROM AN ERROR + MAIN ENGINE'S HERE """
                try:
                    if event.type == pygame.KEYDOWN:
                        try:
                            x_keys = {276: -1,
                                        275: 1}
                            self.x_change = x_keys[event.key]
                            self.y_change = 0
                        except:
                            y_keys = {274: 1,
                                        273: -1}
                            self.y_change = y_keys[event.key]
                            self.x_change = 0
                except:
                    print("An Error Occurs!")
                    gameExit = True

            self.x_pos += self.x_change if self.x_change <= 0 else 1
            self.y_pos += self.y_change if self.y_change <= 0 else 1
            display.fill(displayColour)
            pygame.draw.rect(display, (0,0,0), [self.x_pos, self.y_pos, 15, 15])
            pygame.display.update()

            self.clock.tick(100)


block = Blocks()
main = Main()
