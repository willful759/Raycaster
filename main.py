import game_map,player,sys,render
import numpy as np
import pygame as pyg
import time as t
from collections import namedtuple
from minimap import Minimap
from primitives import *

pyg.init()
internal_resolution = Resolution(256, 150)
screen_w,screen_h = resolution = Resolution(1024, 600)

pyg.display.set_caption("Raycast Engine v0.01")
screen = pyg.display.set_mode(resolution)

#velocity
v = 0.1
m = game_map.Map('map.txt')

p = player.Player(8, 4, v, 0, (np.pi/2))

mini = Minimap(screen, m, resolution.scale(0.35), Point(0,0))
while True:
     
    startTime = t.perf_counter()
    #key detect stuff#
    for event in pyg.event.get():
        if event.type == pyg.QUIT: 
            sys.exit()

    #key detect#
    pressed = pyg.key.get_pressed()
    prevpos = p.x,p.y
    p.handle_keys(pressed)

    #check collition in a ghetto way#
    try:
        if (n:=m.map_array[int(p.y)][int(p.x)]) != 0:
            p.updatePosition(*prevpos)
    except IndexError:
        p.updatePosition(prevpos[0],prevpos[1])
        
    #draw bg#
    screen.fill((0,0,0))
    pyg.draw.rect(screen,(63,63,63),(0,int(screen_h/2),screen_w,int(screen_h/2)),0)
            
    coords = render.render(screen,p,resolution,internal_resolution,m.map())
    mini.draw()

    pyg.display.flip()

    t.sleep(max(0,1/60 - t.perf_counter() + startTime))
