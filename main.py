"""
    Main Module
    Author: Aidin Lehrman

    https://tylerxhobbs.com/essays/2020/flow-fields
    https://github.com/pvigier/perlin-numpy
"""

from math import cos, floor, sin
import math
import numpy as np
import matplotlib.pyplot as plt # pylint: disable=import-error
from perlin_numpy import generate_perlin_noise_2d # pylint: disable=import-error
from Vector2 import Ray2, Vector2 # pylint: disable=unused-import

def render_rays(image_height: int, image_width: int, cells_tall: int, cells_wide: int, \
                ray_list: list[list[Ray2]], curve_length: float = 10, save_to_file: str='image.png') -> None:
    """ Renderes scene
    """
    # Initializes Image
    image = np.ones((image_height, image_width, 3))

    # Works Reguardless of grid or no grid (can be used on random values too)
    
            
                # This draws lines, need to make it draw curves
                if 0 <= x < image_width and 0 <= y < image_height:
                    image[floor(pixel.y)][floor(pixel.x)] = np.clip([0], 0, 1)

    plt.imsave(save_to_file, image)  # Saves image

def generate_rays(step_length: int, noise_scale: float, image_height: int, image_width: int) \
    -> list[list[Ray2]]:
    """ Generates Rays
    """
    cells_tall: int = floor(image_height / step_length)
    cells_wide: int = floor(image_width / step_length)

    # Generate noise with dimensions matching the grid
    np.random.seed(0)
    noise = generate_perlin_noise_2d((image_height, image_width), (8, 8))

    grid: list[list[Ray2]] = [[Ray2(Vector2(0, 0), Vector2(0, 0)) for _ in range(cells_wide + 1)] \
        for _ in range(cells_tall + 1)]

    for j in range(cells_tall + 1):  # For each row
        for i in range(cells_wide + 1):  # For each column
            point: Vector2 = Vector2(step_length * i, step_length * j)
            rand_angle: float = noise[floor(point.y * noise_scale)][floor(point.x * noise_scale)] \
                * 2 * math.pi # Radians
            rand_x: float = sin(rand_angle)
            rand_y: float = cos(rand_angle)
            rand_ray: Ray2 = Ray2(point, Vector2(rand_x, rand_y))
            grid[j][i] = rand_ray

    return grid

def main() -> None:
    """ Main
    """
    image_height: int = 1000
    image_width: int = 1000
    rays: list[list[Ray2]] = generate_rays(15, 0.1, image_height, image_width)
    render_rays(image_height, image_width, rays, 200, 'image.png')

if __name__ == '__main__':
    main()
