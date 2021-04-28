def double(x):
    return 2 *x

def root(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x/2

def generate_values(how, numlist):
       
    list_of_value = []

    for n in numlist:
        list_of_value.append(how(n))

    return list_of_value



numlist = list(range(11))

print(generate_values(double,numlist))
print(generate_values(root,numlist))
print(generate_values(negative,numlist))
print(generate_values(div2,numlist))