'''
create a matrix of "accept" zones surrounding symboles. Reference digits to see if a single digit resides in a safe zone, if so add to list
'''
def find_valid_codes(matrix: list) -> int:
    codetable = []
    accept_matrix = create_accept_matrix(matrix)
    for rownum,rowdata in enumerate(matrix):
        currentnum = ""
        positions = []
        for colnum,value in enumerate(rowdata):
            if value.isnumeric():
                currentnum += value
                positions.append((rownum,colnum))
            if (not value.isnumeric() and len(currentnum) > 0) or (colnum == len(rowdata)-1 and len(currentnum) > 0):
                for check in positions:
                    row,col = check[0],check[1]
                    if accept_matrix[row][col] == True:
                        codetable.append(int(currentnum))
                        break
                currentnum = ""
                positions = []
    return sum(codetable)

def find_gear_ratios(matrix: list) -> int:
    codetable = []
    numtable_check = set()
    numbermatrix = create_number_position_matrix(matrix)
    for rownum,rowdata in enumerate(matrix):
        for colnum,value in enumerate(rowdata):
            if value == "*":
                for y in range(-1,2):
                    for x in range(-1,2):
                        if is_in_grid(rownum+y,colnum+x,matrix):
                            if numbermatrix[rownum+y][colnum+x] != None:
                                numtable_check.add((numbermatrix[rownum+y][colnum+x][0],numbermatrix[rownum+y][colnum+x][1]))
                if len(numtable_check) > 1:
                    first = numtable_check.pop()
                    second = numtable_check.pop()
                    codetable.append(int(first[0]) * int(second[0]))
                else:
                    numtable_check.clear()
    return sum(codetable)

def create_number_position_matrix(matrix: list) -> list:
    return_matrix = [[None for x in range(len(matrix[0]))] for x in range(len(matrix))]
    unique_counter = 0
    for rownum,rowdata in enumerate(matrix):
        currentnum = ""
        positions = []
        for colnum,value in enumerate(rowdata):
            if value.isnumeric():
                currentnum += value
                positions.append((rownum, colnum))
            if (not value.isnumeric() and len(currentnum) > 0) or (colnum == len(rowdata) - 1 and len(currentnum) > 0):
                for position in positions:
                    row, col = position[0], position[1]
                    return_matrix[row][col] = currentnum,unique_counter
                currentnum = ""
                positions = []
                unique_counter += 1
    return return_matrix

def create_accept_matrix(matrix: list) -> list:
    returnmatrix = [[0 for x in range(len(matrix[0]))] for x in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            #check self
            if is_symbol(matrix[row][col]):
                for y in range(-1,2):
                    for x in range(-1,2):
                        if is_in_grid(row+y,col+x,matrix):
                            returnmatrix[row+y][col+x] = 1
    for line in returnmatrix:
        print(line)
    return returnmatrix

def is_symbol(character: str) -> bool:
    if character.isnumeric() or character == ".":
        return False
    return True

def is_in_grid(row,col,matrix):
    if row >= 0 and row <= len(matrix):
        if col >= 0 and col <= len(matrix[0]):
            return True
    return False