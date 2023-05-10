def main(x):
    return int(((x & int('0b1111', 2)) << 8) |
               (((x >> 4) & int('0b11', 2)) << 6) |
               (((x >> 6) & int('0b111111111', 2)) << 12) |
               (((x >> 15) & int('0b0000', 2)) << 28) |
               ((x >> 19) & int('0b111111', 2)) |
               (((x >> 25) & int('0b1111111', 2)) << 21))

print(main(1918333345))
print(main(202945760))
print(main(3406622740))
print(main(3388775956))