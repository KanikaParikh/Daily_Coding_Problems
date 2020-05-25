#return new array with product of all integers except for that i :

def  fun2 (arr):
    res = 1
    new_arr =  []

    for i in arr:
        res = res*i
    for j in arr:
        new_arr.append(int(res/j))
    return new_arr

#print(fun2([1,2,3,4,5]))
#print(fun2([3,2,1]))