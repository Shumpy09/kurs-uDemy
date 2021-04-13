# ZADANIE 1
import math

def GiveGeomSeqElement(a1 = 2, factor = 2, index = 2):
    # a1 - pierwszy element ciagu
    # factor - współczynnik ciągu
    # index - element ciągu, który ma być wyliczony

    value = a1*pow(factor,index-1)

    return value

print(GiveGeomSeqElement(1,2,64))

# ZADANIE 2
a1 = 3
factor = 2
maxindex = 10

for i in range(1, maxindex):
    an = GiveGeomSeqElement(a1 = a1, factor = factor, index = i)
    print(i, an)

# ZADANIE 3
def GiveFactorForGeomSeq(term, nextterm):
    # wyznaczanie wartości współczynnika gdy znane sa 2 kolejne wyrazy

    q = nextterm/term

    return q

print(GiveFactorForGeomSeq(12,24))

# ZADANIE 4
def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):

    sn = a1*(1-pow(factor,n))/(1-factor)
    
    return sn

print(GiveSumOfNElementsGeomSeq(2,3,4))




