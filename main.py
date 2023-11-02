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
from perlin_numpy import generate_perlin_noise_2d
from torch import pixel_shuffle # pylint: disable=import-error
from Vector2 import Ray2, Vector2 # pylint: disable=unused-import

def render_rays(image_height: int, image_width: int, grid_size: int, \
                step_length: float, curve_steps: int = 10, \
                save_to_file: str='image.png') -> None:
    """ Renderes scene
    """
    # Initializes Image
    image = np.ones((image_height, image_width, 3))

    # Noise
    np.random.seed(0)
    noise_x = generate_perlin_noise_2d((image_height, image_width), (8, 8))
    np.random.seed(1)
    noise_y = generate_perlin_noise_2d((image_height, image_width), (8, 8))

    # Works Reguardless of grid or no grid (can be used on random values too)
    for j in range(0, image_height, grid_size):
        for i in range(0, image_width, grid_size):
            pixel: Vector2 = Vector2(i, j)
            for _ in range(1, curve_steps):
                try:
                    image[floor(pixel.y)][floor(pixel.x)] = np.clip([0], 0, 1)

                    direction: Vector2 = Vector2(noise_x[pixel.y][pixel.y], noise_y[pixel.y][pixel.x])
                    step_ray: Ray2 = Ray2(pixel, direction)

                    pixel = step_ray.point_at(step_length)
                except:
                    continue

    plt.imsave(save_to_file, image)  # Saves image

def main() -> None:
    """ Main
    """
    image_height: int = 96
    image_width: int = 96
    render_rays(image_height, image_width, 10, 1, 100, 'image.png')

if __name__ == '__main__':
    main()
