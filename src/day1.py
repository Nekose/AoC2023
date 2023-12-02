from src.tools import input_parser
def sumstripletters(a=str) -> str:
    forwarddict = {}
    reversedict = {}
    numlist = ["0","one", "two", "three", "four", "five", "six", "seven", "eight", "nine","1","2","3","4","5","6","7","8","9",]
    for value in numlist:
        position = a.find(value)
        if position >= 0:
            if value.isalpha():
                forwarddict[position] = numlist.index(value)
            else:
                forwarddict[position] = int(value)
        position = a.rfind(value)
        if position >= 0:
            if value.isalpha():
                reversedict[position] = numlist.index(value)
            else:
                reversedict[position] = int(value)
    return int(str(forwarddict[min(forwarddict)]) + str(reversedict[max(reversedict)]))

def process_values(datafile=list) -> int:
    data = input_parser(datafile)
    sumlist = []
    for row in data:
        sumlist.append(sumstripletters(row))
    return sum(sumlist)
