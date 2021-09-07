import pygame
import sys
import random
import math

from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH,HEIGHT])
        pygame.display.set_caption(TITLE)

    def run(self):
        self.playing = True
        while self.playing:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(DARK_GREY)
        pygame.draw.circle(self.screen, SKIN, (WIDTH//2, HEIGHT//2), 155, 0)            
        pygame.draw.circle(self.screen, WHITE, (WIDTH//2.5, HEIGHT//2.5), 32, 0)        
        pygame.draw.circle(self.screen, BLACK, (WIDTH//2.5, HEIGHT//2.5), 33, 2)
        pygame.draw.line(self.screen, BLACK, (WIDTH//2.5, HEIGHT//2.15),(WIDTH//2.5, HEIGHT//1.5), 2)
        pygame.draw.circle(self.screen, BLACK, (WIDTH//2.5, HEIGHT//2.5), 6, 0)
        pygame.draw.circle(self.screen, WHITE, (WIDTH//1.7, HEIGHT//2.5), 32, 0)
        pygame.draw.circle(self.screen, BLACK, (WIDTH//1.7, HEIGHT//2.5), 6, 0)
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(WIDTH//2.5, HEIGHT//20, (WIDTH//1.7-WIDTH//2.5), (HEIGHT//5 - HEIGHT//20)), 0)
        pygame.draw.rect(self.screen, BLACK, pygame.Rect(WIDTH//4, HEIGHT//6, (WIDTH//1.7-WIDTH//10), (HEIGHT//5 - HEIGHT//7)), 0)
        pygame.draw. arc(self.screen, BLACK,
            pygame.Rect(WIDTH//2-70, HEIGHT//2-40, 128,128), math.radians(270), math.radians(330))
        pygame.display.flip()


game = Game()
game.run()