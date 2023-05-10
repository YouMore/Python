from functools import cache



@cache
def lev_dist(s1: str, s2: str) -> int:
    return f(s1, s2, len(s1), len(s2))

@cache
def f(a, b, i, j):
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return f(a, b, i - 1, j - 1)
    else:
        return 1 + min(f(a, b, i, j - 1), f(a, b, i - 1, j), f(a, b, i - 1, j - 1))


print(lev_dist('столб', 'слон'))


def lev_dist_ops(s1, s2):
    j = 0
    count = 0
    count_max = lev_dist('столб', 'слон')
    actions = [''] * count_max

    for i in range(len(s1)):

        if j > len(s2) - 1:
            actions[count] = "DELETE"
            count += 1

        if j <= len(s2) - 1 and s1[i] != s2[j]:
            if j > len(s2) - 1:
                actions[count] = "DELETE"
                count += 1
            elif i + 1 > len(s1) - 1 and j + 1 > len(s2) - 1:
                actions[count] = "REPLACE"
                count += 1
                j += 1
            elif i + 1 > len(s1) - 1 or j + 1 > len(s2) - 1:
                actions[count] = "DELETE"
                count += 1
            elif s1[i + 1] == s2[j + 1]:
                actions[count] = "REPLACE"
                count += 1
                j += 1
            else:
                actions[count] = "DELETE"
                count += 1

        else:
            j += 1
    return actions

print(lev_dist_ops('столб', 'слон'))

