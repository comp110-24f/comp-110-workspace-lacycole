"""Coordinates for cq04"""

__author__ = "730735704"


def get_coords(xs: str, ys: str) -> None:
    idx_xs: int = 0  # index of x
    idx_ys: int = 0  # index of y
    while idx_xs < len(xs):  # iterates over every x
        while idx_ys < len(ys):  # iterates over every y
            print("(" + xs[idx_xs] + "," + ys[idx_ys] + ")")
            idx_ys += 1
        idx_xs += 1
        idx_ys = 0


if __name__ == "__main__":  # stops visualize from automatically printing
    print(get_coords("hi", "bye"))
