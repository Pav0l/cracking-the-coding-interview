from time import time

# Return n-th number from fibonaci sequence
# 0 1 1 2 3 5 8 13 21 34 ...
# fib(6) = 8


def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n-1) + fib(n-2)


a = 30
start = time()
print(fib(a))
end = time()
print(f'Fib recursion time for input {a}: {end-start}')


# fib with caching
def fib_c(n, cache={}):
    # specify base condition
    if n == 1 or n == 0:
        return n
    # check if n already exists in cache, if yes just return it
    elif n in cache:
        return cache[n]
    # if n is not in cache
    # and end condition is not met
    # save result of next recursive call into cache
    # and return the cache value at n
    else:
        cache[n] = fib_c(n-1, cache) + fib_c(n-2, cache)
        return cache[n]


b = 950
start1 = time()
print(fib_c(b))
end1 = time()
print(f'Fib recursion /w CACHE time for input {b}: {end1-start1}')
