from collections import deque


def max_array(arr, k):
    n = len(arr)
    max_list = list()
    que = deque()

    # Process first k elements of array
    for index in range(k):
        while que and arr[index] > arr[que[-1]]:
            que.pop()
        que.append(index)
    max_list.append(arr[que[0]])

    # Process rest of elements from arr[k] to arr[n-1]

    for index in range(k, n):
        # queue will have largest element at que[0]
        while que and que[0] <= index - k:
            que.popleft()

        while que and arr[index] > arr[que[-1]]:
            que.pop()
        que.append(index)

        max_list.append(arr[que[0]])

    return max_list


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(max_array(arr, k))  # [3, 4, 5, 6, 7, 8, 9, 10]

test_arr = [10, 5, 2, 7, 8, 7]
k = 3
print(max_array(test_arr, k))  # [10, 7, 8, 8]
