# texasholdemDeluxeCalculator.py
#       A deluxe graphical program to determine the odds of having
#        a winning hand in Texas Hold'em Poker
# Kevin Kredit
# 7/15/10

from graphics import *
from texasholdemHandCalculator import *

def main():
    window,allButtons,deck = initWindow()
    handleInput(window,allButtons,deck)

def handleInput(window,allButtons,deck):
    # allButtons = [players,cards,numbers,suits,[calculateButton]]
    cCancel,nCancel = [],[]
    while True:
        if allButtons[1][8].getLabel() != '?' and \
           allButtons[1][9].getLabel() != '?': allButtons[4][0].activate()
        click = window.getMouse()
        n = -1
        found = False
        for buttonType in allButtons:
            if found: break
            n += 1
            x = -1
            for button in buttonType:
                x += 1
                if button.clicked(click):
                    if n == 0:
                        allButtons = addPlayer(allButtons,x)
                        found = True
                        break
                    if n == 1:
                        allButtons,cCancel = initSelectCard\
                                             (allButtons,cCancel,x,deck)                       
                        found = True
                        break
                    if n == 2:
                        allButtons,nCancel = selectNumber\
                                             (allButtons,nCancel,x,deck)
                        selectedNumx = x
                        selectedNum = 'A234567891JQKA'[x]
                        if selectedNum == '1': selectedNum = '10'
                        found = True
                        break
                    if n == 3:
                        allButtons,oldCard = selectSuit\
                                     (allButtons,cCancel,selectedNum,x)
                        selectedSuit = 'SCDH'[x]
                        deck[x][selectedNumx] = 'x'
                        if oldCard != '?':
                            deck['SCHD'.index(oldCard[len(oldCard)-1])]['A234567891JQK'.index(oldCard[0])] = oldCard[:len(oldCard)-1]
                            print deck
                        found = True
                        break
                    if n == 4:#bookmark
                        calculate_buttons_deck(allButtons,deck)
                        found = True
                        break

def addPlayer(allButtons,num):
    # allButtons = [players,cards,numbers,suits,[calculateButton]]
    players = allButtons[0]
    cards = allButtons[1]
    if not cards[2*num+8].isActive():# add new player
        players[num-1].deactivate()
        if num != 7: players[num+1].activate()
        cards[2*num+8].activate()
        cards[2*num+8].draw()
        cards[2*num+9].draw()
        return allButtons
    else:# remove current player
        if num != 2: players[num-1].activate()
        if num != 7: players[num+1].deactivate()
        cards[2*num+8].deactivate()
        cards[2*num+9].deactivate()
        cards[2*num+8].undraw()
        cards[2*num+9].undraw()
        return allButtons

def initSelectCard(allButtons,cCancel,num,deck):
    # allButtons = [players,cards,numbers,suits,[calculateButton]]
    if not allButtons[2][0].isActive()\
       and not allButtons[3][0].isActive():# if selecting a card
        cCancel = [[],[],[],[],[]]
        n = -1
        for buttonType in allButtons:
            n += 1
            x = -1
            for button in buttonType:
                x += 1
                active = False
                if button.isActive(): active = True
                cCancel[n].append(active)
                if n == 2:
                    cNum = 'A234567891JQKA'[x]
                    if cNum == '1': cNum = '10'
                    if cNum in deck[0] or cNum in deck[1] or \
                       cNum in deck[2] or cNum in deck[3]: button.activate()
                else: button.deactivate()
                if n == 1 and x == num: button.activate()
        return allButtons,cCancel
    else:# if un-selecting a card
        n = -1
        for buttonType in allButtons:
            n += 1
            x = -1
            for button in buttonType:
                x += 1
                if cCancel[n][x]: button.activate()
                else: button.deactivate()
        return allButtons,cCancel

def selectNumber(allButtons,nCancel,num,deck):
    # allButtons = [players,cards,numbers,suits,[calculateButton]]
    cNum = 'A234567891JQKA'[num]
    if cNum == '1': cNum = '10'
    if not allButtons[3][0].isActive():# if selecting a number
        nCancel = [[],[],[],[],[]]
        n = -1
        for buttonType in allButtons:
            n += 1
            x = -1
            for button in buttonType:
                x += 1
                active = False
                if button.isActive(): active = True
                nCancel[n].append(active)
                if n == 2 and x != num: button.deactivate()
                if n == 3 and cNum in deck[x]: button.activate()
        return allButtons,nCancel
    else:# if un-selecting a number
        n = -1
        for buttonType in allButtons:
            n += 1
            x = -1
            for button in buttonType:
                x += 1
                if nCancel[n][x]: button.activate()
                else: button.deactivate()
        return allButtons,nCancel

def selectSuit(allButtons,cCancel,selectedNum,num):
    # allButtons = [players,cards,numbers,suits,[calculateButton]]
    n = -1
    for buttonType in allButtons:
        n += 1
        x = -1
        for button in buttonType:
            x += 1
            if n == 1 and button.isActive():
                oldCard = button.getLabel()
                button.setLabel(selectedNum+'\n'+'SCDH'[num])
                cButton = x
            if cCancel[n][x]: button.activate()
            else: button.deactivate()
    if cButton != 2 and cButton != 11 and cButton != 13 and \
       cButton != 15 and cButton != 17 and cButton != 19 and \
       cButton != 21 and cButton != 23 and cButton != 25:
        allButtons[1][cButton+1].activate()
    return allButtons,oldCard

