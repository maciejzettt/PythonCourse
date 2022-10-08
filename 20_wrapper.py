import functools
import time


def FncTime_wrapper(fnc):
    @functools.wraps(fnc)
    def wrapped(*args, **kwargs):
        fstart = time.time()
        result = fnc(*args, **kwargs)
        fend = time.time()
        if (fend - fstart) > 0.001:
            print("Function '{0}' execution time: {1} sec.".format(fnc.__name__, fend - fstart))
        return result
    return wrapped


@FncTime_wrapper
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(8))
