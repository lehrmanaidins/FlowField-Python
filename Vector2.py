"""
    Vector2 Module
    Author: Aidin Lehrman
"""

import math


class Vector2:
    """ 2 Dimentional Vector
    """
    x: float
    y: float
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'[{self.x}, {self.y}]'

    def length(self) -> float:
        """ Return length of Vector2
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

class Point2(Vector2):
    """ 2 Dimentional Point
    """
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


class Ray2:
    """ 2 Dimentional Ray
    """
    origin: Point2
    direction: Vector2
    def __init__(self, origin: Point2, direction:Vector2) -> None:
        self.origin = origin
        self.direction = direction

    def __str__(self) -> str:
        return f'{{{self.origin} -> {self.direction}}}'
