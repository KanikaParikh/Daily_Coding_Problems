#Finding if k is sum of  any 2 digits--- only works for sorted list

def fun(list,k):
   # s_list = list.sort()
    res = False
    for i in list:
        z = i
        for j in list[z:]:
            if i+j == k:
                res= True
                print(str(i) +" + " + str(j) + " = "  + str(k) + " so, " + str(res))
            else:
                res= False
            #z+=1

#list = [1,2,3,5,7]
#k=8
#fun(list,k)
#fun([1,2,3,4,5,6,7,8],12)