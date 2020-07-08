def subset(array,k):
    if len(array) == 0:
        return None
    if array[0] == k:
        return [array[0]]

    first = subset(array[1:],k-array[0])

    if first:
        return [array[0]] + first
    else:
        return subset(array[1:],k)


print(subset([],1))
print(subset([12,1,61,9,2,5],24))