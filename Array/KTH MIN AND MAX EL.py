def MinandMax(arr,k):
    x=sorted(arr)

    min=x[k-1]
    max=x[-k]

    return min,max



arr = [7, 10, 4, 3, 20, 15]

print(MinandMax(arr,3))

