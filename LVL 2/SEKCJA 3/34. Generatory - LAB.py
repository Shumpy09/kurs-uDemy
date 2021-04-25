ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

lines1 = ( (p,k) for p in ports for k in ports)
print("lines1")
counter = 0
for (p,k) in lines1:
    print("{} - {}".format(p,k))
    counter +=1

print(counter)

lines2 = ((p,k) for p in ports for k in ports if p != k)
print("lines2")
counter = 0
for (p,k) in lines2:
    print("{} - {}".format(p,k))
    counter +=1

print(counter)

#błąd
lines3 = {p:k for p in ports for k in ports if p != k}
print("lines3")
print(lines3)

lines4 = ((p,k) for p in ports for k in ports if p < k)
print("lines4")
counter = 0
for (p,k) in lines4:
    print("{} - {}".format(p,k))
    counter +=1

print(counter)

# test