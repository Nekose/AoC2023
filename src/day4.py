from typing import Tuple
def score_card(card_data: str) -> Tuple[list,list]:
    stripname = card_data.split(": ")[1]
    winnum,checknum = stripname.split(" | ")
    winnumlist = winnum.split()
    checknumlist = checknum.split()
    scored = set([int(x) for x in winnumlist]).intersection(set([int(y) for y in checknumlist]))
    if len(scored) > 0:
        return 1 * 2**(len(scored) - 1)
    else:
        return 0

def score_scratchers(cardlist: list) -> int:
    total = 0
    for card in cardlist:
        total += parse_card(card)
    return total

def process_scratchers(cardlist: list) -> int:
    stack = []
    for card in cardlist:
        stripname = card.split(": ")[1]
        winnum,checknum = stripname.split(" | ")
        winnumlist = winnum.split()
        checknumlist = checknum.split()
        stack.append([winnumlist,checknumlist,1])
    return(stack)

def calculate_total_scratchers(cards: list) -> int:
    cardlist = process_scratchers(cards)
    for number,card in enumerate(cardlist):
        score = len([value for value in card[0] if value in card[1]])
        if score > 0:
            for i in range(card[2]):
                for j in range(score):
                    cardlist[number+j+1][2] += 1
    return sum(x[2] for x in cardlist)
