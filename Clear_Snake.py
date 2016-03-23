#-*-coding: utf-8-*-

import pygame, random

class Blocks:
    def __init__(self, block_w=10, block_h=10):
        self.block_w = block_w
        self.block_h = block_h
        self.set_pos()
    def set_pos(self):
        self.block_x = random.randint(0,24) * 20
        self.block_y = random.randint(0,19) * 20


class Main:
    def __init__(self, blocks_plus=0, x_pos=420, y_pos=300):
        self.x_pos, self.y_pos = x_pos, y_pos
        self.x_change = self.y_change = 0
        self.clock = pygame.time.Clock()
        self.blocks_plus = blocks_plus
        self.main_loop()
    def main_loop(self, gameExit=False):
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
                            x_keys = {276: -10,
                                        275: 10}
                            self.x_change = x_keys[event.key]
                            self.y_change = 0
                        except:
                            y_keys = {274: 10,
                                        273: -10}
                            self.y_change = y_keys[event.key]
                            self.x_change = 0
                except:
                    print("An Error Occurs!")
                    self.gameExit = True

                """ DATA PROCESSING """
            self.x_pos += self.x_change if abs(self.x_change) <= 10 else 10
            self.y_pos += self.y_change if abs(self.y_change) <= 10 else 10
            if self.x_pos <= -10 or abs(self.x_pos) >= 760:
                self.lose()
            if self.y_pos <= -10 or abs(self.y_pos) >= 610:
                self.lose()
            self.display.fill(displayColour)
            """ CHEKING BLOCK'S STATUS """
            if self.x_pos == bl.block_x:
                if self.y_pos == bl.block_y:
                    del(self.bl_drown)
                    self.blocks_plus += 1
                    bl.set_pos()
                    self.block_print()
            else:
                self.block_print()

            pygame.draw.rect(self.display, (0,0,0), [self.x_pos, self.y_pos, 10, 10])

            pygame.display.update()

            self.clock.tick(10)

    def lose(self):
        print "YOU LOSE!"
        self.gameExit = True

    def block_print(self):
        self.bl_drown = pygame.draw.rect(self.display, (0,244,15), [bl.block_x, bl.block_y, bl.block_w, bl.block_h])



bl = Blocks()
main = Main()

