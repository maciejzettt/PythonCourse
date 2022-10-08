import itertools as it


def get_factors(x):
    ret_list = [1]
    i = 2
    aux = x
    while i < aux:
        if x % i == 0:
            ret_list.append(i)
            aux = x / i
            ret_list.append(int(aux))
        i += 1
    return ret_list


def get_factors_old(x):
    ret_list = []
    for i in range(2, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list


candidate_list = list(range(1,10000000))
filter_list = []

for num in candidate_list:
    val = get_factors(num)
    if sum(val) == num:
        filter_list.append(True)
    else:
        filter_list.append(False)

magical = it.compress(candidate_list, filter_list)

print(list(magical))

