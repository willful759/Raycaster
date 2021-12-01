import pygame as pyg
import numpy as np
import player
from pygame import gfxdraw
from raycast import raycast

view_distance = 20

def render(screen, object_, resolution, internal_resolution, map_,fov=90):
    line_width = np.ceil(resolution.w/internal_resolution.w)
    line_height = resolution.h/internal_resolution.h

    for cx in range(internal_resolution.w):
        distance,side = raycast(object_.x, object_.y, object_.angle, cx, internal_resolution.w, map_)
        
        if distance is None:
            continue

        lineheight = internal_resolution.h/distance
        celling = max(0,int(internal_resolution.h/2 - lineheight/2))

        gradient = 255 - 255*(distance/view_distance)
        if gradient > 255: 
            gradient = 255 
        elif gradient < 0:
            gradient = 0

        rect = (cx*line_width, celling*line_height, line_width, resolution.h - line_height*2*celling)
        gfxdraw.box(screen, rect, (max(0,gradient - side*50), 0, max(0,gradient - side*50)))
