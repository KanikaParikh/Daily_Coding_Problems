# SIZE = 32
def non_duplicate(array):
    non_dup = 0

    for i in range(0, 32):
        i_bits = 0

        # '<<'- left shift operator -- multiplies number with 2 in decimal
        x = 1 << i

        for j in range(len(array)):
            if array[j] & x:
                i_bits += 1


        if i_bits % 3:
            non_dup |= x

    return non_dup


print(non_duplicate([19, 13, 13, 13]))
print(non_duplicate([6,1,3,3,3,6,6]))
