'''For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.'''


def well_formed_brackets(b_string):
    b_stack = []  # array to maintain brackets
    starting_bracket = {"{", "[", "("}  # only opening brackets
    brackets_pair={"}":"{" , "]":"[" , ")":"("} #dictioanry to maintain pairs of brackets

    for i in b_string:
        if i in starting_bracket:
            b_stack.append(i)
        else:
            if b_stack and b_stack[-1] == brackets_pair[i]:
                b_stack.pop()
            else:
                return False
    return not b_stack

print(well_formed_brackets("([])[]({})"))
print(well_formed_brackets("([)]"))
print(well_formed_brackets("((()"))
