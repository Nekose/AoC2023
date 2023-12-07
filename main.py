'''
Ready for AoC 2024!
'''

import src.tools as tools
import src.day6 as day6

data = tools.input_parser("data/day6part2.txt")
input = day6.process_input(data)
print(day6.return_wins(input[0],input[1]))
