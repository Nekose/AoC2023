'''
Ready for AoC 2024!
'''

import src.tools as tools
import src.day7.Card as Card
import src.day7.Hand as Hand

card = Card.Card("K")
card2 = Card.Card("Q")
print(card != card2)
print(card > card2)
print(card < card2)
print(card == card2)

testhand = Hand.Hand("KKKKK")
print(testhand)