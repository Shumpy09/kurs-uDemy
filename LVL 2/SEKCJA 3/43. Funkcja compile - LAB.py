import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range(100000):
    argument_list.append(i/10)

for formula in formulas_list:
    results_list = []
    print("Trwaja prace nad formula: {}".format(formula))
    
    start = time.time()
    
    for x in argument_list:
        results_list.append(eval(formula))
    
    print("Min value: {}".format(min(results_list)))
    print("Max value: {}".format(max(results_list)))
    
    stop = time.time()
    
    compiled_time = stop - start
    print(compiled_time)


for formula in formulas_list:
    results_list = []
    print("Trwaja prace nad formula: {}".format(formula))
    
    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(formula))
    
    print("Min value: {} Max value: {}".format(min(results_list), max(results_list)))
    stop = time.time()
    
    compiled_time = stop - start
    print(compiled_time)