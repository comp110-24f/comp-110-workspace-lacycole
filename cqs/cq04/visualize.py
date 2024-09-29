from cqs.cq04.concatenation import concat
from cqs.cq04.coordinates import get_coords

"""Visualize for cq04"""

__author__ = "730735704"

x: str = "123"
y: str = "adc"

print(concat(x, y))  # calls concat with x and y
get_coords(x, y)  # calls get_coords with x and y
