# ninesClasses.py
#   A library to support the program nines.py
# Aug 21, 2009
# Kevin Kredit

def points(board):
    '''returns score of any amount of cards'''
    if type(board) == str: board = [board]
    cards = board[:]
    if len(cards) == 9:
        col1 = [cards[0],cards[3],cards[6]]
        col2 = [cards[1],cards[4],cards[7]]
        col3 = [cards[2],cards[5],cards[8]]
        if col1[0] == col1[1] and col1[1] == col1[2]:
            cards[0] = 'K'
            cards[3] = 'K'
            cards[6] = 'K'
        if col2[0] == col2[1] and col2[1] == col2[2]:
            cards[1] = 'K'
            cards[4] = 'K'
            cards[7] = 'K'
        if col3[0] == col3[1] and col3[1] == col3[2]:
            cards[2] = 'K'
            cards[5] = 'K'
            cards[8] = 'K'
    point = ['Q','','K','A','2','3','4','5','6','7','8','9','10','J']
    score = 0
    for card in cards:
        score += point.index(card)-2
    return score

def columnCheck(board,column):
    '''returns the value of an empty space if valid, False if not valid'''
    #column = column%3
    col = [board[0+column],board[3+column],board[6+column]]
    if col.count('') < 2: return False
    from random import random
    if random() < 0.5: return col.index('')*3+column
    return col.index('',col.index('')+1)*3+column

def ace(board,last,risk):
    '''Returns where to put the ace, or False if no good spot'''
    col = [board[2],board[5],board[8]]
    if '' in col: return col.index('')*3+2
    return bestSpot(board,'A',last,risk)

def king(board,last,risk):
    '''Returns where to put the king, or False if no good spot'''
    col = [board[2],board[5],board[8]]
    if '' in col: return col.index('')*3+2
    if 'A' in col: return col.index('A')*3+2
    return bestSpot(board,'K',last,risk)

def queen(board,last,risk):
    '''Returns where to put the queen, or False if no good spot'''
    col = [board[2],board[5],board[8]]
    if 2-col.count('Q'):
        if '' in col: return col.index('')*3+2
        elif 'A' in col and (col.count('A')+col.count('K') > 1):
            return col.index('A')*3+2
        elif col.count('K') > 1: return col.index('K')*3+2
    return bestSpot(board,'Q',last,risk)

def bestSpot(board,card,last,risk):
    '''Returns the best spot for a card not in row 3, of False if none'''
    col = [[board[0],board[3],board[6]],[board[1],board[4],board[7]]]
    best = False
    highest = -5
    for j in [0,1]:
        if not last and col[j][0]!=col[j][1] and col[j][0]!=col[j][2] and col[j][1]!=col[j][2]:
            for i in [0,1,2]:
                if col[j][i] != '':
                    score = points(col[j][i])
                    if score > highest and score > points(card):
                        highest = score
                        best = i*3+j
        if last:
            if col[j][0]!=col[j][1] and col[j][0]!=col[j][2] and col[j][1]!=col[j][2]:
                for i in [0,1,2]:
                    if col[j][i] != '':
                        score = points(col[j][i])
                        if score > highest and score > points(card):
                            highest = score
                            best = i*3+j
                if not best and '' in col[j] and points(card) < 4:
                    best = col[j].index('')*3+j
                    highest = 11-points(card)#########
            elif not col[j][0]==col[j][1]==col[j][2]:#if 2 same
                from random import random
                rand = random()
                for i in [0,1,2]:
                    if col[j][i] != '':
                        score = points(col[j][i])
                        if score > highest and rand >= risk and score > points(card):
                            highest = score
                            best = i*3+j
                if not best and '' in col[j] and points(card) < 4 and rand >= risk:
                    best = col[j].index('')*3+j
                    highest = 11-points(card)#########
    return best

class Deck:

    def __init__(self):
        self.cards = ['Q','K','A','2','3','4','5','6','7','8','9','10','J']*12

    def shuffle(self):
        '''shuffles the deck'''
        from random import randrange
        newdeck = []
        while self.cards:
            newdeck.append(self.cards.pop(randrange(0,len(self.cards))))
        self.cards = newdeck

    def deal(self,num):
        '''deals any number of cards'''
        dealt = []
        for i in range(num):
            dealt.append(self.cards.pop(0))
        return dealt

    def getDeck(self):
        '''returns the deck'''
        return self.cards

    def setNext(self,card):
        self.cards[0] = card

