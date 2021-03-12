def mergeSort(arr):
    def merge(left, right):
        res = []
        while left and right:  # store fully sorted array here    while left and right: # both arrays are not empty
            if left[0] <= right[0]:
                res.append(left.pop(0))  # take first element
            else:                        # and put it to the
                res.append(right.pop(0))
        res = res + left + right  # left or right is empty at this point
        # just append the rest, as it is sorted
        return res

    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        left = mergeSort(left)
        right = mergeSort(right)
    return merge(left, right)


arr = [23, 123, 11, 22, 31, 2]

print(mergeSort(arr))
