def encode(input):
    encoded_list = list()

    c = 0
    prev_letter = None
    for letter in input:

        if letter == prev_letter or not prev_letter:
            c += 1
        else:
            encoded_list.append(str(c))
            encoded_list.append(prev_letter)
            c = 1
        prev_letter = letter

    if c:
        encoded_list.append(str(c))
        encoded_list.append(prev_letter)

    return "".join(encoded_list)


def decode(str):
    decoded_list = list()
    i = 0

    while i < len(str):
        decoded_list.append(int(str[i]) * str[i + 1])
        i += 2

    return "".join(decoded_list)


print(encode("AAAABBBCCDAA"))
print(decode("4A3B2C1D2A"))
