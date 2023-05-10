import math

def main(m, b, a):
    f = 0
    for i in range(1, a + 1):
        for k in range(1, b + 1):
            for j in range(1, m + 1):
                f += (37 * (math.sin(76 + 16 * (j**2) + ((i**3)/88))) - ((k**2)/28))
    return round(f, 2)

print(main(2, 8, 7))
print(main(6, 8, 4))