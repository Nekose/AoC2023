from typing import List
class almanac(object):
    def __init__(self,input_table: List["almanac_entries"]) -> None:
        self.contents = {}
        for almanac in input_table:
            self.contents[almanac.name] = almanac

    def __str__(self) -> str:
        return str([str(x) for x in self.contents.values()])

class almanac_entries(object):
    def __init__(self,input: list[list],name,target) -> None:
        self.map = {}
        for line in input:
            #example: [50,98,2]
            print(line)
            destination_range_start = int(line[0])
            source_range_start = int(line[1])
            range_length = int(line[2])
            for step in range(range_length):
                    self.map[source_range_start + step]=destination_range_start + step
        self.name = name
        self.target = target

    def __str__(self) -> str:
        return f"Almanac titled '{self.name}' which targets '{self.target}'"

def parse_input(data):
    subentry = []
    for rownum,row in enumerate(data):
        if rownum == 0:
            seedlist = row.split(": ")[1].split()
        elif row == "":
            pass
        elif data[rownum - 1] == "":
                while row != "":
                    subentry.append(row)
                firstline = subentry[0]
                firstline.split.split("-")
                almanac_name = firstline[0]
                almanac_target = firstline[2]
    print(subentry)