'''
Ready for AoC 2024!
'''

import src.tools as tools
from src.day8 import Map
raw_data = tools.input_parser("data/day8.txt")
desertmap = Map(raw_data)
print(desertmap.start_ghost_walking())