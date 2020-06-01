def words_set(words_dict, string):
    words_result = []
    while string:
        foo = False
        for i in words_dict:
            if string.startswith(i):
                words_result += [i]
                foo = True
                string = string[len(i):]
                break

        if not foo:
            return None

    return words_result


print(words_set(['quick', 'brown', 'the', 'fox'], 'thequickbrownfox'))
print(words_set(['bed', 'bath', 'bedbath', 'and', 'beyond'], "bedbathandbeyond"))
