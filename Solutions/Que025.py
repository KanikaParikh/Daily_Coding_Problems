def match_func(regex, word):
    # no regex, no word -- return True
    if not regex:
        return not word

    first = bool(word) and regex[0] in {word[0], '.'}

    if len(regex) >= 2 and regex[1] == '*':
        return match_func(regex[2:], word) or (first and match_func(regex, word[1:]))
    else:
        return first and match_func(regex[1:], word[1:])


print(match_func("ra.", "ray"))
print(match_func(".*at", "chats"))
