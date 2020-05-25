def pre(list,substr):
    res= []
    count= len(substr)
    for word in list:

        if word[0:count] == substr:
            res.append(word)
    return res

#list=["date","dog","deer","deal"]
#print(pre(list,"de"))
