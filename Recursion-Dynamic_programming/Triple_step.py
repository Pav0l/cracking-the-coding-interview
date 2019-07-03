"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
"""
from time import time
# define a function, which takes n number of steps in staircase and a cache dict


def triple_step(n, cache={}):
    # define end conditions
    if n == 0:
        return 1
    elif n < 0:
        return 0
    # check for n value in cache:
    elif n in cache:
        return cache[n]
    else:
        cache[n] = triple_step(n-1, cache) + \
            triple_step(n-2, cache) + triple_step(n-3, cache)
        return cache[n]


a = 300
start = time()
print(triple_step(a))
end = time()
print(f'Triple step with CACHE. input size {a}: {end-start}')
