"""
    Main Module
    Author: Aidin Lehrman

    https://tylerxhobbs.com/essays/2020/flow-fields
    https://github.com/pvigier/perlin-numpy
"""

import math
import numpy as np
import matplotlib.pyplot as plt # pylint: disable=import-error
from perlin_numpy import generate_perlin_noise_2d

def render_rays(image_height: int, image_width: int, grid_size: int = 10, \
                noise_scale: float = 8, curve_steps: int = 10, \
                save_to_file: str='image.png') -> None:
    """ Renderes scene
    """
    left_x: int = int(image_width * -0.5)
    right_x: int = int(image_width * 1.5)
    top_y: int = int(image_height * -0.5)
    bottom_y: int = int(image_height * 1.5)

    # I think the code starts @ (0, 0) instead of (<0, <0), but it does go past (width, height).
    num_columns: int = math.floor((right_x - left_x) / grid_size)
    num_rows: int = math.floor((bottom_y - top_y) / grid_size)

    # Initializes Image
    image = np.ones((image_width, image_height, 3))

    for layer in range(1):
        # Initializes Noise
        np.random.seed(layer)
        # the actual range is [-sqrt(n)/2, sqrt(n)/2], where n is the dimensionality
        raw_noise = generate_perlin_noise_2d((num_rows, num_columns), (noise_scale, noise_scale))
        noise = (raw_noise - raw_noise.min()) / (raw_noise.max() - raw_noise.min()) # [0, 1]

        for j in range(num_rows):

            print(f'Progress: Layer[{layer}], {j + 1}/{num_rows} lines ({j / num_columns * 100:.02f}%)', end='\r')

            for i in range(num_columns):
                pixel_x, pixel_y = (i * grid_size + left_x, j * grid_size + top_y)

                for _ in range(curve_steps):
                    if 0 <= pixel_x < image_width and 0 <= pixel_y < image_height:
                        color: list[np.float64] = image[math.floor(pixel_x)][math.floor(pixel_y)]
                        r = 1.0 - color[0]
                        g = 1.0 - color[1]
                        b = 1.0 - color[2]
                        image[math.floor(pixel_x)][math.floor(pixel_y)] = np.clip([r, g, b], 0, 1)

                    x_offset = pixel_x - left_x
                    y_offset = pixel_y - top_y

                    column_index = int(x_offset / grid_size)
                    row_index = int(y_offset / grid_size)

                    if 0 <= row_index < len(noise) and 0 <= column_index < len(noise):
                        grid_angle: float = noise[column_index][row_index] * 2 * math.pi
                    else:
                        continue

                    step_x = math.cos(grid_angle)
                    step_y = math.sin(grid_angle)

                    pixel_x = pixel_x + step_x # Here
                    pixel_y = pixel_y + step_y # Here

    plt.imsave(save_to_file, image)  # Saves image

def main() -> None:
    """ Main
    """
    image_height: int = 1000 # 1920
    image_width: int = 1000 # 1080
    render_rays(image_height, image_width, grid_size=5, noise_scale=5, curve_steps=20, save_to_file='image.png')

if __name__ == '__main__':
    main()