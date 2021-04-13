import math

def GiveGeomSeqElement(a1 = 2, factor = 2, index = 2):
    # a1 - pierwszy element ciagu
    # factor - współczynnik ciągu
    # index - element ciągu, który ma być wyliczony

    value = a1*pow(factor,index-1)

    return value

def GiveFactorForGeomSeq(term, nextterm):
    # wyznaczanie wartości współczynnika gdy znane sa 2 kolejne wyrazy

    q = nextterm/term

    return q

def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):

    sn = a1*(1-pow(factor,n))/(1-factor)
    
    return sn