import numpy as np
import math


def generateKey(n):
    b = []
    w = []
    i = 0
    sum = 0
    summand = 0
    q = 0
    r = 0
    while i < n:
        summand = np.random.randint(low=1, high=10000000000000)
        sum += summand
        w.append(sum)
        i += 1
    q = np.sum(np.array(w)) + np.random.randint(low=1, high=10000000000000)
    r = np.random.randint(low=-10000000000000, high=10000000000000)
    while(math.gcd(q, r) != 1):
        r = np.random.randint(low=-10000000000000, high=10000000000000)
    b = np.array([])
    b = (np.array(w) * r) % q
    return [w, q, r, b]


print(generateKey(7))


# arr = np.identity(5)
# np.random.shuffle(arr)
# print(arr, np.random.rand(1))
