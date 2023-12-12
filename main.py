'''
Ready for AoC 2024!
'''

import src.tools as tools
from src.day10 import pipenode,Map
raw_data = tools.input_parser("data/day10test.txt")
testmap = Map(raw_data)
testpipe = pipenode("-",2,2)

testmap.display_map()
print(testmap.walk_the_map())