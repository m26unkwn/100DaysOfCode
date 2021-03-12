def fab(n):
    if n <= 1:
        return n
    return fab(n-1) + fab(n-2)


print(fab(2))

# this one is too slow optimal code will be pushed soon
