from src.day7 import Card
class Hand(object):

    def __init__(self,handstring) -> None:
        self.handlist = []
        for cardstr in handstring:
            self.handlist.append(Card.Card(cardstr))
    def __str__(self):
        return f"Hand containing: {str(self.handlist)}"

    def Score(self) -> int:
        self.handdict = {}
        for value in self.handlist:

        if len(set(self.handlist)) == 1:
            return 7
