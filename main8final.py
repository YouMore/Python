def main(x):
    character_map = {
        ord('\n'): None,
        ord(' '): None
    }
    x = x.replace("do", "")
    x = x.replace("od", "")
    x = x.replace("end", "")
    x = x.replace("var", "")
    x = x.translate(character_map)
    x = x.replace("->", " ")
    x = x.replace("@", " ")
    new_list_word = x.split()
    final_list = []
    for i in range(1, len(new_list_word), 2):
        final_list.append((new_list_word[i], new_list_word[i - 1][1:-1:1]))
    return final_list


s = "do do var @'xexera_45' -> tequbi_561 od do var @'riso_390'->\
    esance_880 od end"
print(main(s))
