#This is a card arranging game but does
#not contain any ui.
import random

class person:
    def __init__(self,name):
        self.name = name
        self._card = None
        self.score = 0
    @property
    def card(self):
        return self._card.getClass()
    @card.setter
    def card(self,card):
        self._card = card
    def scoreCard(self):
        return self._card.getPriority()

players = [person("player1"),person("player2"),
           person("player3"),person("player4")]

deck = ["K","Q","J","10","9","8","7","6","5","4","3","2","A"]
suite = ["clubs","heart","spades","diamond"]

class gameManager:
    def __init__(self,cards):
        self._card = cards
        
    @property
    def cards(self):
        self.__displayCards()
    
    def __displayCards(self):
        for c in self._card:
            c.getClass()
            
    @cards.setter
    def cards(self,myTuple):
        try:
            deck,suite = myTuple
        except ValueError:
            raise ValueError("Please pass an iterable with two items")
        
        self._card.clear()
        for i,s in enumerate(suite):
            for j,d in enumerate(deck):
                self._card.append(myCards(d,s,i,j))
    def distributeCards(self):
        random.shuffle(self._card)
        for i in range(4):
            players[i].card = self._card[i]
    def scorePlayers(self):
        prioritised = list()
        for i in range(4):
            prioritised.append(players[i].scoreCard())
        prioritised = sorted(prioritised)
        
        for i in range(4):
            if prioritised[-1] == players[i].scoreCard():
                players[i].score+=1


class myCards:
    _Deck = [13,12,11,10,9,8,7,6,5,4,3,2,1]
    _Suite = [3,2,1,0]
    def __init__(self,deck,suite,i,j):
        self._deck = deck
        self._suite = suite
        self._priority = (self._Suite[i],self._Deck[j])
    def getClass(self):
        print(self._suite+" "+self._deck)
    def getPriority(self):
        return self._priority

play = True
while play:
    game = gameManager(list())
    game.cards = (deck,suite)
    game.cards
    game.distributeCards()
    print("..............")
    for i in players:
        i.card
    game.scorePlayers()
    for i in players:
        print(i.name,"-->",i.score)
    if "N" == str(input("Do you like to play again? ")).upper():
        exit()
        

