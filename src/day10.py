class pipenode(object):
    def __init__(self,pipestr: str,ypos: int, xpos: int) -> None:
        self.pipestr = pipestr
        pipedict = {"|": "NS","-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE"}
        self.ypos = ypos
        self.xpos = xpos
        if pipestr == ".":
            self.connections = [None,None]
        elif pipestr == "S":
            self.connections = []
        else:
            self.directions = pipedict[pipestr][0], pipedict[pipestr][1]
            self.connections = []
            for dir in self.directions:
                if dir == "N":
                    self.connections.append([self.ypos - 1, self.xpos])
                if dir == "S":
                    self.connections.append([self.ypos + 1, self.xpos])
                if dir == "E":
                    self.connections.append([self.ypos, self.xpos + 1])
                if dir == "W":
                    self.connections.append([self.ypos, self.xpos - 1])


    def __repr__(self):
        if self.pipestr == "S":
            print("start spot")
        return f"A '{self.pipestr}' pipe at Y={self.ypos},X={self.xpos}, connecting {self.connections[0]} and {self.connections[1]}"

class Map(object):
    def __init__(self,maplist):
        self.rawmaplist = maplist
        self.map = []
        self.visitmatrix = []
        for line in maplist:
            self.visitmatrix.append([0 for _ in line])
        for ypos,row in enumerate(maplist):
            newrow = []
            for xpos,node in enumerate(row):
                newrow.append(pipenode(node,ypos,xpos))
                if node == "S":
                    self.start = [ypos,xpos]
            self.map.append(newrow)
        #TODO determine start connections
        for y in range(-1, 2, 1):
            for x in range(-1, 2, 1):
                ycheck = self.start[0] + y
                xcheck = self.start[1] + x
                if self.is_in_grid(ycheck,xcheck):
                    currentnode = self.map[ycheck][xcheck]
                    if self.start in currentnode.connections:
                        self.map[self.start[0]][self.start[1]].connections.append([ycheck,xcheck])

    def is_in_grid(self, y, x):
        if y >= 0 and y <= len(self.visitmatrix):
            if x >= 0 and x <= len(self.visitmatrix):
                return True
        return False

    def display_map(self):
        for line in self.rawmaplist:
            print(line)

    def display_visit_matrix(self):
        for line in self.visitmatrix:
            print(line)
    def walk_the_map(self):
        stepcount = 0
        position = self.start
        print(self.visitmatrix[position[0]][position[1]])
        while self.visitmatrix[position[0]][position[1]] == False:
            self.visitmatrix[position[0]][position[1]] = 1
            for next_positions in self.map[position[0]][position[1]].connections:
                if self.visitmatrix[next_positions[0]][next_positions[1]] == False:
                    stepcount += 1

                    position = next_positions
                    break
        self.display_visit_matrix()
        return stepcount // 2 + 1

