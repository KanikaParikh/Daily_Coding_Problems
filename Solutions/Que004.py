#Find First missing positive integer
#EX:input:[3,4,-1,1] ==2
#input:[1,2,0] == 3

def missing(input):
    if len(input) == 0:
        return 1

    maxvalue = max(input)
    if maxvalue <=0:
        return 1

    else:
        for i in range(1, maxvalue + 2):
            if not ( i in input ):
                return i
#i=[3,4,-1,1]
#print(missing(i))