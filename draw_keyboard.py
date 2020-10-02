"""
Script that draws the hexagonal keyboard for a given solution
"""

import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt


from utils import check_keyboard, compute_cell_location


def get_args():
    """
    Parse the arguments from the terminal
    """

    descr = 'Draw the keyboard.'
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('--valid-keys', metavar='V', type=str,
                        default='data/en-keys.txt',
                        help='Filename with the valid keys')
    parser.add_argument('--keyboard', metavar='K', type=str,
                        required=True,
                        help='Keyboard assignment')

    return parser.parse_args()


def draw(keyboard, coords, radius=45):
    """
    Function that draws an hexagonal keyboard given the layout coordinates.
    """

    def _polygon_coordinates(radius, center):
        r = radius - 5
        coords_x, coords_y = center
        ret = []
        angle = 2 * np.pi / 6.

        for pos in range(6):
            ret.append((coords_x + r * np.cos(angle * pos),
                        coords_y + r * np.sin(angle * pos)))

        return np.asarray([ret]).astype(np.int)

    resolution = 2 * radius * (4 * 2) - 2 * radius
    resolution = (resolution, resolution, 3)

    text_shift = radius // 4

    drawing = np.zeros(resolution, dtype=np.uint8)

    coords_x, coords_y = resolution[0] / 2, resolution[1] / 2

    for cell in np.arange(37):
        pos = coords[cell] * radius
        pos = (int(pos[0] + coords_x), int(pos[1] + coords_y))

        if keyboard[cell] != '':
            color = (200, 200, 200)
        else:
            color = (75, 75, 75)

        cv2.fillPoly(drawing, _polygon_coordinates(radius, pos), color)
        cv2.putText(drawing, str(keyboard[cell]),
                    (pos[0] - text_shift, pos[1] + text_shift),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 3)

    return drawing


ARGS = get_args()

with open(ARGS.valid_keys, 'r') as f:
    VALID_CHARS = f.read()[:-1]

# Initialize the variables
COORDS = compute_cell_location()

# Read the assigment
ASSIGNMENT = ARGS.keyboard
ASSIGNMENT = [k if k != '_' else "" for k in ASSIGNMENT]

# Validate the keyboard
check_keyboard(ASSIGNMENT, VALID_CHARS)

IMG = draw(ASSIGNMENT, COORDS)
plt.imshow(IMG[:, :, ::-1])
plt.axis('off')
plt.show()
