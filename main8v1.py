from pyparsing import Word, alphas, ZeroOrMore, nums


def main(s):
    start_word = ZeroOrMore(" ") + "do" + ZeroOrMore(" ")
    end_word = ZeroOrMore(" ") + "end"
    between_word = ZeroOrMore(" ") + "od" + ZeroOrMore(" ")
    name_var = ZeroOrMore(" ") + "var" + ZeroOrMore(" ")
    dog_start = ZeroOrMore(" ") + "@"
    first_word = (
        ZeroOrMore(" ") + Word("'" + alphas + "_" + nums + "'")
        + ZeroOrMore(" ")
    )
    devide_symbol = ZeroOrMore(" ") + "->" + ZeroOrMore(" ")
    second_word = (
        ZeroOrMore(" ") + Word("'" + alphas + "_" + nums + "'")
        + ZeroOrMore(" ")
    )
    parse_module = (
        start_word
        + ZeroOrMore(
            start_word
            + name_var
            + dog_start
            + first_word
            + devide_symbol
            + second_word
            + between_word
        )
        + end_word
    )
    word_list = parse_module.parseString(s).asList()
    new_list_word = []
    for i in word_list:
        if len(i) > 3:
            new_list_word.append(i)
    final_list = []
    for j in range(1, len(new_list_word), 2):
        final_list.append((new_list_word[j], new_list_word[j - 1][1:-1:1]))
    return final_list

print(main(s))