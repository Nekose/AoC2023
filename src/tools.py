def input_parser(file=str) -> list:
    returnlist = []
    with open(file) as data:
        for line in data:
            returnlist.append(line.strip("\n"))
    return returnlist
