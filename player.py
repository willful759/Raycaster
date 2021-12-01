import numpy as np
import render
import pygame

class Player:
    def __init__(self, x, y, v, angle, fov):
        self.x = x
        self.y = y
        self.v = v
        self.angle = angle
        self.fov = fov
        self.unit_vx = np.cos(angle)
        self.unit_vy = np.sin(angle)

    def updateAngle(self,angle):
        self.angle = angle
        self.unit_vx = np.cos(angle)
        self.unit_vy = np.sin(angle)

    def updatePosition(self,x,y):
        self.x = x
        self.y = y

    def handle_keys(self,pressed):
        if pressed[pygame.K_LEFT]: 
            self.updateAngle(self.angle - 0.05)

        if pressed[pygame.K_RIGHT]:
            self.updateAngle(self.angle + 0.05)

        if pressed[pygame.K_w]:
            newx = self.unit_vx*self.v              
            newy = self.unit_vy*self.v
            self.updatePosition(self.x + newx,self.y + newy)

        if pressed[pygame.K_s]:
            newx = self.unit_vx*self.v
            newy = self.unit_vy*self.v
            self.updatePosition(self.x - newx,self.y - newy)

        if pressed[pygame.K_d]:
            newx = self.unit_vy*self.v
            newy = self.unit_vx*self.v
            self.updatePosition(self.x - newx,self.y + newy)

        if pressed[pygame.K_a]:
            newx = self.unit_vy*self.v
            newy = self.unit_vx*self.v
            self.updatePosition(self.x + newx,self.y - newy)
