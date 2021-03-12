def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)


print(fact(900))

# this one is not optimal one beacuse after n=> 1000 the recursion depth case exceed
