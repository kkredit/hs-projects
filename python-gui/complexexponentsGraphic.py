# complexexponentsGraphic.py
#       A program to visually display individual terms of (a+bi)^(c+di)
# Kevin Kredit
# 8/8/10

from math import *
from graphics import *

def auto():
    for i in [2,3,4,5,6]:
        main(1,1,i,0)
        #main(i**-1,1,12,0)
    inputs()

def inputs():
    print 'Compute and draw (a+bi)^(c+di)\n'
    
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))
    d = float(input('d: '))
    main(a,b,c,d)

    inputs()

def main(a,b,c,d):    
    
    terms = [a,b]
    icoef = [0,1]
    for n in range(int(c-1)):
        terms,icoef = term(a,b,terms,icoef)
        
    if int(c) == 0:
        terms = [1,0]
        icoef = [0,1]
    x,y = [],[]
    
    for n in range(len(icoef)):### handles the rule i^0=0, i^1=i, i^2=-1, i^3=-i
        ival = icoef[n] % 4
        if ival == 0:
            x.append(terms[n])
        elif ival == 1:
            y.append(terms[n])
        elif ival == 2:
            x.append(-terms[n])
        else:
            y.append(-terms[n])
            
    if d:###allows and adjusts for complex exponents
        g,h = f(a,b,0,d)###(a+ib)*(c+id) = (ac-bd)+i(bc+ad)
        for i in range(len(x)):
            e = x[i]
            z = y[i]
            x[i] = e*g-z*h
            y[i] = z*g+e*h
            
    if c % 1:###allows and adjusts for non-integer c
        g,h = f(a,b,c%1,0)###(a+ib)*(c+id) = (ac-bd)+i(bc+ad)
        for i in range(len(x)):
            e = x[i]
            z = y[i]
            x[i] = e*g-z*h
            y[i] = z*g+e*h

    print x
    print y
    show(x,y)### draws the terms on the complex plane
    

def term(a,b,terms,icoef):
    nterms = []
    for t in terms:
        nterms.append(a*t)
    for t in terms:
        nterms.append(b*t)
    nicoef = []
    for i in icoef:
        nicoef.append(i+1)
    return nterms,icoef+nicoef

def f(a,b,c,d):
    if not a and not b: return 0.0
    try:
        ang = atan(b/a)
        if b == 0 and a < 0: ang = pi
    except:
        if b > 0: ang = pi*0.5
        if b < 0: ang = pi*1.5
    real = (a**2+b**2)**(c/2.0)*e**(-d*ang)*cos(d*log(a**2+b**2)/2.0+c*ang)
    imag = (a**2+b**2)**(c/2.0)*e**(-d*ang)*sin(d*log(a**2+b**2)/2.0+c*ang)
    return myRound(real,.0000000001),myRound(imag,.0000000001)

def myRound(num,accuracy):
    return int((1/accuracy)*num+(-.5+int(num>0)))*accuracy

def show(x,y):
    
    win = GraphWin('Complex Exponent Components',200,200)
    win.setBackground('black')
    
    xcount,xmax,xmin = 0,0,0### sets the Coordinates and Axis
    for n in x:
        xcount += n
        if xcount > xmax: xmax = xcount
        if xcount < xmin: xmin = xcount
    ycount,ymax,ymin = 0,0,0
    for n in y:
        ycount += n
        if ycount > ymax: ymax = ycount
        if ycount < ymin: ymin = ycount
    xdif = xmax-xmin
    ydif = ymax-ymin
    maxdif = xdif
    if ydif > xdif: maxdif = ydif
    maxdif *= 1.1
    win.setCoords((xmin-(maxdif-xdif)/2.0),(ymin-(maxdif-ydif)/2.0),\
                  (xmax+(maxdif-xdif)/2.0),(ymax+(maxdif-ydif)/2.0))    
    xaxis = Line(Point(xmin-(maxdif-xdif)/4.0,0),\
                 Point(xmax+(maxdif-xdif)/4.0,0))
    yaxis = Line(Point(0,ymin-(maxdif-ydif)/4.0),\
                 Point(0,ymax+(maxdif-ydif)/4.0))

    ### draws axis, labels
    '''for axis in [xaxis,yaxis]:
        axis.setFill('red')
        axis.draw(win)
    orig = Text(Point(0,0),'O')
    ylabel = Text(Point(0,ymax+(maxdif-ydif)/4.0),'imag')
    xlabel = Text(Point(xmax+(maxdif-xdif)/4.0,0),'real')
    for label in [orig,xlabel,ylabel]:
        label.setFill('white')
        label.setSize(8)
        label.draw(win)'''
        
    lastX,lastY = 0.0,0.0
    for i in range(len(x)):###draws the lines (real,imag)
        ###for even more broken down: draw (real,0), draw (0,imag)
        l = Line(Point(lastX,lastY),Point(lastX+x[i],lastY+y[i]))
        l.setFill('green')
        l.draw(win)
        lastX += x[i]
        lastY += y[i]
        
    ### labels the endpoint
    '''end = Text(Point(lastX,lastY),'('+\
               str(myRound(lastX,.0001))+', '+\
               str(myRound(lastY,.0001))+')')
    end.setFill('white')
    end.setSize(8)
    end.draw(win)'''

#inputs()
auto()


