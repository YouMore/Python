def encode_val(a, b, x):
    x = bin(x)[2:]
    if (len(x) < a):
        x = x.zfill(a)
    z = '0b'
    for i in range(a):
        z = z + x[i] * b
    return int(z, 2)


def decode_val(a, b, x):
    x = bin(x)[2:]
    if (len(x) < a * b):
        x = x.zfill(a*b)
    z = '0b'
    for i in range(0, a * b, b):
        substring = '0b' + x[i] + x[i+1] + x[i+2]
        if ham_dist(encode_val(a, b, int(substring, 2)), 0) <= 3:
            z = z + '0'
        else:
            z = z + '1'
    return int(z, 2)


def ham_dist(x1, x2):
    x1 = bin(x1)[2:]
    x2 = bin(x2)[2:]
    if (len(x1) < len(x2)):
        x1 = x1.zfill(len(x2))
    if (len(x2) < len(x1)):
        x2 = x2.zfill(len(x1))
    distance = 0
    for i in range(len(x1)):
        if x1[i] != x2[i]:
            distance += 1
    return distance

massage = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912, 2067455, 2093116, 1044928, 2064407,
           6262776, 2027968, 4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903,
           2067967, 2068456]

str_massage = ''
for y in range(len(massage)):
    str_massage = str_massage + (chr(decode_val(8, 3, massage[y])))
print(str_massage)
