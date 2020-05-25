# For example, given s = "abcba" and k = 2, the longest substring
# with k distinct characters is "bcb".

# Enumerate() method adds a counter to an iterable and returns it in a form
# of enumerate object. This enumerate object can then be used directly in for
# loops or be converted into a list of tuples using list() method.


def sub_string(str, k):
    if not str:
        return ""
    elif k == 1:
        return str[0]
    elif len(str) <= k:
        return str

    first_index = str[0]
    second_index = 0
    while str[second_index] == first_index:
        second_index += 1

    char_count = 0
    chars_seen = set()
    current_str = None
    remaining_str = None

    current_str = str

    for i, ch in enumerate(str):
        if ch not in chars_seen:
            chars_seen.add(ch)
            char_count += 1

        if char_count > k:
            current_str = str[:i]
            remaining_str = str[second_index:]
            break

    longest_s = sub_string(remaining_str, k)
    long_substring = None
    if len(current_str) < len(longest_s):
        long_substring = longest_s
    else:
        long_substring = current_str
    return long_substring

# print(sub_string("abcba", 2))  # bcb
# print(sub_string("abcbbbabbcbbadd", 2))  # bbbabb
# print(sub_string("abcbbbaaaaaaaaaabbcbbadd", 1)) #a

