import geom

# ZADANIE 1

print(geom.GiveGeomSeqElement(1,2,64))

# ZADANIE 2
a1 = 3
factor = 2
maxindex = 10

for i in range(1, maxindex):
    an = geom.GiveGeomSeqElement(a1 = a1, factor = factor, index = i)
    print(i, an)

# ZADANIE 3

print(geom.GiveFactorForGeomSeq(12,24))

# ZADANIE 4

print(geom.GiveSumOfNElementsGeomSeq(2,3,4))