class aiPlayer:# under construction

    def __init__(self,risk,deck,pnum,board=False):
        self.pnum = pnum
        self.risk = risk
        if not board:
            self.hidden = deck.deal(9)
            self.deck = deck
            self.real = self.hidden[:2]
            for i in range(7):
                self.real.append('')
        else:
            self.real = board
            self.hidden = ['2','2','2','2','2','2','2','2','2']

    def getDeck(self):
        '''only for use after creating the aiPlayer'''
        return self.deck

    def turn(self,last,dealt,deck):
        '''returns the new face up draw pile card and the changed deck'''
        card,deck = self.what(dealt,deck,last)
        if type(card)==list: card = card[0]
        index = self.where(card,last)
        if type(index) != int: return card,deck
        dealt = self.real[index] or self.hidden[index]
        self.real[index] = card
        return dealt,deck

    def over(self):
        if '' not in self.real: return True
        return False

    def what(self,dealt,deck,last):
        '''returns teh chosen card and changed deck'''
        spec = False
        if dealt == 'A': spec = ace(self.real,last,self.risk)
        elif dealt == 'K': spec = king(self.real,last,self.risk)
        elif dealt == 'Q': spec = queen(self.real,last,self.risk)
        if 1 <= self.real.count(dealt) <= 2 or type(spec) == int:
            return dealt,deck
        card = deck.deal(1)[0]
        print 'drew:',card,'\n'
        return card,deck

    def where(self,card,last):
        '''returns where to place the chosen card'''
        #from random import randrange
        if type(card) == list: card = card[0]
        if card == 'K': return king(self.real,last,self.risk)
        elif card == 'Q': return queen(self.real,last,self.risk)
        elif card in self.real:
            column = self.real.index(card)%3
            while column <= 8:
                if self.real[column] != card and self.real[column] != '':
                    return column
                column += 3
            column = self.real.index(card)%3
            while column <= 8:
                if self.real[column] == '':
                    return column
                column += 3
            return False
        elif card == 'A': return ace(self.real,last,self.risk)
        else:#elif card not in self.real
            for i in range(2):
                check = columnCheck(self.real,i)
                if type(check) == int:
                    return check
            return bestSpot(self.real,card,last,self.risk)#index

    def finish(self):
        '''flips over leftover cards and returns score'''
        for i in range(9):
            if self.real[i] == '':
                self.real[i] = self.hidden[i]
        return points(self.real)

    def getBoard(self):
        return self.real

    def getPnum(self):
        return self.pnum

