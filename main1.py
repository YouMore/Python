import math


def main(x, z, y):
    return round(
        (
            math.sqrt(((math.sqrt(4 * (x**2) + (y**3) / 6 + 1)) ** 6) - (z**4))
            + (
                (7 * (x**3) + 95 * (y**2) + (((23 * (z**3)) ** 5) / 43))
                / ((math.sin(x + y**2 + z**3)) ** 6)
            )
        ),
        2,
    )

print(main(-0.87, -0.09, 0.53))
print(main(-0.31, 0.33, 0.66))
print(main(0.57, 0.54, 0.88))
print(main(-0.81, 0.13, 0.27))
print(main(0.16, 0.23, 0.03))
