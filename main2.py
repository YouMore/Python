import math

def main(x):
    if x < 34:
        return (round(((99 * (x**4)) - ((math.cos(x))**3) - 1), 2))
    elif 34 <= x < 107:
        return (round(((x**7) / 50), 2))
    else:
        return (round(((88 * (math.atan(x/75 - x**2))**3) + ((math.cos(x))**6) + 19 * ((98 * (x**3) - 69 * (x**2) - x)**2)), 2))


print(f(112))
print(f(70))
print(f(38))
print(f(76))
print(f(-42))
