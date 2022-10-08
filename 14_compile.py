import math
import time as t

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

arg_list = [i/10 for i in range(1, 1000001)]

for formula in formulas_list:
    print("Processng formula: ", formula)
    start = t.time()
    results = []
    for x in arg_list:
        results.append(eval(formula))
    print("\tMin: {0:f};\tMax: {1:f}".format(min(results), max(results)))
    stop = t.time()
    print("\tEvaluation time (not compiled): ", stop - start)

for formula in formulas_list:
    print("Processng formula: ", formula)
    start = t.time()
    c_formula = compile(formula, "internal values", 'eval')
    results = []
    for x in arg_list:
        results.append(eval(c_formula))
    print("\tMin: {0:f};\tMax: {1:f}".format(min(results), max(results)))
    stop = t.time()
    print("\tEvaluation time (compiled): ", stop - start)
