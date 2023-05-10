from functools import cache


@cache
def lev_dist(s1: str, s2: str) -> int:
    @cache
    def f(a, b, i, j):
        if i == 0 or j == 0:
            return max(i, j)
        elif a[i - 1] == b[j - 1]:
            return f(a, b, i - 1, j - 1)
        else:
            return 1 + min(f(a, b, i, j - 1), f(a, b, i - 1, j), f(a, b, i - 1, j - 1))

    return f(s1, s2, len(s1), len(s2))


d = {}
with open("words.txt", encoding='UTF-8') as f:
    for line in f:
        (key, val) = line.split()
        d[str(key)] = int(val)


def spell(speech: str) -> str:
    words = speech.split()
    answer = []
    for word in words:
        synoms = None
        exists = False
        if d.get(word) is not None:
            answer.append(word)
            exists = True
        else:
            synoms = check_dict(word)
        if synoms != None:
            synoms.sort(key=lambda x: x[1], reverse=True)
            answer.append(synoms[0][0])
        elif not exists:
            answer.append(word)
    return ' '.join(answer)


def check_dict(word: str):
    ones = []
    twos = []
    for key in d:
        if lev_dist(word, key) == 1:
            ones.append((key, d.get(key)))
        elif len(ones) == 0:
            if lev_dist(word, key) == 2:
                twos.append((key, d.get(key)))
    if len(ones) > 0:
        return ones
    elif len(twos) > 0:
        return twos
    else:
        return None


print(spell('миня оня знает'))
print(spell('ты кта такай'))
print(spell('поставьте оценку'))