def reverseArray(list_Array):
    start=0
    end=len(list_Array)-1
    while start < end:
        list_Array[start],list_Array[end]=list_Array[end],list_Array[start]
        start+=1
        end-=1
    return list_Array

array=[1,2,3,4,5,7]
print(reverseArray(array))

