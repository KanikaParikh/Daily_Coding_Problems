def long_palindrome(str):
    if not str or (str == str[::-1]):
        return str

    front_palindrome = long_palindrome(str[1:])
    last_palindrome = long_palindrome(str[:-1])

    if len(front_palindrome) >= len(last_palindrome):
        return front_palindrome
    else:
        return last_palindrome


print(long_palindrome("bananas"))
print(long_palindrome("mom"))
print(long_palindrome("aabcdcb"))
