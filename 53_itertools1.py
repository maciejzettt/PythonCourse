from itertools import permutations
from itertools import product


notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
# a = combinations_with_replacement(notes, 4)
# all_a = []
# for ia in a:
#     all_a.extend(permutations(ia))
# print(all_a)
a = list(permutations(notes, 4))
print(len(a))
print(a)

b = list(product(notes, repeat=4))
print(len(b))
print(b)
