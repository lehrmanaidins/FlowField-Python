"""
    Main Module
    Author: Aidin Lehrman

    https://tylerxhobbs.com/essays/2020/flow-fields
"""

from Vector2 import Point2, Ray2, Vector2


def main() -> None:
    """ Main
    """
    point: Point2 = Point2(1, 2)
    print(point)

    vector: Vector2 = Vector2(2, 1)
    print(vector)

    ray: Ray2 = Ray2(point, vector)
    print(ray)


if __name__ == '__main__':
    main()
