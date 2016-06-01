# mastermind.py
#       A program to simulate the game 'mastermind'
# Kevin Kredit
# 8/24/10

def main():
    solution,ngame,cbuttons,pegButtons,win = initBoard()
    colors = ['red','yellow','green','blue','white','black']
    won = False
    cSelceted = None
    while not won:
        while True:
            click = win.getMouse()
            for i in range(6):
                if cbuttons[i].clicked(click):
                    if cSelected == i: cSelected = None
                    else: cSelected = i
                
    
    input()

def initBoard():
    from graphics import *
    win = GraphWin('Mastermind',500,800)
    win.setBackground('dark green')
    win.setCoords(0,0,10,16)
    board = Rectangle(Point(2.5,2),Point(8.5,15))
    board.setFill('grey')
    cover = Rectangle(Point(4,13.5),Point(8,14.5))
    cover.setFill('dark grey')
    label = Text(Point(5.75,14),'Secret\nCode')
    for obj in [board,cover,label]:
        obj.draw(win)
        
    gpegs = [4.5,5.5,6.5,7.5]
    pegButtons = []
    for i in range(3,14):
        for j in range(4):
            dot = Button(win,Point(gpegs[j],i),.1,.1,'',True,'black')
            dot.activate()
            pegButtons.append(dot)
    apegsx = [3.3,3.7]
    apegsy = [-.2,.2]
    for i in range(3,14):
        for j in range(2):
            for k in range(2):
                dot = Circle(Point(apegsx[k],i+apegsy[j]),.05)
                dot.setFill('black')
                dot.draw(win)

    from random import random
    a1 = int(6*random())
    a2 = int(6*random())
    a3 = int(6*random())
    a4 = int(6*random())
    nums = [a1,a2,a3,a4]
    solution = []
    for i in range(4):
        solution.append(nums[int((4-i)*random())])

    ngame = Button(win,Point(2,1),2,1,'New Game')
    ngame.activate()

    colors = ['red','yellow','green','blue','white','black']
    yvals = [14,12.5,11,9.5,8,6.5]
    cbuttons = []
    for i in range(6):
        cbutton = Button(win,Point(1,yvals[i]),.5,.5,'')
        cbutton.setFill(colors[i])
        cbutton.activate()
        cbuttons.append(cbutton)

    return solution,ngame,cbuttons,pegButtons,win       
            
main()
