q = 'THE EYES'
print(q)
print(q[0], q[1], q[2], q[5], q[3], q[7], q[4], q[6])
print(q[0] + q[1] + q[2] + q[5] + q[3] + q[7] + q[4] + q[6])

q = 'the gentleman'
print(q)
print(q[3], q[6], q[7], q[2], q[0], q[4], q[5], q[1], q[8:])
print(q[3] + q[6] + q[7] + q[2] + q[0] + q[4] + q[5] + q[1] + q[8:])

q = 'THE MORSE CODE'
print(q)
print(q[1], q[2], q[6], q[8], q[10], q[11], q[4], q[13], q[12], q[11], q[0], q[7])
print(q[1] + q[2] + q[6] + q[8] + q[10] + q[11] + q[4] + q[13] + q[12] + q[11] + q[0] + q[7])
print(q[1:3]  + q[6] + q[8], q[3] + q[10:12] + q[4] + q[13], q[9] + q[12] + q[5] + q[0] + q[7])

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[33:]
print(time)

tmp = line[9:]
print(tmp)

title = tmp[:12]
print(title, time)

line = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
time = line[line.find(':')+2:]
print(time)

tmp = line[line.find('"')+1:]
print(tmp)

title = tmp[:tmp.find('"')]
print(title, time)
