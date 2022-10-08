arg_list = [0.1*i for i in range(100)]

formula = input("Formula f(x) to calculate: ")

for x in arg_list:
    print(x, eval(formula, {'x': x, 'math': __import__('math')}))
