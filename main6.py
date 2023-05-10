s = (['OPAL', 0, 'PONY', 1965, 0],
     ['OPAL', 0, 'PONY', 2014, 0],
     ['OPAL', 0, 'PONY', 1963, 'YANG'],
     ['OPAL', 0, 'PONY', 1963, 'CLIPS'],
     ['OPAL', 0, 'PONY', 1963, 'X10'],
     ['OPAL', 0, 'DM', 1965, 0],
     ['OPAL', 1982,  'DM', 2014, 0],
     ['OPAL', 2003, 'DM', 2014, 0],
     ['OPAL', 1982, 'DM', 1963, 0],
     ['OPAL', 2003, 'DM', 1963, 0],
     ['OPAL', 0, 'UNO', 0, 0],
     ['DIFF', 0, 0, 0, 0],
     ['ARC', 0, 0, 0, 0])

def main(x):
    a = [0] *13
    b = [5] *13
    k = 0;
    for str in s:
        for i in range (5):
            if str[i] == 0:
                b[k] = b[k] - 1
            if x[i] == str[i]:
                a[k] = a[k] + 1
        k = k +1
    for j in range (13):
        if a[j] == b[j]:
            return j

print(main(['DIFF', 2003, 'UNO', 1965, 'CLIPS']))
print(main(['ARC', 2003, 'UNO', 1963, 'CLIPS']))
print( main(['OPAL', 2003, 'PONY', 1965, 'X10']))
print(main(['OPAL', 2003, 'PONY', 2014, 'YANG']))
print(main(['OPAL', 1982, 'DM', 1965, 'CLIPS']))