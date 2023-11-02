"""
    Main Module
    Author: Aidin Lehrman

    https://tylerxhobbs.com/essays/2020/flow-fields
"""

from math import cos, floor, sin
import random
import numpy as np
import matplotlib.pyplot as plt
from colors import red, green, blue, yellow # pylint: disable=unused-import
from Vector2 import Ray2, Vector2 # pylint: disable=unused-import

def render(resolution: int, image_height: int, image_width: int, \
    vector_length: float = 100, save_to_file: str='image.png') -> None:
    """ Renders scene
    """

    # Initializes Image
    image = np.zeros((image_height, image_width, 3))

    cells_tall: int = floor(image_height / resolution)
    cells_wide: int = floor(image_width / resolution)

    grid: list[list[Ray2]] = [[Ray2(Vector2(0, 0), Vector2(0, 0)) for _ in range(cells_wide)] \
        for _ in range(cells_tall)]
    for j in range(cells_tall):  # For each row
        for i in range(cells_wide):  # For each column
            rand_angle: float = random.random() * 360
            point: Vector2 = Vector2((resolution / 2) + (resolution * i), \
                (resolution / 2) + (resolution * j))
            rand_x: float = vector_length * sin(rand_angle)
            rand_y: float = vector_length * cos(rand_angle)
            rand_ray: Ray2 = Ray2(point, Vector2(rand_x, rand_y))
            grid[j][i] = rand_ray

    # Works Reguardless of grid or no grid (can be used on random values too)
    for row in grid:
        for cell in row:
            step_length: int = 1
            for length in range(0, floor(vector_length), step_length):
                pixel: Vector2 = cell.point_at(length)
                # Manually set the pixel to a color
                x, y = int(pixel.x), int(pixel.y)
                if 0 <= x < image_width and 0 <= y < image_height:
                    image[floor(pixel.y)][floor(pixel.x)] = np.clip([1], 0, 1)

    plt.imsave(save_to_file, image)  # Saves image

def main() -> None:
    """ Main
    """
    render(20, 1000, 1000, 30)

if __name__ == '__main__':
    main()
