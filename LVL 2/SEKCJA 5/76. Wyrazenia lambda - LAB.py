text_list = ['x','xxx','xxxxx','xxxxxxx','']


x = 'napis'
f = lambda x: len(x)

print(f(x))
print(f('napis'))

mapped_list = list(map(f, text_list))
print(mapped_list)
print(list(map(f,text_list)))

print(list(map(lambda s: len(s),text_list)))
