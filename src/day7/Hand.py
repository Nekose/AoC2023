from src.day7 import Card
class Hand(object):

    def __init__(self,handstring,wager,day2 = False) -> None:
        self.wager = int(wager)
        self.handlist = []
        self.day2 = day2

        for cardstr in handstring:
            self.handlist.append(Card.Card(cardstr,day2))

    def __repr__(self):
        return f"Hand containing: {str(self.handlist)} and wager of {self.wager}"
    def score(self) -> int:
        countlist = []
        rawcardscores = "".join([str(card.value).zfill(2) for card in self.handlist])
        handset = set(self.handlist)
        jackcount = 0
        testjack = Card.Card("J", True)
        for value in handset:
            if self.day2:
                if value == testjack:
                    jackcount = self.handlist.count(value)
                else:
                    countlist.append(self.handlist.count(value))
            else:
                countlist.append(self.handlist.count(value))
        countlist.sort(reverse=True)
        if self.day2:
            if len(countlist) == 0:
                countlist = [5]
            else:
                countlist[0] += jackcount
        if countlist == [5]:
            return int("7" + rawcardscores)  # 5 of a kind
        elif countlist == [4,1]:
            return int("6" + rawcardscores) #four of a kind
        elif countlist == [3,2]:
            return int("5" + rawcardscores) #full house
        elif countlist == [3,1,1]:
            return int("4" + rawcardscores) #three of a kind
        elif countlist == [2,2,1]:
            return int("3" + rawcardscores) #two pair
        elif countlist == [2,1,1,1]:
            return int("2" + rawcardscores)  # pair
        elif countlist == [1,1,1,1,1]:
            return int("1" + rawcardscores)  # high card
        else:
            print("Card Scoring Error")
            print(self.handlist,countlist)
            raise Exception
        #DAY 2


    def winnings(self,rank):
        self.wager *= rank


