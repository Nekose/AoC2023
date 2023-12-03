from src.tools import input_parser

def import_data(datafile: str) -> list:
    returndata = []
    rawdata = input_parser(datafile)
    for row in rawdata:
        gamedata = row.split(": ")[1]
        rounds = gamedata.split("; ")
        returndata.append(rounds)
    return returndata

def check_game(numred: int, numgreen: int, numblue: int,gamedata: list) -> int:
    invalidgames = set()
    answerdict = {"red":numred, "green":numgreen, "blue":numblue}
    for gamenum,data in enumerate(gamedata):
        for rounds in data:
            round = rounds.split(", ")
                #split into draws
            for draw in round:
                num,color = draw.split(" ")
                if int(num) > answerdict[color]:
                    invalidgames.add(gamenum+1)
    totalsum = sum(x for x in range(len(gamedata)+1))
    return totalsum - sum(invalidgames)

def find_min_valid_game(gamedata: list) -> int:
    powers = []
    for game in gamedata:
        cubedict = {"red": 0, "green": 0, "blue": 0}
        for rounds in game:
            round = rounds.split(", ")
            for draw in round:
                num, color = draw.split(" ")
                num = int(num)
                if num > cubedict[color]:
                    cubedict[color] = num
        powers.append(cubedict["red"]*cubedict["blue"]*cubedict["green"])

    print(powers)
    return sum(powers)