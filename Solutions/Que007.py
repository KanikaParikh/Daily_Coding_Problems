#Given the mapping a=1, b=2 ... z=26. count number of ways it can be decoded.
# Example: 111  can be decoded as 1--1--1 , 11--1, 1---11 hence 3 ways
def ways(str):

    if not str:
        return 1
    elif int(str[:2]) <27 and int(str[:2]) >9 :
        return ways(str[1:]) +ways(str[2:])
    else:
        return ways(str[1:])

#print(ways("111"))