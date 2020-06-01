# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''
time        type        room_number
0           start           1
30          start           2
50          end             1
60          start           2
75          end             1
150         end             0
'''


def num_of_rooms(time_interval):

    # sort the start time and end time individually
    start_time = sorted([i[0] for i in time_interval])
    end_time = sorted([i[1] for i in time_interval])

    occupied_room = rooms = 0
    m = n = 0
    l = len(time_interval)

#if start time is less than end time then assign one room to it-- when end
#time is greater than start time then we can use this room and hence subtract one


    while m <l and n < l:
        if start_time[m] < end_time[n]:
            occupied_room += 1
            rooms = max(occupied_room, rooms)
            m += 1
        else:
            occupied_room -= 1
            n += 1

    return rooms


list = [(30, 75), (0, 50), (60, 150)]
list2 = [(30, 75), (0, 50), (10, 60), (60, 150)]
print(num_of_rooms(list))
print(num_of_rooms(list2))

