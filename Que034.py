def palindrome(str):
    # to check if its actual palindrome or not ex: mom
    if str[::-1] == str:
        return str

    # recursive call to check if first and last letter are same or not
    if str[0] == str[-1]:
        return str[0] + palindrome(str[1:-1]) + str[-1]

    else:
        #make palindrome using first letter
        palindrome_1 = str[0] + palindrome(str[1:]) +str[0]

        # make palindrome using last letter
        palindrome_2 = str[-1] + palindrome(str[:-1]) +str[-1]

        #compare their length
        if len(palindrome_1) > len(palindrome_2):
            return palindrome_2
        elif len(palindrome_2) > len(palindrome_2):
            return palindrome_1
        return palindrome_1 if palindrome_1 < palindrome_2 else palindrome_2

print(palindrome("racecar"))
print(palindrome("google"))
print(palindrome("egoogle"))

