# complex_exponents.py
#       A program to compute complex numbers raised to complex powers
# Kevin Kredit
# 8/5/10

from math import *

def main():
    print 'Compute (a+bi)^(c+di)'
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))
    d = float(input('d: '))
    print '\n',f(a,b,c,d),'\n\n'

def f(a,b,c,d):
    if not a and not b:
        return 0.0
    try:
        ang = atan(b/a)
        if b == 0 and a < 0:
            ang = pi
    except:
        if b > 0: ang = pi*0.5
        if b < 0: ang = pi*1.5
    real = (a**2+b**2)**(c/2.0)*e**(-d*ang)*cos(d*log(a**2+b**2)/2.0+c*ang)
    imag = (a**2+b**2)**(c/2.0)*e**(-d*ang)*sin(d*log(a**2+b**2)/2.0+c*ang)
    return str(myRound(real,.0000000001))+'+'+\
           str(myRound(imag,.0000000001))+'i'

def myRound(x,a):
    return int((1/a)*x+(-.5+int(x>0)))*a

while True:
    main()
