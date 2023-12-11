'''
Ready for AoC 2024!
'''

import src.tools as tools
from src.day10 import pipenode,map
raw_data = tools.input_parser("data/day10test.txt")
testmap = map(raw_data)
testpipe = pipenode("-",2,2)
print(testpipe)
testmap.display_map()
print(testmap.visitmatrix)
print(testmap.map)
print(testmap.start)