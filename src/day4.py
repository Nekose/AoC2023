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