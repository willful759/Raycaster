from dataclasses import dataclass
from collections import namedtuple

Point = namedtuple('Point',['x','y'])

class Resolution(namedtuple('Resolution',['w','h'])):
    __slots__ = ()

    def scale(self, factor):
        return Resolution(self.w*factor, self.h*factor)

