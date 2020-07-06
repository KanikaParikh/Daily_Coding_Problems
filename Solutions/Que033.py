import heapq as h


def running_median(array):
    if not array:
        return None

    max_heap = list()
    min_heap = list()
    med = list()

    for i in array:
        h.heappush(min_heap, i)
        if len(min_heap) > len(max_heap) + 1:
            element = h.heappop(min_heap)
            h.heappush(max_heap, -element)

        if len(min_heap) == len(max_heap):
            m = (min_heap[0] - max_heap[0]) / 2
        else:
            m = min_heap[0]
        med.append(m)
    return med


print(running_median([2, 5]))
print(running_median([2,1,5,7,2,0,5]))
