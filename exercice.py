#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib as plt


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(start=-1.3, num=64, stop=2.5)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([(np.sqrt(c[0] ** 2 + c[1] ** 2), np.arctan2(c[1], c[0])) for c in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.abs(values - number).argmin()     # argmin() permet de trouver l'index du min et non la valeur


def draw_function():
    x = np.linspace(start=-1, stop=1, num=250)
    y = x ** 2 * np.sin(1 / (x ** 2)) + x

    plt.plot(x, y)
    plt.xlim((-2, 2))   # Pour modifier l'échelle des axes
    plt.show()


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # print(linear_values())
    draw_function()