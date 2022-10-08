import functools
import time


@functools.lru_cache()
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


def fib_u(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


tstart = time.time()

for i in range(1,53):
    print("Fib_U({0} = {1} :: {2} s".format(i, fib_u(i), time.time()-tstart))
unopt_time = time.time() - tstart

tstart = time.time()

for i in range(1,53):
    print("Fib({0} = {1} :: {2} s".format(i, fib(i), time.time()-tstart))
opt_time = time.time() - tstart

timediff = unopt_time - opt_time
print("Time difference: ", timediff)
print(fib.cache_info())
