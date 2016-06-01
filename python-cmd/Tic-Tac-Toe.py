# Tic-Tac-Toe.py
#   A tic-tac-toe playing program that learns from its mistakes.
# Kevin Kredit
import string
import random
import pickle

def main():
    fi = open("mem.dat","r")
    if fi.read() == '':
        fo = open("mem.dat","w")
        pickle.dump([],fo)
        fo.close()
    fi.close()
    player = input("\nHow many players are going to participate (0 or 1)?  ")    
    if not player:
        aiai()
    if player:
        huai()        
    again = raw_input("\nPlay again? (y/n)  ")# input(clear memory?)
    if again.lower() == "y":
        main()
    elif again.lower() == "n":
        fo = open("mem.dat","w")
        x = []
        pickle.dump(x,fo)
        fo.close()

def aiai():
    for i in range(input("How many simulations would you like to perform?  ")):
        # New game.
        aiboardX, aiboardO = [], []
        openboard, win = [1,2,3,4,5,6,7,8,9], 0
        while True:
            openboard,aiboardX,m = aimove(openboard,aiboardX,aiboardO)
            win, winner,won = awin(aiboardX,"\nPlayer X wins.",openboard,"h/x")
            if win:break
            openboard,aiboardO,m = aimove(openboard,aiboardO,aiboardX)
            win, winner,won = awin(aiboardO,"\nPlayer O wins.",openboard,"a/o")
            if win:break
            #print winner
        store(aiboardX,aiboardO,won)
        # End of game.

def huai():
    openboard, win = [1,2,3,4,5,6,7,8,9], 0
    huboard, aiboard = [], []
    xoro = raw_input("\nDo you want to play as X or O (X goes first)?  ")
    print
    # New game.
    if xoro.lower() == "o":
        openboard,aiboard,m = aimove(openboard,aiboard,huboard)
        print "My move:",m
    while True:
        openboard,huboard = humove(openboard,huboard)
        win, winner, won = awin(huboard,"\nYou win.",openboard,"h/x")
        if win:break
        openboard,aiboard,m = aimove(openboard,aiboard,huboard)
        print "My move:",m
        win, winner, won = awin(aiboard,"\nI win.",openboard,"a/o")
        if win:break
    # End of Game.
    print winner
    store(huboard,aiboard,won)
    for i in range(0):
        aiai()

def store(hxboard,aoboard,winner):
    if winner == "a/o":
        aoboard.append(2)
        hxboard.append(0)
    elif winner == "h/x":
        aoboard.append(0)
        hxboard.append(2)
    elif winner == "tie":
        aoboard.append(1)
        hxboard.append(1)
    fi = open("mem.dat","r")
    bigmem = pickle.load(fi)
    fi.close()
    otherx, othero = mult(hxboard,aoboard)
    counter, go = 0, 1
    for i in range(8):
        if bigmem.count(otherx[counter]) \
           and bigmem.count(othero[counter]):
            go = 0
            break
        counter = counter + 1
    if go:
        fi = open("mem.dat","r")
        bigmem = pickle.load(fi)
        fi.close()
        bigmem.append(hxboard)
        bigmem.append(aoboard)
        fo = open("mem.dat","w")
        pickle.dump(bigmem,fo)
        fo.close()
    
def humove(openboard,huboard):
    m = input("Where would you like to move?  ")
    try:
        openboard.remove(m)        
    except ValueError:
        print "\nPlease choose a valid place.\n"
        humove(openboard,huboard)
    huboard.append(m)
    return(openboard,huboard)

def aimove(openboard,my,their):
    acceptable = openboard
    if my != []:#make it so that i don't need this "if my != []"
        nogo, dogo = recall(my,their)
        if nogo:
            counter = 0
            for i in range(len(nogo)):
                print counter, nogo, my, acceptable, their
                acceptable.remove(nogo[counter])
                counter = counter + 1
        if dogo:
            acceptable = dogo
    y = random.randrange(0,len(acceptable))
    m = openboard.pop(y)
    my.append(m)
    return openboard,my,m

def recall(my,their):
    won, lasttimes, nogo, dogo = [], [], [], []
    infile = open("mem.dat","r")
    bigmem = pickle.load(infile)
    infile.close()    
    otherx, othero = mult(my,their)
    counter = 0
    for i in range(8):
        my, their = otherx[counter], othero[counter]
        for i in range(str(bigmem).count(str(my)[0:len(str(my))-1])):
            part = str(bigmem).split(str(my)[0:len(str(my))-1])
            if len(part)>1:
                index = part[0].count("[")-1
                won = bigmem[index][len(bigmem[index])-1]
                win, thing = -1, -1
                if index/2 == index/2.0:
                    win, thing = 1, 0
                if str(bigmem[index+win]).count(str(their)[0:len(str(their))-1]):
                    if won == 0:
                        if bigmem[index][len(my)] == 0:
                            dogo.append(bigmem[index+win][len(bigmem[index+win])-1])
                            dogo = fix(dogo,counter)
                        else:
                            nogo.append(bigmem[index][len(my)])
                            nogo = fix(nogo,counter)
                    elif won == 2:
                        dogo = [bigmem[index][len(my)]]
                        dogo = fix(dogo,counter)
                        return [], dogo
                    elif won == 1:
                        dogo.append(bigmem[index][len(my)])
                        dogo = fix(dogo,counter)
                    lasttimes.append(bigmem[index+thing])
                    lasttimes.append(bigmem[index+thing])
                    bigmem.remove(bigmem[index+thing])
                    bigmem.remove(bigmem[index+thing])
        counter = counter + 1
    return nogo, dogo

def fix(board,counter):
    if (4 - counter + abs(4 - counter)):
        for i in range(4-counter):
            board = map(rotfun,board)
        return board
    else:
        board = map(mirfun,board)
        counter = counter - 4
        fix(board,counter)

def mult(n,b):
    nflip = map(mirfun,n)
    nn90,nn180,nn270 = rotate(n)
    nf90,nf180,nf270 = rotate(nflip)
    bflip = map(mirfun,b)
    bn90,bn180,bn270 = rotate(b)
    bf90,bf180,bf270 = rotate(bflip)
    return [n,nn90,nn180,nn270,nflip,nf90,nf180,nf270], \
           [b,bn90,bn180,bn270,bflip,bf90,bf180,bf270]

def rotate(n):
    n90 = map(rotfun,n)
    n180 = map(rotfun,n90)
    n270 = map(rotfun,n180)
    return n90,n180,n270

def rotfun(n):
    return -3*n+10*int(n/3.1)+10

def mirfun(n):
    return 3*n-8*int(n/3.1)-2

def awin(b,text,o,winner):
    if b.count(1) and b.count(2) and b.count(3) or \
    b.count(4) and b.count(5) and b.count(6) or \
    b.count(7) and b.count(8) and b.count(9) or \
    b.count(1) and b.count(4) and b.count(7) or \
    b.count(2) and b.count(5) and b.count(8) or \
    b.count(3) and b.count(6) and b.count(9) or \
    b.count(1) and b.count(5) and b.count(9) or \
    b.count(3) and b.count(5) and b.count(7):
        return 1,text,winner
    elif o == []:
        return 1,"\nThe game was a tie.","tie"
    else:
        return 0,"",""

main()
