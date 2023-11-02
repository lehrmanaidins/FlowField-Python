"""
    Vector2 Module
    Author: Aidin Lehrman
"""

from __future__ import annotations
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

    def __add__(self, value: Vector2) -> Vector2:
        x: float = self.x + value.x
        y: float = self.y + value.y
        return Vector2(x, y)

    def __mul__(self, scalar) -> Vector2:
        x: float = self.x * scalar
        y: float = self.y * scalar
        return Vector2(x, y)

    def __truediv__(self, scalar) -> Vector2:
        x: float = self.x / scalar
        y: float = self.y / scalar
        return Vector2(x, y)

    def length(self) -> float:
        """ Return length of Vector2
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def unit_vector(self) -> Vector2:
        """ Returns same direction w/ magnitude of 1
        """
        return self / self.length()

class Ray2:
    """ 2 Dimentional Ray
    """
    origin: Vector2
    direction: Vector2
    def __init__(self, origin: Vector2, direction:Vector2) -> None:
        self.origin = origin
        self.direction = direction

    def __str__(self) -> str:
        return f'{{{self.origin} -> {self.direction}}}'

    def point_at(self, t: float) -> Vector2:
        """ Returns point at distance 't'
        """
        return self.origin + (self.direction.unit_vector() * t)
