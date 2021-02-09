#Below solution divides the problem into subproblems of size y/2 and call the subproblems recursively. 

def power(a,b):
    if(b==1): return a
    elif(b%2==0):
         return (power(a, int(b / 2)) *
               power(a, int(b / 2)))
    
    else:
        return (a*(power(a, int(b / 2)) *
               power(a, int(b / 2))))

    

print(power(2,2))
