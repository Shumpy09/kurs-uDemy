import math

def check_int(s):
    # Czy liczba jest całkowita
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
'''
def Delta(a, b, c):
    d = pow(b,2)-4*a*c
    return d

def X1(d, b, a):
    return (-b-sqrt(d))/2*a

def X2(d, b, a):
    return (-b+sqrt(d)/2*a)
'''

a_str = input("Enter a: ")
b_str = input("Enter b: ")
c_str = input("Enter c: ")



if not (check_int(a_str) and check_int(b_str) and check_int(c_str)):
     print("Nieprawidłowe dane")
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)

    if a==0:
        print("Nie jest to równanie kwadratowe")

    else:
        delta = b**2-4*a*c

        if delta > 0:
            x1 = (-b-delta**0.5)/(2*a)
            x2 = (-b+delta**0.5)/(2*a)
            print("Delta dodatnia. Istnieją 2 rozwiązania: %.2f i %.2f" % (x1, x2)) 
        
        elif delta == 0:
            x1 = -b/(2*a)
            print("Delta równa 0. Istnieje 1 rozwiązanie: %.2f" % (x1))
        else:
            print("Delta = 0. Brak rozwiązania.")
