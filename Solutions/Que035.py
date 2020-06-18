def helper(array, start, end, letter):
    i = start
    j = end
    last_index = -1

    while i < j:

        if array[i] == letter:
            last_index = i
            i += 1
        elif array[j] != letter:
            j -= 1

        else:
            last_index = i

            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    return last_index


def rearrange_array(array):
    last = helper(array, 0, len(array) - 1, "R")
    helper(array, last + 1, len(array) - 1, "G")
    return array


print(rearrange_array(['G', 'B', 'R', 'R', 'R', 'G','B', 'G', 'R','B']))
print(rearrange_array(['B', 'G', 'R']))
