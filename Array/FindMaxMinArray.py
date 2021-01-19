def maxMinArray1(array):
    return max(array),min(array)

    



def maxMinArray(arr):
    n=len(arr)

    if(n%2==0):
        mx=max(arr[0],arr[1])
        mn= min(arr[0], arr[1])

        i=2

    else:
        mx=mn=arr[0]
        i=0

    for i in range(n-1):
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])
        i+=2
    
    return (mx, mn)

    
A=[3,6,2,7,9,1,35]
print(len(A))
print(maxMinArray(A)) 