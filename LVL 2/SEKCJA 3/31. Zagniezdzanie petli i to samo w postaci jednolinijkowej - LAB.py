ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

lines1 = [(p,k) for p in ports for k in ports]
print(lines1)

lines2 = [(p,k) for p in ports for k in ports if p != k]
print(lines2)

#błąd
lines3 = {p:k for p in ports for k in ports if p != k}
print(lines3)

lines4 = [(p,k) for p in ports for k in ports if p < k]
print(lines4)

print("Liczba połączeń w poszczególnych krokach: ")
print("Połączenia 1: {}, Połączenia 2: {}, Połączenia 3: {}, Połączenia 4: {}".format(len(lines1),len(lines2),len(lines3),len(lines4)))

