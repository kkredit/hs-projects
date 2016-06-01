# spiralPrimes.py
#   A program to draw numbers in a spiral and circle the primes
# Kevin Kredit
# 9/24/10

from graphics import *

def main():
    win = GraphWin('Spiral Primes',800,800)
    win.setCoords(0,0,800,800)
    win.setBackground('black')

    ###### set size to go up to here (width of the square)
    width = 261

    ''' You can easily adjust the settings to fit more numbers in, switch
        to circles instead of the actual numbers, or change the spacing'''

    primelist = []
    for x in iter_primes():
        if x > width**2: break
        primelist.append(x)
    
    turn = []
    num = 0
    for i in range(width):
        num += i
        turn.append(num)
        num += i
        turn.append(num)
    
    p = Point(400,400)
    direction = 2
    for num in range(1,width**2+1):
        #n = Text(p,num)
        ##n.setFill('red')##### uncomment this and move "n.draw(win)" back one tab to view non-prime numbers in red
        if num in primelist:
            #n.setFill('green')
            #n.setSize(5)
            #n.draw(win)
            ###### uncomment these and comment text ones to view primes as circles. This way it is easier to see the pattern
            s = Circle(p,1)
            s.setFill('green')
            s.draw(win)
        ###### Spaceing
        spacing = 3
        if direction == 0:
            p = Point(p.getX(),p.getY()+spacing)
        elif direction == 1:
            p = Point(p.getX()+spacing,p.getY())
        elif direction == 2:
            p = Point(p.getX(),p.getY()-spacing)
        elif direction == 3:
            p = Point(p.getX()-spacing,p.getY())
        if num in turn:
            if not direction: direction = 3
            else: direction -= 1

    dontclose = input()
        

        

def iter_primes ():        
        yield 2 # handle trivial case
        val = 1
        primesq_pairs = []
        while True:
                curr = None
                while (curr is None):
                        val += 2
                        curr = val
                        for prime, square in primesq_pairs:
                                if (curr < square):
                                        break
                                if (curr % prime == 0):
                                        curr = None
                                        break
                primesq_pairs.append ((curr, curr**2))
                yield curr

main()








