def initWindow():
    window = GraphWin("Texas Hold'em Hand Calculator",600,400)
    window.setCoords(0,0,600,400)
    window.setBackground('green4')
    
    p1 = Button_Circle(window,Point(50,200),35,'Player\nOne')
    p2 = Button_Circle(window,Point(105,260),35,'Player\nTwo')
    p3 = Button_Circle(window,Point(175,300),35,'Player\nThree')
    p4 = Button_Circle(window,Point(255,325),35,'Player\nFour')
    p5 = Button_Circle(window,Point(345,325),35,'Player\nFive')
    p6 = Button_Circle(window,Point(425,300),35,'Player\nSix')
    p7 = Button_Circle(window,Point(495,260),35,'Player\nSeven')
    p8 = Button_Circle(window,Point(550,200),35,'Player\nEight')
    players = [p1,p2,p3,p4,p5,p6,p7,p8]
    players[2].activate()
    
    Text(Point(50,360),'Revealed\nCards:').draw(window)
    Text(Point(300,185),'          Flop            Turn  River').draw(window)
    c1 = Button(window,Point(105,360),25,38,'?')#revealed1
    c2 = Button(window,Point(140,360),25,38,'?')#revealed2
    c3 = Button(window,Point(175,360),25,38,'?')#revealed3
    c4 = Button(window,Point(220,150),25,38,'?')#flop1
    c5 = Button(window,Point(260,150),25,38,'?')#flop2
    c6 = Button(window,Point(300,150),25,38,'?')#flop3
    c7 = Button(window,Point(340,150),25,38,'?')#turn
    c8 = Button(window,Point(380,150),25,38,'?')#river
    c9 = Button(window,Point(85,145),25,38,'?')#########p1 c1
    c10 = Button(window,Point(115,145),25,38,'?')#######p1 c2
    c11 = Button(window,Point(115,200),25,38,'?')#######p2 c1
    c12 = Button(window,Point(145,200),25,38,'?')#######p2 c2
    c13 = Button(window,Point(175,240),25,38,'?',False)#p3 c1
    c14 = Button(window,Point(205,240),25,38,'?',False)#p3 c2
    c15 = Button(window,Point(245,265),25,38,'?',False)#p4 c1
    c16 = Button(window,Point(275,265),25,38,'?',False)#p4 c2
    c17 = Button(window,Point(325,265),25,38,'?',False)#p5 c1
    c18 = Button(window,Point(355,265),25,38,'?',False)#p5 c2
    c19 = Button(window,Point(395,240),25,38,'?',False)#p6 c1
    c20 = Button(window,Point(425,240),25,38,'?',False)#p6 c2
    c21 = Button(window,Point(455,200),25,38,'?',False)#p7 c1
    c22 = Button(window,Point(485,200),25,38,'?',False)#p7 c2
    c23 = Button(window,Point(485,145),25,38,'?',False)#p8 c1
    c24 = Button(window,Point(515,145),25,38,'?',False)#p8 c2
    cards = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,\
             c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24]
    
    for card in cards:
        card.setFill('white')
    for card in [0,3,8,10]:
        cards[card].activate()
        
    nA = Button(window,Point(30,70),25,38,'A')
    n2 = Button(window,Point(65,70),25,38,'2')
    n3 = Button(window,Point(100,70),25,38,'3')
    n4 = Button(window,Point(135,70),25,38,'4')
    n5 = Button(window,Point(170,70),25,38,'5')
    n6 = Button(window,Point(205,70),25,38,'6')
    n7 = Button(window,Point(240,70),25,38,'7')
    n8 = Button(window,Point(275,70),25,38,'8')
    n9 = Button(window,Point(310,70),25,38,'9')
    n10 = Button(window,Point(345,70),25,38,'10')
    nJ = Button(window,Point(380,70),25,38,'J')
    nQ = Button(window,Point(415,70),25,38,'Q')
    nK = Button(window,Point(450,70),25,38,'K')
    numbers = [nA,n2,n3,n4,n5,n6,n7,n8,n9,n10,nJ,nQ,nK]
    for number in numbers:
        number.setFill('white')
        
    sS = Button(window,Point(58,25),80,38,'Spades')
    sC = Button(window,Point(158,25),80,35,'Clubs')
    sD = Button(window,Point(258,25),80,35,'Diamonds')
    sH = Button(window,Point(358,25),80,35,'Hearts')
    suits = [sS,sC,sD,sH]
    
    calculateButton = Button(window,Point(530,350),90,50,'Calculate')

    deck = [['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
            ['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
            ['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
            ['A','2','3','4','5','6','7','8','9','10','J','Q','K']]
                                                          
    return window,[players,cards,numbers,suits,[calculateButton]],deck

main()
