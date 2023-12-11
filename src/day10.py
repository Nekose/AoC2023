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
        return f"A '{self.pipestr}' pipe at Y={self.ypos},X={self.xpos}, connecting {self.connections[0]} and {self.connections[1]}"

class map(object):
    def __init__(self,maplist):
        self.rawmaplist = maplist
        self.map = []
        self.visitmatrix = []
        for line in maplist:
            self.visitmatrix.append("X"*len(line))
        for ypos,row in enumerate(maplist):
            for xpos,node in enumerate(row):
                self.map.append(pipenode(node,ypos,xpos))
                if node == "S":
                    self.start = [ypos,xpos]
        #TODO determine start connections
        for y in range(-1, 2, 1):
            for x in range(-1, 2, 1):
                if self.is_in_grid(y,x):
                    print(self.map)
                    currentnode = self.map[y][x]
                    if self.start in currentnode.connections:
                        currentnode.connections.append([y,x])

    def is_in_grid(self, y, x):
        if y >= 0 and y <= len(self.visitmatrix):
            if x >= 0 and x <= len(self.visitmatrix):
                return True
        return False

    def display_map(self):
        for line in self.rawmaplist:
            print(line)
