'''
i = 10
result = 1

for j in range(1, i+1):
    result *=j

print(i, result)    
'''
'''
x = 10
for i in range(1, x+1):
    result = 1

    for j in range(1, i+1):
        result *= j
    
    print(i, result)
'''
'''
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']
result = 0

for i in list_adj:
    for j in list_noun:
        print(i, j)
'''

i = 10
result = 1
for x in range(1, i+1):
    
    
    for y in range(1, x+1):
        result *= y
    
    print(x, result)