class NinesGame:

    def __init__(self,aiRisk,aiRisk2=False,aiRisk3=False):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        pnum = 1
        for risk in [aiRisk,aiRisk2,aiRisk3]:
            if type(risk) == float:
                player = aiPlayer(risk,self.deck,pnum)
                self.players.append(player)
                self.deck = player.getDeck()
                pnum += 1
        self.dealt = self.deck.deal(1)[0]
        #self.gui = NinesGUI(##########
        self.unhand = self.deck.deal(9)
        self.realhand = [self.unhand[0],self.unhand[1],'','','','','','','']

    def turn(self):
        '''does one round of play and returns whether or not anyone finished'''
        over = False
        for player in self.players:
            b = player.getBoard()
            print b[0] or '?',b[1] or '?',b[2] or '?'
            print b[3] or '?',b[4] or '?',b[5] or '?'
            print b[6] or '?',b[7] or '?',b[8] or '?'
            print
            print 'draw pile:',self.dealt,'\n'
            #g = raw_input()
            self.dealt,self.deck = player.turn(over,self.dealt,self.deck)
            b = player.getBoard()
            print b[0] or '?',b[1] or '?',b[2] or '?'
            print b[3] or '?',b[4] or '?',b[5] or '?'
            print b[6] or '?',b[7] or '?',b[8] or '?'
            print
            print 'discard:',self.dealt,'\n'
            #g = raw_input()
            if player.over():
                over = True
                self.finisher = player
        #############################################
        '''def turn(self,last,dealt,deck):
        card,deck = self.what(dealt,deck,last)
        if type(card)==list: card = card[0]
        index = self.where(card,last)
        if type(index) != int: return card,deck
        dealt = self.real[index] or self.hidden[index]
        self.real[index] = card
        return dealt,deck'''
        print
        print 'Your board'
        print self.realhand[0] or '?',self.realhand[1] or '?',self.realhand[2] or '?'
        print self.realhand[3] or '?',self.realhand[4] or '?',self.realhand[5] or '?'
        print self.realhand[6] or '?',self.realhand[7] or '?',self.realhand[8] or '?'
        print '\nDraw pile:',self.dealt
        if raw_input('Take card? ')[0] == 'y':
            card = self.dealt
        else:
            card = self.deck.deal(1)[0]
            print 'Card drawn:',card
        where = input('\nWhere do you wnat ot place the card (9 for discard)? ')
        if where == 9:
            self.dealt = card
        else:
            self.realhand[where] = card
            self.dealt = self.realhand[where] or self.unhand[where]
        if '' not in self.realhand:
            over = True
            self.finisher = 'human'
            ###############################################
        return over

    def finish(self):
        for player in self.players:
            if player == self.finisher: break
            b = player.getBoard()
            print b[0] or '?',b[1] or '?',b[2] or '?'
            print b[3] or '?',b[4] or '?',b[5] or '?'
            print b[6] or '?',b[7] or '?',b[8] or '?'
            print
            print self.dealt
            print
            self.dealt,self.deck = player.turn(True,self.dealt,self.deck)
            b = player.getBoard()
            print b[0] or '?',b[1] or '?',b[2] or '?'
            print b[3] or '?',b[4] or '?',b[5] or '?'
            print b[6] or '?',b[7] or '?',b[8] or '?'
            print
            ##########################
        if self.finisher != 'human':
            print
            print 'Your board'
            print self.realhand[0] or '?',self.realhand[1] or '?',self.realhand[2] or '?'
            print self.realhand[3] or '?',self.realhand[4] or '?',self.realhand[5] or '?'
            print self.realhand[6] or '?',self.realhand[7] or '?',self.realhand[8] or '?'
            print '\nDraw pile:',self.dealt
            if raw_input('Take card? ')[0] == 'y':
                card = self.dealt
            else:
                card = self.deck.deal(1)[0]
                print 'Card drawn:',card
            where = input('\nWhere do you wnat ot place the card (9 for discard)? ')
            if where == 9:
                self.dealt = card
            else:
                self.realhand[where] = card
                self.dealt = self.realhand[where] or self.unhand[where]
                ##########################
        best = 127
        for player in self.players:
            print 'Player:',player.getPnum()
            print
            score = player.finish()
            print 'score:',score
            if score < best:
                best = score
                self.winner = player.getPnum()
            print
            b = player.getBoard()
            print b[0] or '?',b[1] or '?',b[2] or '?'
            print b[3] or '?',b[4] or '?',b[5] or '?'
            print b[6] or '?',b[7] or '?',b[8] or '?'
            print
        ###################################
        print 'You:'
        for i in range(9):
            if self.realhand[i] == '':
                self.realhand[i] = self.unhand[i]
        print '\nScore:',points(self.realhand)
        print self.realhand[0] or '?',self.realhand[1] or '?',self.realhand[2] or '?'
        print self.realhand[3] or '?',self.realhand[4] or '?',self.realhand[5] or '?'
        print self.realhand[6] or '?',self.realhand[7] or '?',self.realhand[8] or '?'
        print
        ########################################
        print self.winner

    def getWinner(self):
        return self.winner

class NinesGUI:#######480h*320w

    def __init__(self,sizex,sizey,d,board1,board2,board3=False,board4=False):
        from graphics import GraphWin
        win = GraphWin('Nines',sizex,sizey)
        win.setCoords(0,0,sizex,sizey)
        self.sizex = sizex
        self.sizey = sizey
        self.dealt = d
        self.boards = [board1,board2,board3,board4]
        while False in boards:
            self.boards.remove(False)
        self.update()

def test():
    board = input('Board: ')
    draw = raw_input('Draw: ')
    deal = raw_input('Deal: ')
    last = bool(raw_input('Last: '))
    risk = input('Risk: ')
    deck = Deck()
    deck.setNext(deal)
    player = aiPlayer(risk,deck,1,board)
    player.turn(last,draw,deck)
    b = player.getBoard()
    print
    print b[0]or '?',b[1] or '?',b[2] or '?'
    print b[3]or '?',b[4] or '?',b[5] or '?'
    print b[6]or '?',b[7] or '?',b[8] or '?'
    
if __name__=='__main__': test()
