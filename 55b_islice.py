import itertools as it
import math


def check_if_has_dividers(x):
    for i in range(2, math.ceil(x/2)):
        if x % i == 0:
            return True
    else:
        return False


# prime_numbers = list(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 100000)))
# print(prime_numbers)

prime_numbers = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 10)
print(list(prime_numbers))
