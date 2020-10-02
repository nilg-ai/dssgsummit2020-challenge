"""
Auxiliary functions for the ALS keyboard challenge
"""

import numpy as np


def check_keyboard(keyboard, valid_chars):
    """Validates if the keyboard is valid based on a set of valid characters
    """

    assert len(keyboard) == 37
    assert all([x in valid_chars for x in keyboard])
    assert all([x in keyboard for x in valid_chars])


def compute_cell_location():
    """Compute the location of each key in the hexagonal keyboard
    """

    ring_id = np.asarray([0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                          2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                          3])

    n_cells = len(ring_id)
    n_rings = max(ring_id) + 1

    coords = np.zeros((n_cells, 2))
    radius = 1.

    dist = 2 * radius * np.cos(30 / 180. * np.pi)
    angle = 2 * np.pi / 6.

    sin_dir = dist * np.sin(angle * np.arange(6))
    cos_dir = dist * np.cos(angle * np.arange(6))

    for rid in range(n_rings):
        cells_in_ring = np.arange(n_cells)[ring_id == rid]
        pos = (0, 0 - rid * dist)

        current_dir = 2
        remaining_in_edge = rid

        for cell in cells_in_ring:
            coords[cell] = pos

            if remaining_in_edge == 0:
                current_dir = (current_dir + 1) % 6
                remaining_in_edge = rid

            pos = (pos[0] + sin_dir[current_dir],
                   pos[1] - cos_dir[current_dir])
            remaining_in_edge -= 1
    return coords
