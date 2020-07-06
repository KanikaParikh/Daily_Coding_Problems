def edit_dist(str1,str2):

    if str1==str2:
        return 0
    elif not str1:
        return len(str2)
    elif not str2:
        return len(str1)

    if str1[0] == str2[0]:
        return edit_dist(str1[1:],str2[1:])

    return 1 + min(edit_dist(str1[1:],str2),edit_dist(str1,str2[1:]),edit_dist(str1[1:],str2[1:]))

print(edit_dist("kitten","sitting"))
print(edit_dist("",""))
print(edit_dist("s","t"))



