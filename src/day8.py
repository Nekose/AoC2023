import itertools
from math import lcm
class Map(object):
    def __init__(self,rawdata):
        self.directiondict,self.turns = self.buildmap(rawdata)

    def buildmap(self,raw_data):
        mapdict = {}
        for pos,line in enumerate(raw_data):
            if pos == 0:
                directions = line
            elif pos == 1:
                continue
            else:
                #AAA = (BBB, CCC)
                equalsplit = line.split(" = ")
                #["AAA","(BBC, CCC)"
                name = equalsplit[0]
                left,right = equalsplit[1].strip('"').strip("(").strip(")").split(", ")
                mapdict[name] = [left,right]
        return mapdict,directions
    def start_ghost_walking(self,stoplocation="Z"):
        ghoststeps = []
        for location in self.directiondict.keys():
            if location[2] == "A":
                ghoststeps.append(self.start_walking(location,stoplocation))
        return lcm(*ghoststeps)



    def start_walking(self,startlocation="AAA",stoplocation="ZZZ"):
        currentstep = 0
        stepiterator = itertools.cycle(self.turns)
        currentlocation = startlocation
        for turn in stepiterator:
            if turn == "L":
                turn = 0
            elif turn == "R":
                turn = 1
            else:
                print("Turn step error")
                raise Exception
            if not currentlocation.endswith(stoplocation):
                currentstep += 1
                currentlocation = self.directiondict[currentlocation][turn]
            else:
                return currentstep


