import numpy as np
import pygame
from event import broadcast
from primitives import *

def raycast(x, y, angle, cx, width, map_):
    if angle == 0:
        angle = 0.00001

    dir_x = np.cos(angle)
    dir_y = np.sin(angle)

    plane_x = -dir_y
    plane_y = dir_x

    camera_x = 2*(cx/width) -1

    ray_dir_x = dir_x + plane_x*camera_x
    ray_dir_y = dir_y + plane_y*camera_x

    map_x = int(x)
    map_y = int(y)
    
    dx = abs(1/ray_dir_x)
    dy = abs(1/ray_dir_y)

    hit = False
    side = 0

    if ray_dir_x < 0:
        step_x = - 1
        x_intercept = (x - map_x)*dx
    else:
        step_x = 1
        x_intercept = (map_x + 1 - x)*dx

    if ray_dir_y < 0:
        step_y = -1
        y_intercept = (y - map_y)*dy
    else:
        step_y = 1
        y_intercept = (map_y + 1 - y)*dy
        
    try:
        while not hit:
            if x_intercept < y_intercept:
                x_intercept += dx
                map_x += step_x
                side = 0
            else:
                y_intercept += dy
                map_y += step_y
                side = 1

            if map_[map_y][map_x] != 0:
                hit = True
                broadcast("ray_hit", Point(x, y), Point(map_x, map_y))

    except IndexError:
        return None,None
                
    if side == 0:
        distance = x_intercept - dx
    else:
        distance = y_intercept - dy
        
    if distance == 0:
        distance = 0.0001

    return distance,side
