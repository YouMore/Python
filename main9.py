def first(test):
    for i in test:
        for j in range(4, 0, -1):
            if i[j] is None:
                i.pop(j)
    return test


def second(test):
    for i in range(len(test) - 1, -1, -1):
        if test[i] == [None]:
            del test[i]
            i -= 1
    return test


def third(test):
    for i in range(len(test)):
        for j in range(len(test[i])):
            if j == 0:
                test[i][j] = test[i][j][0:str(test[i][j]).find(",")]
            if j == 1:
                test[i][j] = format(round(float(test[i][j]), 3), ".3f")
            if j == 2:
                if test[i][j] == "Не выполнено":
                    test[i][j] = "Нет"
                else:
                    test[i][j] = "Да"
            if j == 3:
                test[i][j] = test[i][j][test[i][j].find("]") + 1:]
    return test


def main(test):
    test = first(test)
    test = second(test)
    test = third(test)
    final_test = [[test[j][i] for j in range(len(test))]
                  for i in range(len(test[0]))]
    return final_test


entered_data = [[None, None, None, None, None],
                ['Шилошук, А.А.', None, '0.40', 'Выполнено', 'silosuk98[at]yandex.ru'],
                ['Чонко, Р.Ш.', None, '0.17', 'Выполнено', 'conko28[at]gmail.com'],
                ['Кешисман, С.У.', None, '0.14', 'Выполнено', 'kesisman71[at]mail.ru'],
                ['Ромов, Е.Б.', None, '0.20', 'Выполнено', 'romov54[at]yandex.ru']
            ]
print(main(entered_data))