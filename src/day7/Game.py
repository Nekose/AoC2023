from src.day7 import Hand
from src.tools import input_parser
rawdata = input_parser(r"C:\Users\nekos\PycharmProjects\AoC2024\data\day7.txt")
game = []
for line in rawdata:
    hand,wager = line.split()
    game.append(Hand.Hand(hand,wager,True))

game.sort(key=Hand.Hand.score)

final_score = 0
for rank,hand in enumerate(game):
    hand.winnings(rank + 1)
    final_score += hand.wager

print(final_score)
