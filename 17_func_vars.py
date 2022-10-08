def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


number = 8
transformations = [double, root, negative, div2]
tmp_ret = number

for instr in transformations:
    tmp_ret = instr(tmp_ret)
    print(tmp_ret)
