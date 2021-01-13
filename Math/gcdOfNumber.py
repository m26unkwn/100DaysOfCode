# Finding gcd of two number

m=20
n=10

while m%n!=0:
    old_m=m
    print(old_m)
    old_n=n
    print(old_n)

    m=old_n
    print(m)
    n=old_m%old_n
print(n)
    