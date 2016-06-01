# texasholdemCalculatorObjects.py
#       A supplementary program to provide classes for the program
#       texasholdemCalculator.py
# Kevin Kredit
# 7/10/10

class pokerPlayer:

    def __init__(self,window,pos,button,card1,card2):
        self.pos = pos
        self.window = window
        self.button = button
        self.card1 = card1
        self.card2 = card2

    def activatePlayer(self,lastPlayer,nextPlayer):
        lastPlayer.button.deactivate()
        nextPlayer.button.activate()
        self.card1.activate()
        self.card1.draw(window)
        self.card2.draw(window)

    def deactivatePlayer(self,lastPlayer,nextPlayer):
        if pos != 2:lastPlayer.button.activate()
        nextPlayer.button.deactivate()
        self.card1.deactivate()
        self.card1.undraw(window)
        self.card2.undraw(window)
