def generate_power_set(num_list):
    if len(num_list) == 0:
        return [set([])]

    powerset = list()

    current = num_list[0]

    # adding individual entries in powerset
    sub_powerset = generate_power_set(num_list[1:])
    powerset.extend(sub_powerset)

    for i in sub_powerset:
        newset = i.copy()
        newset.add(current)
        powerset.append(newset)

    return powerset


print(generate_power_set([1]))
print(generate_power_set([1, 2]))
print(generate_power_set([1, 2, 3]))
