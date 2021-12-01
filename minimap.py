import pygame
from dataclasses import dataclass
from game_map import Map
from event import subscribe
import numpy as np

class Minimap:
    def __init__(self, screen, map_, size, position):
        self.screen = screen
        self.map_ = map_
        self.size = size
        self.position = position
        self.square_width = int(np.ceil(size.w/map_.w))
        self.square_height = int(np.ceil(size.h/map_.h))
        self.surface = pygame.Surface((map_.w*self.square_width,map_.h*self.square_height))

        subscribe("ray_hit",self.draw_ray)

    def draw(self):
        clear_rect = (*self.position, *self.size)
        pygame.draw.rect(self.screen, (0,0,0), clear_rect)

        for y,line in enumerate(self.map_.map()):
            for x,c in enumerate(line):
                if c != 0:
                    rect = (x*self.square_width,
                            y*self.square_height,
                            self.square_width,
                            self.square_height)
                    pygame.draw.rect(self.surface, (255,255,255), rect)

        self.screen.blit(self.surface, (*self.position, *self.size))
        self.surface.fill((0,0,0))

    def draw_ray(self, origin, end):
        local_origin = (
                origin.x*self.square_width,
                origin.y*self.square_height
                )
        local_end = (
                end.x*self.square_width,
                end.y*self.square_height
                )
        pygame.draw.line(self.surface, (0,255,0), local_origin, local_end)
