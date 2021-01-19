# Finding gcd of two number

def gcdOfTwoNumber(m,n):
    while m%n!=0:
        old_m=m
        print(old_m)
        old_n=n
        print(old_n)

        m=old_n
        print(m)
        n=old_m%old_n
    return  n

print(gcdOfTwoNumber(20,10))
    