def reverseArray(list_Array, start, end):
    while start < end:
        list_Array[start],list_Array[end]=list_Array[end],list_Array[start]
        start+=1
        end-=1
    return list_Array

array=[1,2,3,4,5,7]
print(reverseArray(array,0,len(array)-1))

