s = ([1992, 0, 'ANTLR', 'FLUX'],
     [1992, 0, 'ANTLR', 'ANTLR'],
     [1992, 0, 'ANTLR', 'TEX'],
     [1976, 'SCSS', 'ANTLR', 0],
     [1976, 'ROUGE', 'ANTLR', 0],
     [1988, 0, 'ANTLR', 'FLUX'],
     [1988, 0, 'ANTLR', 'ANTLR'],
     [1988, 0, 'ANTLR', 'TEX'],
     [0, 0, 'COOL', 'FLUX'],
     [1992, 0, 'COOL', 'ANTLR'],
     [1976, 0, 'COOL', 'ANTLR'],
     [1988, 0, 'COOL', 'ANTLR'],
     [0, 0, 'COOL', 'TEX'])

def main(x):
    a = [0] *13
    b = [4] *13
    k = 0;
    for str in s:
        for i in range(4):
            if str[i] == 0:
                b[k] = b[k] - 1
            if x[i] == str[i]:
                a[k] = a[k] + 1
        k = k + 1
    for j in range (13):
        if a[j] == b[j]:
            return j

print(main([1988,'ROUGE','ANTLR','TEX']))
print(main([1976,'ROUGE','COOL','FLUX']))
print(main([1992,'SCSS','COOL','ANTLR']))
print(main([1988, 'SCSS', 'ANTLR', 'FLUX']))
print(main([1976, 'ROUGE', 'COOL', 'TEX']))