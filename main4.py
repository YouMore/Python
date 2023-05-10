import math

def main(n):
    f = 0
    if n == 0:
        f = 0.59
    if n >= 1:
        f = ((math.cos(main(n - 1)))**3) - (math.log((19 * ((main(n - 1))**2) + 1), 10))
    return f

print(main(5))
print(main(3))