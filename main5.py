import math

def main(x, z, y):
    f = 0
    for i in range(1, len(x) + 1):
        f += 58 * (((x[len(x) + 1 - math.ceil(i/4) - 1])**3) - (66 * z[i - 1]) - (83 * ((y[len(y) + 1 - math.ceil(i/3) - 1])**2)))**6
    return round((63 * f), 2)

print(main([0.58, -0.2, 0.09, -0.75], [0.46, 0.88, 0.76, 0.04], [0.48, -0.16, -0.2, -0.27]))