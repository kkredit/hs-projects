# nines.py
#  A program to play the card game nines.
# Aug 21, 2009
# Kevin Kredit

from ninesClasses import NinesGame

def main():
    nines = NinesGame(0.1,0.1,0.1)
    while True:
        over = nines.turn()
        if over: break
    nines.finish()

'''def main():
    r1 = input('Risk of player 1: ')
    r2 = input('Risk of player 2: ')
    r3 = input('Risk of player 3: ')
    num = input('Number of games simulated: ')
    p1wins = 0
    p2wins = 0
    p3wins = 0
    for i in range(num):
        nines = NinesGame(r1,r2,r3)
        while True:
            over = nines.turn()
            if over: break
        nines.finish()
        winner = nines.getWinner()
        if winner == 1:
            p1wins += 1
        elif winner == 2:
            p2wins += 1
        elif winner == 3:
            p3wins += 1
    print 'Player 1: ',p1wins
    print 'Player 2: ',p2wins
    print 'Player 3: ',p3wins'''
    
if __name__=='__main__': main()
